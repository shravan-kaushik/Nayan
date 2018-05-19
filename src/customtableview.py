from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import pyqtSignal


class CustomTableView(QTableView):
    itemSelectionChanged = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)

    def selectionChanged(self, item1, item2):
        super(CustomTableView, self).selectionChanged(item1, item2)
        self.itemSelectionChanged.emit()
