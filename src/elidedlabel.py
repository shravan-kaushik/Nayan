from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QLabel


class ElidedLabel(QLabel):
    """A subclass of QLabel that shows elided text."""

    def __init__(self, parent=None):
        """Initializes the GUI for the dialog."""
        super(ElidedLabel, self).__init__(parent)
        self.elideMode_ = Qt.ElideLeft
        self.cached_elided_text = ""

    def setText(self, text):
        QLabel.setText(self, text)
        self.cache_elided_text(self.geometry().width())

    def cache_elided_text(self, w):
        self.cached_elided_text = self.fontMetrics().elidedText(
            self.text(), self.elideMode_, w, Qt.TextShowMnemonic)

    def resizeEvent(self, e):
        QLabel.resizeEvent(self, e)
        self.cache_elided_text(e.size().width())

    def paintEvent(self, e):
        p = QPainter(self)
        p.drawText(0, 0,
                   self.geometry().width(),
                   self.geometry().height(),
                   self.alignment(),
                   self.cached_elided_text)

    def clear(self):
        self.setText("")
