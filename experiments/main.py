# import pyximport; pyximport.install()
from proc_concurrentfutures import Scanner

from PyQt5.QtWidgets import (QWidget,
                             QApplication,
                             QPushButton,
                             QProgressBar,
                             QVBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize


class Wind(QWidget):
    def __init__(self, parent=None):
        super(Wind, self).__init__(parent)
        self.count = 0
        self.layout = QVBoxLayout(self)
        self.btn = QPushButton(self)
        self.prog = QProgressBar(self)
        self.prog.setMaximum(100)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.prog)
        self.btn.setFont(QFont("Segoe UI", 9))
        self.setMinimumSize(QSize(300, 300))
        self.proc = None
        self.btn.clicked.connect(self.do_da_job)
        self.show()

    def clean_exit(self):
        if self.proc and self.proc.isRunning():
            print("I'm trying to clean up your mess... >(")
            self.proc.stop()

    def do_da_job(self):
        filenames = [
            "./Doggo-1.png",
            "./Doggo-2.png",
            "./Doggo-3.png",
            "./Doggo-4.png",
            "./Doggo-5.png",
            "./Doggo-6.png",
            "./Doggo-7.png",
            "./Doggo-8.png",
            "./Doggo-9.png",
        ]
        self.proc = Scanner(filenames, "dHash", 90, self)
        self.btn.clicked.disconnect()
        self.btn.setText("Starting now...")
        self.proc.sig_one_more_done.connect(self.prog.setValue)
        self.btn.clicked.connect(lambda: self.prog.setMaximum(0))
        self.btn.clicked.connect(self.proc.stop)
        self.proc.start()


def main():
    import sys
    app = QApplication(sys.argv)
    w = Wind()
    app.aboutToQuit.connect(w.clean_exit)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


# def doer(p):
#     return p + 1


# class Controller:
#     def doda(self):
#         res = None
#         with mp.Pool() as pool:
#             res = pool.map(doer, range(5))
#         print(res)


# class Controller2:
#     def doda(self):
#         res = None
#         with ProcessPoolExecutor() as pool:
#             res = pool.map(doer, range(5))
#         print(res)

# if __name__ == "__main__":
#     c = Controller2()
#     c.doda()
