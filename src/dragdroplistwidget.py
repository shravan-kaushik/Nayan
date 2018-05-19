from glob import iglob
from os.path import isfile, isdir

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget


class DragDropListWidget(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self._items_added_callback_fn = None

    def set_items_added_callback_fn(self, fn):
        self._items_added_callback_fn = fn

    def add_unique(self, paths):
        from os.path import normpath
        from os import scandir

        # the following is the list of image types readable by Qt
        supported_exts = {"bmp", "gif", "jpeg", "jpg", "png",
                          "pbm", "pgm", "ppm", "xbm", "xpm"}

        # the following is the list of image types supported by PIL
        # exts = {"bmp", "cur", "dcx", "dds", "eps", "gif", "icns", "ico",
        #         "im", "imt", "j2k", "j2p", "jfif", "jpeg", "jpg", "jpx",
        #         "msp", "pcx", "png", "ppm", "spi", "tiff", "webp", "xbm",
        #         "xpm"}

        def search_for_images(path):
            for entry in scandir(path):
                if entry.is_dir(follow_symlinks=True):
                    yield from search_for_images(entry.path)
                else:
                    entry_path = entry.path
                    if entry_path.split(".")[-1] in supported_exts:
                        yield entry_path

        if not isinstance(paths, list):
            paths = [paths]

        filenames = []

        for p in paths:
            p = normpath(p)
            # ORIGINAL
            # files = iglob(u"%s/**/*.*" % p, recursive=True)
            # filenames += [f for f in files if is_supported_image(f)]
            # ORIGINAL
            if isfile(p):
                filenames.append(p)
            else:
                filenames += [f for f in search_for_images(p)]

        set_items = set([self.item(i).text() for i in range(self.count())])
        filenames = [x for x in filenames if x not in set_items]

        self.addItems(filenames)
        self._items_added_callback_fn()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Delete:
            take_item = self.takeItem
            row = self.row
            for item in self.selectedItems():
                take_item(row(item))
            self._items_added_callback_fn()
        super().keyPressEvent(e)
