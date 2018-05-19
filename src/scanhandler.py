import sqlite3
from concurrent.futures import ProcessPoolExecutor, as_completed
from itertools import product, combinations, chain
from os.path import isfile
from os import remove as delete_file
# from PIL import Image
from PyQt5.QtCore import QThread, QMutex, pyqtSignal
from imagehash import *


class Pair:
    """
    A class specifically created to store a pair of filenames in a frozenset
    so that they can be hashed in order to be used as dictionary keys.
    """

    def __init__(self, a, b):
        self.A = a
        self.B = b

    def __hash__(self):
        return hash(frozenset((self.A, self.B)))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __ne__(self, other):
        return not (hash(self) == hash(other))


def hash_file(hash_fn, filename):
    img = Image.open(filename)
    try:
        ret_tup = filename, (hash_fn(img),
                             # hash_fn(img.transpose(Image.ROTATE_90)),
                             # hash_fn(img.transpose(Image.ROTATE_180)),
                             # hash_fn(img.transpose(Image.ROTATE_270)),
                             # hash_fn(img.transpose(Image.FLIP_LEFT_RIGHT)),
                             # hash_fn(img.transpose(Image.FLIP_TOP_BOTTOM))
                             )
    except:
        return (None, None,)
    return ret_tup


# noinspection SqlResolve
class Scanner(QThread):
    sig_progress_changed = pyqtSignal(int)
    sig_stopped = pyqtSignal()  # emitted when processing is abruptly stopped
    sig_finished = pyqtSignal()  # emitted when everything completes nicely
    sig_reset_progress = pyqtSignal()
    sig_set_operation_text = pyqtSignal(str)

    def __init__(self, filenames, hash_fn, threshold, database_name, parent=None):
        super(Scanner, self).__init__(parent)

        def get_fn_from_str(s):
            if s == "dHash":
                return dhash
            elif s == "pHash":
                return phash
            elif s == "pHash-simple":
                return phash_simple
            elif s == "wHash":
                return whash
            else:
                return average_hash

        self._filenames = filenames
        self._hash_fn = get_fn_from_str(hash_fn)
        if isfile(database_name):
            delete_file(database_name)
        self._duplicates_db = sqlite3.connect(database_name, check_same_thread=False)
        self._duplicates_db.execute("CREATE TABLE dups (file1 TEXT, file2 TEXT, similarity INTEGER)")
        self._threshold = threshold
        self._total_count = 0
        self._done_count = 0
        self._last_perc = 0
        self._stopping = False
        self._futures = []
        self._mutex = QMutex()
        self._mutex_done_count = QMutex()
        self._executor = ProcessPoolExecutor()
        self._hashes = {}
        self.info = {}
        self.duplicates = {}

    def run(self):
        import time

        self.sig_set_operation_text.emit("Analyzing images...")
        self._total_count = len(self._filenames)

        for filename in self._filenames:
            if self.isInterruptionRequested():
                self.stop()
                return
            if isfile(filename):
                r = self._executor.submit(hash_file,
                                          self._hash_fn,
                                          filename)
                self._futures.append(r)
                r.add_done_callback(self.cb_hash_file)
            else:
                self.increment_done_count()
        for f in as_completed(self._futures):
            if self.isInterruptionRequested():
                self.stop()
                return

        self.sig_reset_progress.emit()
        self.sig_set_operation_text.emit("Finding duplicates...")

        start_time = time.clock()

        def get_total(num_files, num_hashes_for_an_img):
            try:
                from gmpy2 import comb as nCr
            except ImportError:
                def nCr(n, k):
                    """
                    A fast way to calculate binomial coefficients by Andrew Dalke.
                    """
                    if 0 <= k <= n:
                        ntok = 1
                        ktok = 1
                        for t in range(1, min(k, n - k) + 1):
                            ntok *= n
                            ktok *= t
                            n -= 1
                        return ntok // ktok
                    else:
                        return 0

            return nCr((num_files * num_hashes_for_an_img), 2) - (
                nCr(num_hashes_for_an_img, 2) * num_files)

        u, v = len(self._filenames), len(self._hashes[self._filenames[0]])
        self._total_count = get_total(u, v)
        self._futures.clear()
        self._done_count = 0
        self._last_perc = 0

        cur = self._duplicates_db.cursor()
        hash_d = self._hashes
        for l in combinations(chain.from_iterable(
                [p for p in [product([x], hash_d[x]) for x in hash_d]]), 2):
            if self.isInterruptionRequested():
                self.stop()
                return
            m, n = l
            if m[0] != n[0]:
                similarity = 100 - (m[1] - n[1])
                if similarity >= self._threshold:
                    try:
                        cur.execute(
                            "SELECT similarity FROM dups WHERE file1=? AND file2=?", (m[0], n[0],))
                        old_val = cur.fetchone()[0]
                        print("Similarity", similarity, "and Old Val", old_val)
                        if similarity > old_val:
                            cur.execute(
                                "UPDATE dups SET similarity=? WHERE file1=? AND file2=?",
                                (int(similarity), m[0], n[0]))
                    except Exception as e:
                        cur.execute(
                            "INSERT INTO dups VALUES (?, ?, ?)", (m[0], n[0], int(similarity)))
                self.increment_done_count()
        self._duplicates_db.commit()
        self._duplicates_db.close()

        for f in as_completed(self._futures):
            if self.isInterruptionRequested():
                self.stop()
                return

        clk = time.clock() - start_time
        if not self._stopping:
            with open("timetaken.txt", "a") as w:
                w.write("It took %f seconds to crunch %d image combinations.\n" % (
                    clk, self._total_count))

        if not self._stopping:
            self._filenames.clear()
            self._futures.clear()
            self._executor = None
            self._hashes.clear()
            self.sig_finished.emit()

    def cb_hash_file(self, retval):
        try:
            filename, hashes = retval.result()
        except:
            return
        if filename:
            self._mutex.lock()
            self._hashes[filename] = hashes
            self._mutex.unlock()
            self.increment_done_count()

    def increment_done_count(self):
        self._mutex_done_count.lock()
        self._done_count += 1
        perc = int(self._done_count / self._total_count * 100)
        if perc != self._last_perc:
            self._last_perc = perc
            self.sig_progress_changed.emit(perc)
        self._mutex_done_count.unlock()

    def stop(self):
        if not self._stopping:
            self._stopping = True
            self.sig_set_operation_text.emit("Stopping... Please wait")
            for f in self._futures:
                f.cancel()
            self._executor.shutdown()
            self.sig_stopped.emit()
