import pyximport; pyximport.install()


def main():
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtGui import QPalette, QColor, QIcon
    from mainwindow import MainWindow
    import sys

    app = QApplication(sys.argv)
    app.setStyle("fusion")
    mw = MainWindow()
    mw.setWindowIcon(QIcon(":/icon.png"))
    mw.setWindowTitle("Nayan")
    mw.LIGHT_PALETTE = app.palette()
    mw.LIGHT_PALETTE.setColor(QPalette.Highlight, QColor("#34DB8A"))  # 3498DB
    mw.DARK_PALETTE = app.palette()
    mw.DARK_PALETTE.setColor(QPalette.Base, QColor("#2B2B2B"))
    mw.DARK_PALETTE.setColor(QPalette.Window, QColor("#3C3F41"))
    mw.DARK_PALETTE.setColor(QPalette.WindowText, QColor("#FFFFFF"))
    mw.DARK_PALETTE.setColor(QPalette.Highlight, QColor("#34DB8A"))  # 3498DB
    mw.DARK_PALETTE.setColor(QPalette.Text, QColor("#FFFFFF"))
    mw.DARK_PALETTE.setColor(QPalette.Button, QColor("#3C3F41"))
    mw.DARK_PALETTE.setColor(QPalette.ButtonText, QColor("#FFFFFF"))
    mw.DARK_PALETTE.setColor(QPalette.Link, QColor("#F44336"))
    mw.DARK_PALETTE.setColor(QPalette.LinkVisited, QColor("#D32F2F"))
    app.setPalette(mw.DARK_PALETTE)
    app.setApplicationName("Nayan")
    app.setApplicationVersion("1.0")
    app.aboutToQuit.connect(mw.stop_everything_before_exit)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
