from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QAbstractItemView


class DragOrderableList(QListWidget):
    itemMoved = pyqtSignal(int, int,
                           QListWidgetItem)  # Old index, new index, item

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.drag_item = None
        self.drag_row = None

    def dropEvent(self, event):
        super().dropEvent(event)
        self.itemMoved.emit(self.drag_row, self.row(self.drag_item),
                            self.drag_item)
        self.drag_item = None

    def startDrag(self, supported_actions):
        self.drag_item = self.currentItem()
        self.drag_row = self.row(self.drag_item)
        super().startDrag(supported_actions)

    def addItem(self, item):
        item.setSizeHint(QSize(item.sizeHint().width(), 26))
        super().addItem(item)

    def up(self):
        if self.currentRow():
            cr = self.currentRow()
            self.insertItem(cr - 1, self.takeItem(cr))
            self.setCurrentRow(cr - 1)

    def down(self):
        if self.currentRow() < self.count() - 1:
            self.insertItem(self.currentRow() + 1, self.takeItem(self.currentRow()))
            self.setCurrentRow(self.currentRow() + 1)
