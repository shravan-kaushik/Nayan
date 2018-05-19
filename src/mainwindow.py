from platform import system as cur_system
from subprocess import Popen

from PyQt5.QtCore import (Qt,
                          QEasingCurve,
                          QPropertyAnimation)
from PyQt5.QtWidgets import (QApplication,
                             QCheckBox,
                             QFileDialog,
                             QGraphicsOpacityEffect,
                             QHeaderView,
                             QMainWindow,
                             QMenu,
                             QMessageBox,
                             QProgressDialog,
                             QTableWidgetItem)
from send2trash import send2trash
from PIL import Image
from imageviewer import ImageViewer
from scanhandler import Scanner
from os.path import basename, getsize as filesize


class MainWindow(QMainWindow):
    """
    The main GUI window class.
    """
    DARK_PALETTE = None
    LIGHT_PALETTE = None
    ACTIVE_PALETTE = 1  # 0 is light, 1 is dark

    def __init__(self):
        """
        C-tor.
        """
        super().__init__()
        from mainwindow_ui import Ui_MainWindow
        from PyQt5.QtCore import QStandardPaths
        from os import makedirs

        appdata_loc = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        try:
            makedirs(appdata_loc, exist_ok=True)
        except:
            appdata_loc = QStandardPaths.writableLocation(QStandardPaths.CacheLocation)

        self.defaults = {
            "THRESHOLD": 90,
            "ALGORITHM": "dHash",
            "DB_LOCATION": appdata_loc + "/.nayan.db"
        }
        self.all_selected = False
        self.scanner = None
        self.dups_db_model = None
        self.confirm_delete = True
        self.anim1 = None
        self.anim2 = None
        self.image_viewer1 = ImageViewer(self)  # adding these to Ui_MainWindow causes the "wrapped
        self.image_viewer2 = ImageViewer(self)  # C++ object of type QLabel has been deleted" issue

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_ui_more()
        self.setup_connections()
        self.show()
        # self.ui.listWidget_targets.add_unique(
        #     "E:/Life/Programming/Own Projects/Finished/Nayan/testimages-general")

    def setup_ui_more(self):
        """
        Performs additional GUI initialization tasks.
        :return:
        """
        self.ui.gridLayout_img1.addWidget(self.image_viewer1, 3, 0, 1, 5)
        self.ui.gridLayout_img2.addWidget(self.image_viewer2, 3, 0, 1, 5)
        self.ui.spinBox_threshold.setValue(self.defaults["THRESHOLD"])
        self.ui.comboBox_algorithm.setCurrentText(self.defaults["ALGORITHM"])
        self.ui.groupBox_scanOptions.hide()
        self.ui.splitter.setStretchFactor(0, 5)
        self.ui.splitter.setStretchFactor(1, 2)
        menu = QMenu(self)
        menu.addAction("Apply auto-delete on all pairs", self.auto_del_all)
        self.ui.toolButton_autoDel.setMenu(menu)
        self.setAcceptDrops(True)

        import qtawesome as qta
        self.ui.pushButton_img1Delete.setIcon(
            qta.icon("fa.trash", color="white", color_active="#34DB8A"))
        self.ui.pushButton_img2Delete.setIcon(
            qta.icon("fa.trash", color="white", color_active="#34DB8A"))
        self.ui.pushButton_img1OpenFolder.setIcon(
            qta.icon("fa.folder-open", color="white", color_active="#34DB8A"))
        self.ui.pushButton_img2OpenFolder.setIcon(
            qta.icon("fa.folder-open", color="white", color_active="#34DB8A"))
        self.ui.pushButton_swap.setIcon(
            qta.icon("fa.exchange", color="white", color_active="#34DB8A"))
        self.ui.pushButton_up.setIcon(
            qta.icon("fa.arrow-up", color="white", color_active="#34DB8A"))
        self.ui.pushButton_down.setIcon(
            qta.icon("fa.arrow-down", color="white", color_active="#34DB8A"))
        self.ui.pushButton_rotateImg1.setIcon(
            qta.icon("fa.rotate-right", color="white", color_active="#34DB8A"))
        self.ui.pushButton_rotateImg2.setIcon(
            qta.icon("fa.rotate-right", color="white", color_active="#34DB8A"))
        self.ui.toolButton_autoDel.setIcon(
            qta.icon("fa.magic", color="white", color_active="#34DB8A"))
        self.ui.pushButton_scan.setIcon(
            qta.icon("fa.search", color="white", color_active="#34DB8A"))
        self.ui.pushButton_cancelOperation.setIcon(
            qta.icon("fa.times-circle", color="white", color_active="#34DB8A"))

    def setup_connections(self):
        """
        Sets up the signal-slot connections of various UI elements.
        :return: 
        """
        self.ui.listWidget_targets.set_items_added_callback_fn(self.update_items_count)
        self.ui.listWidget_targets.itemSelectionChanged.connect(self.reset_all_selected)
        self.ui.pushButton_addFilesFolders.clicked.connect(self.add_files_folders)
        self.ui.pushButton_selectAll.clicked.connect(self.select_deselect_all)
        self.ui.pushButton_removeSelected.clicked.connect(self.remove_selected)
        self.ui.pushButton_resetScanOptions.clicked.connect(self.reset_scan_options)
        self.ui.pushButton_scan.clicked.connect(self.scan)
        self.ui.tableView_results.itemSelectionChanged.connect(self.result_table_selection_changed)
        self.ui.pushButton_swap.clicked.connect(self.swap_images)
        self.ui.pushButton_delBoth.clicked.connect(self.del_both)
        self.ui.toolButton_autoDel.clicked.connect(self.auto_del)
        self.ui.pushButton_img1Delete.clicked.connect(self.del_left_image)
        self.ui.pushButton_img2Delete.clicked.connect(self.del_right_image)
        self.ui.pushButton_img1OpenFolder.clicked.connect(self.open_left_img_folder)
        self.ui.pushButton_img2OpenFolder.clicked.connect(self.open_right_img_folder)
        self.ui.pushButton_rotateImg1.clicked.connect(self.image_viewer1.rotate_image)
        self.ui.pushButton_rotateImg1.clicked.connect(self.ui.tableView_results.setFocus)
        self.ui.pushButton_rotateImg2.clicked.connect(self.image_viewer2.rotate_image)
        self.ui.pushButton_rotateImg2.clicked.connect(self.ui.tableView_results.setFocus)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionToggle_theme.triggered.connect(self.toggle_theme)
        self.ui.pushButton_up.clicked.connect(self.ui.listWidget_autoDelRules.up)
        self.ui.pushButton_down.clicked.connect(self.ui.listWidget_autoDelRules.down)

    def resizeEvent(self, e):
        """
        This is an overridden method that is called whenever the main window is resized. It
        changes the size of the headers in the results table.

        :param e: QResizeEvent variable containing information about the event.
        :return: 
        """
        self.ui.tableView_results.resizeColumnsToContents()
        if self.ui.tableView_results.horizontalHeader():
            self.ui.tableView_results.horizontalHeader().setSectionResizeMode(0,
                                                                              QHeaderView.Stretch)
            self.ui.tableView_results.horizontalHeader().setSectionResizeMode(1,
                                                                              QHeaderView.Stretch)

    def dragEnterEvent(self, e):
        """
        This is an overridden method that is called whenever a drag is initiated over tab #0 of
        the central QTabWidget.

        :param e: QDragEnterEvent variable containing information about the event.
        :return: 
        """
        if not self.ui.tabWidget.currentIndex():
            if e.mimeData().hasUrls():
                e.accept()

    def dropEvent(self, e):
        """
        This is an overridden method that is called whenever a drop happens over tab 0 of the
        central QTabWidget. It is used to send information to the targets list widget.

        :param e: QDropEvent variable containing information about the event.
        :return:
        """
        if not self.ui.tabWidget.currentIndex():
            mime_data = e.mimeData()
            if mime_data.hasUrls():
                self.add_files_folders([x.toLocalFile() for x in mime_data.urls()])
                e.accept()

    @staticmethod
    def sizeof_fmt(num):
        """
        Converts a number to a formatted file-size string.

        Examples:
            1024 -> 1 KiB
            3233432 -> 3.1 MiB

        :param num: The number to be formatted.
        :return: The file-size as a formatted string.
        """
        for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti']:
            if abs(num) < 1024.0:
                return "%3.1f %sB" % (num, unit)
            num /= 1024.0
        return "%.1f%sB" % (num, 'Yi')

    @staticmethod
    def open_folder(path):
        """
        Opens a path using the standard file manager of the host OS.
        :param path: The path to be opened.
        :return:
        """
        if cur_system() == "Windows":
            Popen(["explorer", "/select,", path])
        elif cur_system() == "Darwin":
            Popen(["open", path])
        else:
            Popen(["xdg-open", path])

    def add_files_folders(self, paths=None):
        """
        This SLOT responds to the user clicking the "Add files/folders..." button. It also
        doubles up as a response to the user "dragging a folder".
        :param paths: The optional list of paths obtained from a drag-and-drop. If this is None,
        it is assumed that this method was triggered by the user clicking the
        "Add files/folders..." button.
        :return:
        """
        if not paths:
            from PyQt5.QtWidgets import (QAbstractItemView,
                                         QListView,
                                         QTreeView)

            dlg = QFileDialog(self, "Add files/folders...")
            dlg.setAcceptMode(QFileDialog.AcceptOpen)
            dlg.setFileMode(QFileDialog.Directory)
            dlg.setOption(QFileDialog.DontUseNativeDialog)
            l = dlg.findChild(QListView, "listView")
            if l:
                l.setSelectionMode(QAbstractItemView.MultiSelection)
            t = dlg.findChild(QTreeView)
            if t:
                t.setSelectionMode(QAbstractItemView.MultiSelection)
            if not dlg.exec_():
                return
            paths = dlg.selectedFiles()
        mb = QMessageBox(QMessageBox.Information,
                         "Nayan - Information",
                         "Please wait...\n"
                         "This may take a while and Nayan may seem unresponsive.")
        mb.show()
        QApplication.processEvents()
        self.ui.listWidget_targets.add_unique(paths)
        mb.hide()

    def update_items_count(self):
        """
        Updates the "Number of files" label whenever files are added to or removed from the list
        of targets.
        :return:
        """
        self.ui.label_no_of_items.setText("Number of files: %d" %
                                          self.ui.listWidget_targets.count())

    def reset_all_selected(self):
        """
        Two lines of code. Fucking read them.
        :return:
        """
        self.all_selected = False
        self.ui.pushButton_selectAll.setText("Select all")

    def select_deselect_all(self):
        """
        Selects or deselects all the items in the list of targets.
        :return:
        """
        if not self.all_selected and self.ui.listWidget_targets.count():
            self.ui.listWidget_targets.selectAll()
            self.ui.pushButton_selectAll.setText("Deselect all")
            self.all_selected = True
        else:
            self.ui.listWidget_targets.clearSelection()
            self.reset_all_selected()

    def remove_selected(self):
        """
        Removes the selected item from the list of targets.
        :return:
        """
        take_item = self.ui.listWidget_targets.takeItem
        row = self.ui.listWidget_targets.row
        for item in self.ui.listWidget_targets.selectedItems():
            take_item(row(item))
        self.update_items_count()

    def reset_scan_options(self):
        """
        Resets all the scan options to their defaults.
        :return:
        """
        self.ui.dial_threshold.setValue(self.defaults["THRESHOLD"])
        self.ui.spinBox_threshold.setValue(self.defaults["THRESHOLD"])
        self.ui.comboBox_algorithm.setCurrentText(self.defaults["ALGORITHM"])

    def scan(self):
        """
        Starts the "scan" (hashing, duplicate finding) or all the items in the targets list.
        :return:
        """
        from PyQt5.QtCore import QThread

        if self.ui.listWidget_targets.count() < 2:
            QMessageBox.warning(self,
                                "Warning - Nayan",
                                "You need to add at least 2 images to the target list.")
            return
        self.set_ui_frozen(True)
        self.ui.label_operationLabel.setText("Starting...")
        self.ui.progressBar_operation.setMaximum(100)
        self.ui.progressBar_operation.setValue(0)
        self.ui.stackedWidget.setCurrentIndex(1)
        QApplication.processEvents()

        if self.dups_db_model:
            self.dups_db_model.database().close()
            self.dups_db_model = None

        lw = self.ui.listWidget_targets
        files = [lw.item(i).text() for i in range(lw.count())]

        self.scanner = Scanner(files,
                               self.ui.comboBox_algorithm.currentText(),
                               self.ui.dial_threshold.value(),
                               self.defaults["DB_LOCATION"],
                               self)

        self.scanner.sig_set_operation_text.connect(self.ui.label_operationLabel.setText)
        self.scanner.sig_reset_progress.connect(self.ui.progressBar_operation.reset)
        self.scanner.sig_progress_changed.connect(self.ui.progressBar_operation.setValue)
        self.scanner.sig_stopped.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.scanner.sig_stopped.connect(lambda: self.set_ui_frozen(False))
        self.ui.pushButton_cancelOperation.clicked.connect(
            lambda: self.scanner.requestInterruption())
        self.scanner.sig_finished.connect(self.scan_finished)
        self.scanner.start(QThread.HighPriority)

    def clear_image_and_info(self):
        """
        Clears the images in the image viewers and the labels displaying information.
        :return:
        """
        self.ui.label_img1Name.clear()
        self.ui.label_img1Size.clear()
        self.ui.label_img1Dimension.clear()
        self.ui.label_img2Name.clear()
        self.ui.label_img2Size.clear()
        self.ui.label_img2Dimension.clear()
        self.ui.label_similarity.clear()
        self.image_viewer1.clear_image()
        self.image_viewer2.clear_image()

    def scan_finished(self):
        """
        This slot is triggered when the scan finishes completely. It retrieves the information
        from the scan handler and feeds them into the GUI controls.
        :return:
        """
        from PyQt5.QtSql import QSqlTableModel, QSqlDatabase

        tbl_res = self.ui.tableView_results
        self.ui.label_operationLabel.setText("Populating table...")
        tbl_res.itemSelectionChanged.disconnect(self.result_table_selection_changed)
        self.ui.progressBar_operation.setMaximum(0)

        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName(self.defaults["DB_LOCATION"])
        if not db.open():
            QMessageBox.critical(self,
                                 "Nayan - Error",
                                 "Fatal error occurred while trying to process the results.",
                                 QMessageBox.Close)
            return
        if self.dups_db_model:
            self.dups_db_model.clear()
        self.clear_image_and_info()
        self.dups_db_model = QSqlTableModel(self, db)
        self.dups_db_model.setTable("dups")
        self.dups_db_model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.dups_db_model.select()
        self.dups_db_model.setHeaderData(0, Qt.Horizontal, "Image 1")
        self.dups_db_model.setHeaderData(1, Qt.Horizontal, "Image 2")
        self.dups_db_model.setHeaderData(2, Qt.Horizontal, "Similarity")
        self.ui.tableView_results.setModel(self.dups_db_model)

        self.scanner = None

        tbl_res.resizeColumnsToContents()
        tbl_res.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        tbl_res.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        tbl_res.sortByColumn(2, Qt.DescendingOrder)

        self.set_ui_frozen(False)
        tbl_res.itemSelectionChanged.connect(self.result_table_selection_changed)
        if self.dups_db_model.rowCount():
            self.ui.tableView_results.selectRow(0)
        self.ui.tabWidget.setCurrentIndex(1)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.tableView_results.setFocus()

    def result_table_selection_changed(self):
        """
        This slot responds when an item of the results table is selected.
        :return:
        """
        if not self.dups_db_model.rowCount():
            self.clear_image_and_info()
            return
        items = self.ui.tableView_results.selectedIndexes()
        if not items:
            self.clear_image_and_info()
            return
        img1_filename = str(items[0].data())
        img2_filename = str(items[1].data())
        self.image_viewer1.set_image(img1_filename)
        self.image_viewer2.set_image(img2_filename)
        self.ui.label_similarity.setText(str(items[2].data()) + "%")
        self.ui.label_img1Name.setText(basename(img1_filename))
        self.ui.label_img2Name.setText(basename(img2_filename))
        try:
            self.ui.label_img1Size.setText(self.sizeof_fmt(filesize(img1_filename)))
        except:
            self.ui.label_img1Size.setText("N/A")
        try:
            self.ui.label_img2Size.setText(self.sizeof_fmt(filesize(img2_filename)))
        except:
            self.ui.label_img2Size.setText("N/A")
        w, h = self.image_viewer1.width_height
        self.ui.label_img1Dimension.setText("%s x %s px" % (w, h))
        w, h = self.image_viewer2.width_height
        self.ui.label_img2Dimension.setText("%s x %s px" % (w, h))

    def swap_images(self):
        """
        Swaps the image on the right image viewer with the one on the left. Also swaps their
        details.
        :return:
        """
        if not self.dups_db_model.rowCount():
            return
        self.ui.tableView_results.setEnabled(False)
        items = self.ui.tableView_results.selectedIndexes()
        if not items:
            return

        row = items[0].row()

        filename_1 = str(items[0].data())
        filename_2 = str(items[1].data())

        db = self.dups_db_model.database()
        qs = "UPDATE dups SET file1='%s', file2='%s' WHERE file1='%s' AND file2='%s'" % (
            filename_2, filename_1, filename_1, filename_2)
        db.exec_(qs)
        db.commit()
        self.dups_db_model.submitAll()

        self.ui.tableView_results.selectRow(row)

        self.result_table_selection_changed()
        self.ui.tableView_results.setEnabled(True)
        self.ui.tableView_results.setFocus()

    def del_both(self):
        self.ui.tableView_results.setDisabled(True)
        items = self.ui.tableView_results.selectedIndexes()
        if items:
            filename_1 = str(items[0].data())
            filename_2 = str(items[1].data())
            if self.confirm_delete:
                mbox = QMessageBox(QMessageBox.Question,
                                   "Nayan - Question",
                                   "Are you sure you want to delete both the images?",
                                   QMessageBox.Yes | QMessageBox.No,
                                   self)
                if mbox.exec_() == QMessageBox.No:
                    return
            try:
                # print("Deleted %s and %s" % (filename_1, filename_2))
                send2trash(filename_1)
                send2trash(filename_2)
            except OSError:
                QMessageBox.warning(self,
                                    "Nayan - Warning",
                                    "Failed to delete one or both of the files!",
                                    QMessageBox.Close)
                self.ui.tableView_results.setEnabled(True)
                self.ui.tableView_results.setFocus()
                return

            db = self.dups_db_model.database()
            db.exec_("DELETE FROM dups WHERE file1='%s' OR file2='%s'" % (filename_1, filename_1,))
            db.exec_("DELETE FROM dups WHERE file2='%s' OR file2='%s'" % (filename_2, filename_2,))
            db.commit()

            selected_row = items[0].row()

            self.dups_db_model.submitAll()

            num_rows = self.dups_db_model.rowCount()
            if num_rows > 1:
                self.ui.tableView_results.selectRow(min(selected_row, num_rows - 1))
            elif num_rows == 1:
                self.ui.tableView_results.selectRow(0)
            else:
                self.clear_image_and_info()

        self.ui.tableView_results.setEnabled(True)
        self.ui.tableView_results.setFocus()

    def del_left_image(self):
        self.ui.tableView_results.setEnabled(False)
        items = self.ui.tableView_results.selectedIndexes()
        if items:
            self.del_image(items[0], self.image_viewer1.label)
        self.ui.tableView_results.setEnabled(True)
        self.ui.tableView_results.setFocus()

    def del_right_image(self):
        self.ui.tableView_results.setEnabled(False)
        items = self.ui.tableView_results.selectedIndexes()
        if items:
            self.del_image(items[1], self.image_viewer2.label)
        self.ui.tableView_results.setEnabled(True)
        self.ui.tableView_results.setFocus()

    def del_image(self, item, wid, interactive=True):
        filename = str(item.data())
        if self.confirm_delete:
            mbox = QMessageBox(QMessageBox.Question,
                               "Nayan - Question",
                               "Are you sure you want to delete %s?" % filename,
                               QMessageBox.Yes | QMessageBox.No,
                               self)
            cbox = QCheckBox("&Don't ask again", mbox)
            mbox.setCheckBox(cbox)
            mbox_res = mbox.exec_()
            if mbox_res == QMessageBox.No:
                return
            self.confirm_delete = not cbox.isChecked()
        try:
            # print(filename, "pseudo-deleted")
            send2trash(filename)
        except OSError:
            QMessageBox.warning(self,
                                "Nayan - Warning",
                                "Failed to delete the file! Please check whether the file exists "
                                "and Nayan has permission to delete it.",
                                QMessageBox.Close)
            return

        def whendone(tbl):
            db = self.dups_db_model.database()
            db.exec_("DELETE FROM dups WHERE file1='%s' OR file2='%s'" % (filename, filename))
            db.commit()

            selected_row = item.row()

            self.dups_db_model.submitAll()

            num_rows = self.dups_db_model.rowCount()
            if num_rows > 1:
                self.ui.tableView_results.selectRow(min(selected_row, num_rows - 1))
            elif num_rows == 1:
                self.ui.tableView_results.selectRow(0)
            else:
                self.clear_image_and_info()

            if interactive:
                anim2 = QPropertyAnimation(effect, b"opacity")
                anim2.setDuration(150)
                anim2.setStartValue(0.2)
                anim2.setEndValue(1.0)
                anim2.setEasingCurve(QEasingCurve.InExpo)
                anim2.start()
                self.anim2 = anim2

        if interactive:
            effect = QGraphicsOpacityEffect(wid)
            wid.setGraphicsEffect(effect)
            anim1 = QPropertyAnimation(effect, b"opacity")
            anim1.setDuration(150)
            anim1.setStartValue(1.0)
            anim1.setEndValue(0.2)
            anim1.setEasingCurve(QEasingCurve.OutExpo)
            anim1.finished.connect(lambda: whendone(self.ui.tableView_results))
            anim1.start()
            self.anim1 = anim1
        else:
            whendone(self.ui.tableView_results)

    def auto_del(self):
        tbl_res = self.ui.tableView_results
        if not self.dups_db_model.rowCount():
            return
        if not self.ui.tableView_results.selectedIndexes():
            return
        tbl_res.setDisabled(True)

        self.ui.listWidget_autoDelRules.setDisabled(True)

        items = self.ui.tableView_results.selectedIndexes()
        filename_1, filename_2 = str(items[0].data()), str(items[1].data())

        adr = self.ui.listWidget_autoDelRules

        try:
            for i in range(adr.count()):
                rule = adr.item(i).text()
                comp_func = min if "smaller" in rule else max

                if "dimension" in rule:
                    w, h = Image.open(filename_1).size
                    attr_1 = w * h
                    w, h = Image.open(filename_2).size
                    attr_2 = w * h
                elif "width" in rule:
                    w1, h1 = Image.open(filename_1).size
                    w2, h2 = Image.open(filename_2).size
                    attr_1, attr_2 = w1, w2
                elif "height" in rule:
                    w1, h1 = Image.open(filename_1).size
                    w2, h2 = Image.open(filename_2).size
                    attr_1, attr_2 = h1, h2
                elif "file size" in rule:
                    attr_1, attr_2 = filesize(filename_1), filesize(filename_2)
                else:
                    special = 0 if "the left" in rule else 1

                try:
                    wid = self.image_viewer2.label if special else self.image_viewer1.label
                    self.del_image(items[special], wid)
                    break
                except (IndexError, NameError):  # if 'special' is not defined
                    if attr_1 == attr_2:
                        continue
                    res = 0 if comp_func(attr_1, attr_2) == attr_1 else 1
                    wid = self.image_viewer2.label if res else self.image_viewer1.label
                    self.del_image(items[res], wid)
                    break

        except:
            QMessageBox.warning(self,
                                "Nayan - Warning",
                                "Auto-delete failed!",
                                QMessageBox.Close)

        self.ui.listWidget_autoDelRules.setEnabled(True)
        tbl_res.setEnabled(True)
        tbl_res.setFocus()

    def auto_del_all(self):
        tbl_res = self.ui.tableView_results
        if not self.dups_db_model.rowCount():
            return

        QMessageBox.question(self,
                             "Nayan - Question",
                             "Are you sure you want to apply auto-delete to all the duplicate "
                             "pairs?\n"
                             "WARNING: No deletion confirmations will be shown.")

        tbl_res.itemSelectionChanged.disconnect(self.result_table_selection_changed)
        tbl_res.setDisabled(True)
        self.ui.listWidget_autoDelRules.setDisabled(True)

        row_count = self.dups_db_model.rowCount()
        prog_dlg = QProgressDialog("Auto-deletion in progres...", "Cancel", 0, row_count, self)
        QApplication.processEvents()

        adr = self.ui.listWidget_autoDelRules
        rules = [adr.item(i).text() for i in range(adr.count())]

        db = self.dups_db_model.database()
        i = 0
        while self.dups_db_model.rowCount():
            if prog_dlg.wasCanceled() or i == row_count:
                break

            filename_1 = str(self.dups_db_model.index(i, 0).data())
            filename_2 = str(self.dups_db_model.index(i, 1).data())

            for rule in rules:
                comp_func = min if "smaller" in rule else max

                try:
                    if "dimension" in rule:
                        w, h = Image.open(filename_1).size
                        attr_1 = w * h
                        w, h = Image.open(filename_2).size
                        attr_2 = w * h
                    elif "width" in rule:
                        w1, h1 = Image.open(filename_1).size
                        w2, h2 = Image.open(filename_2).size
                        attr_1, attr_2 = w1, w2
                    elif "height" in rule:
                        w1, h1 = Image.open(filename_1).size
                        w2, h2 = Image.open(filename_2).size
                        attr_1, attr_2 = h1, h2
                    elif "file size" in rule:
                        attr_1, attr_2 = filesize(filename_1), filesize(filename_2)
                    else:
                        special = 0 if "the left" in rule else 1
                except:
                    break

                try:
                    try:
                        filename = filename_2 if special else filename_1
                        # print(filename, "pseudo-deleted")
                        send2trash(filename)
                        db.exec_("DELETE FROM dups WHERE file1='%s' OR file2='%s'" % (
                            filename, filename,))
                    except OSError:
                        QMessageBox.warning(self,
                                            "Nayan - Warning",
                                            "Failed to delete '%s'! Please check whether the file "
                                            "exists and Nayan has permission to delete it." % filename,
                                            QMessageBox.Close)
                        continue
                except NameError:  # if 'special' is not defined
                    if attr_1 == attr_2:
                        continue
                    res = 0 if comp_func(attr_1, attr_2) == attr_1 else 1
                    try:
                        filename = filename_2 if res else filename_1
                        # print(filename_2 if res else filename_1, "pseudo-deleted")
                        send2trash(filename)
                        db.exec_("DELETE FROM dups WHERE file1='%s' OR file2='%s'" % (
                            filename, filename,))
                    except OSError:
                        QMessageBox.warning(self,
                                            "Nayan - Warning",
                                            "Failed to delete '%s'! Please check whether the file "
                                            "exists and Nayan has permission to delete it." % filename,
                                            QMessageBox.Close)
                        continue
            i += 1
            prog_dlg.setValue(i)
            QApplication.processEvents()
        db.commit()
        self.dups_db_model.submitAll()
        prog_dlg.hide()
        prog_dlg.deleteLater()

        tbl_res.itemSelectionChanged.connect(self.result_table_selection_changed)
        self.result_table_selection_changed()
        self.ui.listWidget_autoDelRules.setEnabled(True)
        tbl_res.setEnabled(True)
        tbl_res.setFocus()

    def open_left_img_folder(self):
        items = self.ui.tableView_results.selectedIndexes()
        if items:
            self.open_folder(str(items[0].data()))
        self.ui.tableView_results.setFocus()

    def open_right_img_folder(self):
        items = self.ui.tableView_results.selectedIndexes()
        if items:
            self.open_folder(str(items[1].data()))
        self.ui.tableView_results.setFocus()

    def stop_everything_before_exit(self):
        if self.scanner and self.scanner.isRunning():
            print("I'm trying to clean up your mess... >(")
            self.scanner.stop()

    def set_ui_frozen(self, b):
        self.ui.tabWidget.setDisabled(b)
        self.ui.listWidget_targets.setDisabled(b)
        self.ui.pushButton_addFilesFolders.setDisabled(b)
        self.ui.pushButton_selectAll.setDisabled(b)
        self.ui.pushButton_removeSelected.setDisabled(b)

    def about(self):
        QMessageBox.about(self,
                          "About - Nayan",
                          "<html><body>"
                          "<p>Nayan  - A duplicate image finder built with Python using the "
                          "wonderful Qt framework through the PyQt5 bindings.</p><p>"
                          "Nayan is free and open source software released under the <a "
                          "href=\"https://www.gnu.org/licenses/gpl-3.0.en.html\">GNU "
                          "GPL v3.0</a>.</p>"
                          "<p>© 2016 Shravan Kaushik</p>"
                          "</body></html>")

    def toggle_theme(self):
        import qtawesome as qta
        from PyQt5.QtWidgets import qApp

        if self.ACTIVE_PALETTE:  # if dark theme is active
            QApplication.setPalette(self.LIGHT_PALETTE)
            self.ACTIVE_PALETTE = 0
            self.ui.pushButton_img1Delete.setIcon(
                qta.icon("fa.trash", color="black", color_active="#34DB8A"))
            self.ui.pushButton_img2Delete.setIcon(
                qta.icon("fa.trash", color="black", color_active="#34DB8A"))
            self.ui.pushButton_img1OpenFolder.setIcon(
                qta.icon("fa.folder-open", color="black", color_active="#34DB8A"))
            self.ui.pushButton_img2OpenFolder.setIcon(
                qta.icon("fa.folder-open", color="black", color_active="#34DB8A"))
            self.ui.pushButton_swap.setIcon(
                qta.icon("fa.exchange", color="black", color_active="#34DB8A"))
            self.ui.pushButton_up.setIcon(
                qta.icon("fa.arrow-up", color="black", color_active="#34DB8A"))
            self.ui.pushButton_down.setIcon(
                qta.icon("fa.arrow-down", color="black", color_active="#34DB8A"))
            self.ui.pushButton_rotateImg1.setIcon(
                qta.icon("fa.rotate-right", color="black", color_active="#34DB8A"))
            self.ui.pushButton_rotateImg2.setIcon(
                qta.icon("fa.rotate-right", color="black", color_active="#34DB8A"))
            self.ui.toolButton_autoDel.setIcon(
                qta.icon("fa.magic", color="black", color_active="#34DB8A"))
            self.ui.pushButton_scan.setIcon(
                qta.icon("fa.search", color="black", color_active="#34DB8A"))
            self.ui.pushButton_cancelOperation.setIcon(
                qta.icon("fa.times-circle", color="black", color_active="#34DB8A"))
        else:
            qApp.setPalette(self.DARK_PALETTE)
            self.ACTIVE_PALETTE = 1
            self.ui.pushButton_img1Delete.setIcon(
                qta.icon("fa.trash", color="white", color_active="#34DB8A"))
            self.ui.pushButton_img2Delete.setIcon(
                qta.icon("fa.trash", color="white", color_active="#34DB8A"))
            self.ui.pushButton_img1OpenFolder.setIcon(
                qta.icon("fa.folder-open", color="white", color_active="#34DB8A"))
            self.ui.pushButton_img2OpenFolder.setIcon(
                qta.icon("fa.folder-open", color="white", color_active="#34DB8A"))
            self.ui.pushButton_swap.setIcon(
                qta.icon("fa.exchange", color="white", color_active="#34DB8A"))
            self.ui.pushButton_up.setIcon(
                qta.icon("fa.arrow-up", color="white", color_active="#34DB8A"))
            self.ui.pushButton_down.setIcon(
                qta.icon("fa.arrow-down", color="white", color_active="#34DB8A"))
            self.ui.pushButton_rotateImg1.setIcon(
                qta.icon("fa.rotate-right", color="white", color_active="#34DB8A"))
            self.ui.pushButton_rotateImg2.setIcon(
                qta.icon("fa.rotate-right", color="white", color_active="#34DB8A"))
            self.ui.toolButton_autoDel.setIcon(
                qta.icon("fa.magic", color="white", color_active="#34DB8A"))
            self.ui.pushButton_scan.setIcon(
                qta.icon("fa.search", color="white", color_active="#34DB8A"))
            self.ui.pushButton_cancelOperation.setIcon(
                qta.icon("fa.times-circle", color="white", color_active="#34DB8A"))


class IntegerTableWidgetItem(QTableWidgetItem):
    def __init__(self, value):
        super(IntegerTableWidgetItem, self).__init__(str(value))

    def __lt__(self, other):
        return int(self.text()) < int(other.text())
