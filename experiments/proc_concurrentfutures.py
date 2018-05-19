from concurrent.futures import CancelledError, ProcessPoolExecutor, wait as wait_for_completion
from multiprocessing import Manager
from itertools import combinations, product, starmap
from os.path import basename, getsize as filesize
from PIL import Image
from PyQt5.QtCore import QThread, QMutex, pyqtSignal
from gmpy2 import comb as nCr


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

    def swap(self):
        temp = self.A
        self.A = self.B
        self.B = temp


def scan(hash_fn, threshold, img_1_filename, img_2_filename, q):
    nonetup = (None, None, None, None, None, None)
    img_1_img = Image.open(img_1_filename)
    if q.full():
        return nonetup
    img_1_hashes = [hash_fn(img_1_img)]
    # hash_fn(img_1_img.rotate(90)),
    # hash_fn(img_1_img.rotate(180)),
    # hash_fn(img_1_img.rotate(270)),
    # hash_fn(img_1_img.transpose(FLR)),
    # hash_fn(img_1_img.transpose(FTB))]
    if q.full():
        return nonetup
    img_2_img = Image.open(img_2_filename)
    if q.full():
        return nonetup
    img_2_hashes = [hash_fn(img_2_img)]
    # hash_fn(img_2_img.rotate(90)),
    # hash_fn(img_2_img.rotate(180)),
    # hash_fn(img_2_img.rotate(270)),
    # hash_fn(img_2_img.transpose(FLR)),
    # hash_fn(img_2_img.transpose(FTB))]

    prods = product(img_1_hashes, img_2_hashes)
    if q.full():
        return nonetup
    max_similarity = 100 - max(starmap(lambda a, b: a - b, prods))
    if q.full():
        return nonetup
    print("Max similarity: %d" % max_similarity)

    if max_similarity >= threshold:
        img_1_info = (basename(img_1_filename),
                      filesize(img_1_filename),
                      img_1_img.size)
        if q.full():
            return nonetup
        img_2_info = (basename(img_2_filename),
                      filesize(img_2_filename),
                      img_2_img.size)

        if q.full():
            return nonetup
        # TODO: Analyze the precedence rules
        img_a, img_b = img_1_filename, img_2_filename
        if q.full():
            return nonetup
        key = Pair(img_a, img_b)

        return (img_1_filename,
                img_2_filename,
                img_1_info,
                img_2_info,
                key,
                max_similarity)
    else:
        return nonetup


class Scanner(QThread):
    sig_one_more_done = pyqtSignal(int)  # emitted after each "micro-action"
    sig_stopped = pyqtSignal()  # emitted when processing is abruptly stopped
    sig_finished = pyqtSignal()  # emitted when everything completes nicely

    def __init__(self, filenames, hash_fn, threshold, parent=None):
        super(Scanner, self).__init__(parent)

        def get_fn_from_str(s):
            from imagehash import dhash, phash, average_hash as ahash
            if s == "dHash":
                return dhash
            elif s == "pHash":
                return phash
            else:
                return ahash

        self._filenames = filenames
        self._hash_fn = get_fn_from_str(hash_fn)
        self._threshold = threshold
        self._total_count = 0
        self._done_count = 0
        self._stopping = False
        self._futures = []
        self._mutex = QMutex()
        self._executor = ProcessPoolExecutor()
        self._manager = Manager()
        self._queue = self._manager.Queue(1)
        self.info = {}
        self.duplicates = {}

    def run(self):
        payloads = combinations(self._filenames, 2)
        self._total_count = int(nCr(len(self._filenames), 2))

        for p in payloads:
            f1, f2 = p
            r = self._executor.submit(scan,
                                      self._hash_fn,
                                      self._threshold,
                                      f1,
                                      f2,
                                      self._queue)
            self._futures.append(r)
            r.add_done_callback(self.call_me_when_done)
        wait_for_completion(self._futures)
        if not self._stopping:
            print("I finished!")

        if not self._stopping:
            self.sig_finished.emit()
            print("Run done!")

    def call_me_when_done(self, retval):
        try:
            img1_fname, img2_fname, img1_info, img2_info, key, similarity = retval.result()
        except CancelledError:
            return

        self._mutex.lock()
        if img1_fname:
            if img1_fname not in self.info:
                self.info[img1_fname] = img1_info
            if img2_fname not in self.info:
                self.info[img2_fname] = img2_info
            dups = self.duplicates
            if (key not in dups) or (dups[key] < similarity):
                dups[key] = similarity

        self._done_count += 1
        perc = int(self._done_count / self._total_count * 100)
        self.sig_one_more_done.emit(perc)
        self._mutex.unlock()

    def stop(self):
        if not self._stopping:
            self._stopping = True
            self._queue.put(1)
            for f in self._futures:
                f.cancel()
        self._executor.shutdown()
        self.sig_stopped.emit()
