# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 558)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.page)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_targets = QtWidgets.QWidget()
        self.tab_targets.setObjectName("tab_targets")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_targets)
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.tab_targets)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.listWidget_targets = DragDropListWidget(self.tab_targets)
        self.listWidget_targets.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.listWidget_targets.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget_targets.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.listWidget_targets.setUniformItemSizes(True)
        self.listWidget_targets.setObjectName("listWidget_targets")
        self.verticalLayout_4.addWidget(self.listWidget_targets)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_addFilesFolders = QtWidgets.QPushButton(self.tab_targets)
        self.pushButton_addFilesFolders.setObjectName("pushButton_addFilesFolders")
        self.horizontalLayout.addWidget(self.pushButton_addFilesFolders)
        self.label_no_of_items = QtWidgets.QLabel(self.tab_targets)
        self.label_no_of_items.setObjectName("label_no_of_items")
        self.horizontalLayout.addWidget(self.label_no_of_items)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_selectAll = QtWidgets.QPushButton(self.tab_targets)
        self.pushButton_selectAll.setObjectName("pushButton_selectAll")
        self.horizontalLayout.addWidget(self.pushButton_selectAll)
        self.pushButton_removeSelected = QtWidgets.QPushButton(self.tab_targets)
        self.pushButton_removeSelected.setObjectName("pushButton_removeSelected")
        self.horizontalLayout.addWidget(self.pushButton_removeSelected)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_scanOptions = QtWidgets.QGroupBox(self.tab_targets)
        self.groupBox_scanOptions.setObjectName("groupBox_scanOptions")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_scanOptions)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_scanOptions)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.spinBox_threshold = QtWidgets.QSpinBox(self.groupBox_scanOptions)
        self.spinBox_threshold.setMinimum(10)
        self.spinBox_threshold.setMaximum(100)
        self.spinBox_threshold.setProperty("value", 10)
        self.spinBox_threshold.setObjectName("spinBox_threshold")
        self.gridLayout_4.addWidget(self.spinBox_threshold, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 1, 3, 1, 1)
        self.comboBox_algorithm = QtWidgets.QComboBox(self.groupBox_scanOptions)
        self.comboBox_algorithm.setObjectName("comboBox_algorithm")
        self.comboBox_algorithm.addItem("")
        self.comboBox_algorithm.addItem("")
        self.comboBox_algorithm.addItem("")
        self.comboBox_algorithm.addItem("")
        self.comboBox_algorithm.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_algorithm, 0, 1, 1, 2)
        self.dial_threshold = QtWidgets.QDial(self.groupBox_scanOptions)
        self.dial_threshold.setMinimumSize(QtCore.QSize(50, 50))
        self.dial_threshold.setMaximumSize(QtCore.QSize(50, 50))
        self.dial_threshold.setMinimum(10)
        self.dial_threshold.setMaximum(100)
        self.dial_threshold.setProperty("value", 10)
        self.dial_threshold.setNotchesVisible(True)
        self.dial_threshold.setObjectName("dial_threshold")
        self.gridLayout_4.addWidget(self.dial_threshold, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_scanOptions)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.pushButton_resetScanOptions = QtWidgets.QPushButton(self.groupBox_scanOptions)
        self.pushButton_resetScanOptions.setObjectName("pushButton_resetScanOptions")
        self.gridLayout_4.addWidget(self.pushButton_resetScanOptions, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_scanOptions, 3, 0, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 3, 1, 1)
        self.pushButton_scan = QtWidgets.QPushButton(self.tab_targets)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_scan.setFont(font)
        self.pushButton_scan.setAutoDefault(True)
        self.pushButton_scan.setDefault(True)
        self.pushButton_scan.setObjectName("pushButton_scan")
        self.gridLayout_3.addWidget(self.pushButton_scan, 0, 1, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 0, 0, 1, 1)
        self.checkBox_showOptions = QtWidgets.QCheckBox(self.tab_targets)
        self.checkBox_showOptions.setObjectName("checkBox_showOptions")
        self.gridLayout_3.addWidget(self.checkBox_showOptions, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 2, 0, 1, 4)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.tabWidget.addTab(self.tab_targets, "")
        self.tab_results = QtWidgets.QWidget()
        self.tab_results.setObjectName("tab_results")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tab_results)
        self.verticalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.splitter = QtWidgets.QSplitter(self.tab_results)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.horizontalFrame = QtWidgets.QFrame(self.splitter)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_img1 = QtWidgets.QFrame(self.horizontalFrame)
        self.frame_img1.setObjectName("frame_img1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_img1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_img1 = QtWidgets.QGridLayout()
        self.gridLayout_img1.setObjectName("gridLayout_img1")
        self.pushButton_img1Delete = QtWidgets.QPushButton(self.frame_img1)
        self.pushButton_img1Delete.setObjectName("pushButton_img1Delete")
        self.gridLayout_img1.addWidget(self.pushButton_img1Delete, 2, 2, 1, 1)
        self.label_img1Dimension = QtWidgets.QLabel(self.frame_img1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_img1Dimension.sizePolicy().hasHeightForWidth())
        self.label_img1Dimension.setSizePolicy(sizePolicy)
        self.label_img1Dimension.setText("")
        self.label_img1Dimension.setObjectName("label_img1Dimension")
        self.gridLayout_img1.addWidget(self.label_img1Dimension, 2, 1, 1, 1)
        self.pushButton_img1OpenFolder = QtWidgets.QPushButton(self.frame_img1)
        self.pushButton_img1OpenFolder.setObjectName("pushButton_img1OpenFolder")
        self.gridLayout_img1.addWidget(self.pushButton_img1OpenFolder, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_img1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_img1.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_img1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_img1.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_img1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_img1.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_img1Name = ElidedLabel(self.frame_img1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_img1Name.sizePolicy().hasHeightForWidth())
        self.label_img1Name.setSizePolicy(sizePolicy)
        self.label_img1Name.setText("")
        self.label_img1Name.setObjectName("label_img1Name")
        self.gridLayout_img1.addWidget(self.label_img1Name, 0, 1, 1, 4)
        self.label_img1Size = QtWidgets.QLabel(self.frame_img1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_img1Size.sizePolicy().hasHeightForWidth())
        self.label_img1Size.setSizePolicy(sizePolicy)
        self.label_img1Size.setText("")
        self.label_img1Size.setObjectName("label_img1Size")
        self.gridLayout_img1.addWidget(self.label_img1Size, 1, 1, 1, 4)
        self.pushButton_rotateImg1 = QtWidgets.QPushButton(self.frame_img1)
        self.pushButton_rotateImg1.setText("")
        self.pushButton_rotateImg1.setObjectName("pushButton_rotateImg1")
        self.gridLayout_img1.addWidget(self.pushButton_rotateImg1, 2, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_img1)
        self.horizontalLayout_2.addWidget(self.frame_img1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.horizontalFrame)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.label_similarity = QtWidgets.QLabel(self.horizontalFrame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_similarity.setFont(font)
        self.label_similarity.setText("")
        self.label_similarity.setAlignment(QtCore.Qt.AlignCenter)
        self.label_similarity.setObjectName("label_similarity")
        self.verticalLayout_5.addWidget(self.label_similarity)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.pushButton_swap = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_swap.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_swap.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton_swap.setObjectName("pushButton_swap")
        self.verticalLayout_7.addWidget(self.pushButton_swap)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem6)
        self.pushButton_delBoth = QtWidgets.QPushButton(self.horizontalFrame)
        self.pushButton_delBoth.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_delBoth.setMaximumSize(QtCore.QSize(16777215, 25))
        self.pushButton_delBoth.setObjectName("pushButton_delBoth")
        self.verticalLayout_7.addWidget(self.pushButton_delBoth)
        self.toolButton_autoDel = QtWidgets.QToolButton(self.horizontalFrame)
        self.toolButton_autoDel.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.toolButton_autoDel.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_autoDel.setObjectName("toolButton_autoDel")
        self.verticalLayout_7.addWidget(self.toolButton_autoDel)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.frame_img2 = QtWidgets.QFrame(self.horizontalFrame)
        self.frame_img2.setObjectName("frame_img2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_img2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_img2 = QtWidgets.QGridLayout()
        self.gridLayout_img2.setObjectName("gridLayout_img2")
        self.label_img2Dimension = QtWidgets.QLabel(self.frame_img2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_img2Dimension.sizePolicy().hasHeightForWidth())
        self.label_img2Dimension.setSizePolicy(sizePolicy)
        self.label_img2Dimension.setText("")
        self.label_img2Dimension.setObjectName("label_img2Dimension")
        self.gridLayout_img2.addWidget(self.label_img2Dimension, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_img2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_img2.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_img2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.gridLayout_img2.addWidget(self.label_13, 0, 0, 1, 1)
        self.pushButton_img2Delete = QtWidgets.QPushButton(self.frame_img2)
        self.pushButton_img2Delete.setObjectName("pushButton_img2Delete")
        self.gridLayout_img2.addWidget(self.pushButton_img2Delete, 2, 2, 1, 1)
        self.pushButton_img2OpenFolder = QtWidgets.QPushButton(self.frame_img2)
        self.pushButton_img2OpenFolder.setObjectName("pushButton_img2OpenFolder")
        self.gridLayout_img2.addWidget(self.pushButton_img2OpenFolder, 2, 3, 1, 1)
        self.pushButton_rotateImg2 = QtWidgets.QPushButton(self.frame_img2)
        self.pushButton_rotateImg2.setText("")
        self.pushButton_rotateImg2.setObjectName("pushButton_rotateImg2")
        self.gridLayout_img2.addWidget(self.pushButton_rotateImg2, 2, 4, 1, 1)
        self.label_img2Name = ElidedLabel(self.frame_img2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_img2Name.sizePolicy().hasHeightForWidth())
        self.label_img2Name.setSizePolicy(sizePolicy)
        self.label_img2Name.setText("")
        self.label_img2Name.setObjectName("label_img2Name")
        self.gridLayout_img2.addWidget(self.label_img2Name, 0, 1, 1, 4)
        self.label_12 = QtWidgets.QLabel(self.frame_img2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.gridLayout_img2.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_img2Size = QtWidgets.QLabel(self.frame_img2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_img2Size.sizePolicy().hasHeightForWidth())
        self.label_img2Size.setSizePolicy(sizePolicy)
        self.label_img2Size.setText("")
        self.label_img2Size.setObjectName("label_img2Size")
        self.gridLayout_img2.addWidget(self.label_img2Size, 1, 1, 1, 4)
        self.verticalLayout_6.addLayout(self.gridLayout_img2)
        self.horizontalLayout_2.addWidget(self.frame_img2)
        self.tableView_results = CustomTableView(self.splitter)
        self.tableView_results.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView_results.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView_results.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView_results.setGridStyle(QtCore.Qt.NoPen)
        self.tableView_results.setSortingEnabled(True)
        self.tableView_results.setObjectName("tableView_results")
        self.tableView_results.verticalHeader().setDefaultSectionSize(23)
        self.tableView_results.verticalHeader().setMinimumSectionSize(23)
        self.verticalLayout_8.addWidget(self.splitter)
        self.tabWidget.addTab(self.tab_results, "")
        self.tab_autoDelRules = QtWidgets.QWidget()
        self.tab_autoDelRules.setObjectName("tab_autoDelRules")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_autoDelRules)
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_down = QtWidgets.QPushButton(self.tab_autoDelRules)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_down.sizePolicy().hasHeightForWidth())
        self.pushButton_down.setSizePolicy(sizePolicy)
        self.pushButton_down.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_down.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_down.setText("")
        self.pushButton_down.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_down.setObjectName("pushButton_down")
        self.gridLayout_2.addWidget(self.pushButton_down, 2, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem8, 3, 1, 1, 1)
        self.pushButton_up = QtWidgets.QPushButton(self.tab_autoDelRules)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_up.sizePolicy().hasHeightForWidth())
        self.pushButton_up.setSizePolicy(sizePolicy)
        self.pushButton_up.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_up.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_up.setText("")
        self.pushButton_up.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_up.setObjectName("pushButton_up")
        self.gridLayout_2.addWidget(self.pushButton_up, 1, 1, 1, 1)
        self.listWidget_autoDelRules = DragOrderableList(self.tab_autoDelRules)
        self.listWidget_autoDelRules.setUniformItemSizes(True)
        self.listWidget_autoDelRules.setObjectName("listWidget_autoDelRules")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_autoDelRules.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_autoDelRules.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_autoDelRules.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_autoDelRules.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_autoDelRules.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_autoDelRules.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_autoDelRules.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_autoDelRules.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_autoDelRules.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_autoDelRules.addItem(item)
        self.gridLayout_2.addWidget(self.listWidget_autoDelRules, 1, 0, 3, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_autoDelRules)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tab_autoDelRules, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar_operation = QtWidgets.QProgressBar(self.page_2)
        self.progressBar_operation.setMinimumSize(QtCore.QSize(450, 0))
        self.progressBar_operation.setMaximum(0)
        self.progressBar_operation.setProperty("value", -1)
        self.progressBar_operation.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_operation.setObjectName("progressBar_operation")
        self.gridLayout.addWidget(self.progressBar_operation, 2, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 2, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.pushButton_cancelOperation = QtWidgets.QPushButton(self.page_2)
        self.pushButton_cancelOperation.setObjectName("pushButton_cancelOperation")
        self.horizontalLayout_3.addWidget(self.pushButton_cancelOperation)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 0, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem13, 5, 1, 1, 1)
        self.label_operationLabel = QtWidgets.QLabel(self.page_2)
        self.label_operationLabel.setObjectName("label_operationLabel")
        self.gridLayout.addWidget(self.label_operationLabel, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 874, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionToggle_theme = QtWidgets.QAction(MainWindow)
        self.actionToggle_theme.setObjectName("actionToggle_theme")
        self.menuFile.addAction(self.actionToggle_theme)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.label_3.setBuddy(self.dial_threshold)
        self.label_2.setBuddy(self.comboBox_algorithm)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.dial_threshold.valueChanged['int'].connect(self.spinBox_threshold.setValue)
        self.spinBox_threshold.valueChanged['int'].connect(self.dial_threshold.setValue)
        self.checkBox_showOptions.toggled['bool'].connect(self.groupBox_scanOptions.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.listWidget_targets, self.pushButton_addFilesFolders)
        MainWindow.setTabOrder(self.pushButton_addFilesFolders, self.pushButton_selectAll)
        MainWindow.setTabOrder(self.pushButton_selectAll, self.pushButton_removeSelected)
        MainWindow.setTabOrder(self.pushButton_removeSelected, self.pushButton_scan)
        MainWindow.setTabOrder(self.pushButton_scan, self.checkBox_showOptions)
        MainWindow.setTabOrder(self.checkBox_showOptions, self.comboBox_algorithm)
        MainWindow.setTabOrder(self.comboBox_algorithm, self.dial_threshold)
        MainWindow.setTabOrder(self.dial_threshold, self.spinBox_threshold)
        MainWindow.setTabOrder(self.spinBox_threshold, self.pushButton_resetScanOptions)
        MainWindow.setTabOrder(self.pushButton_resetScanOptions, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.pushButton_swap)
        MainWindow.setTabOrder(self.pushButton_swap, self.pushButton_delBoth)
        MainWindow.setTabOrder(self.pushButton_delBoth, self.toolButton_autoDel)
        MainWindow.setTabOrder(self.toolButton_autoDel, self.pushButton_img1Delete)
        MainWindow.setTabOrder(self.pushButton_img1Delete, self.pushButton_img1OpenFolder)
        MainWindow.setTabOrder(self.pushButton_img1OpenFolder, self.pushButton_rotateImg1)
        MainWindow.setTabOrder(self.pushButton_rotateImg1, self.pushButton_img2Delete)
        MainWindow.setTabOrder(self.pushButton_img2Delete, self.pushButton_img2OpenFolder)
        MainWindow.setTabOrder(self.pushButton_img2OpenFolder, self.pushButton_rotateImg2)
        MainWindow.setTabOrder(self.pushButton_rotateImg2, self.tableView_results)
        MainWindow.setTabOrder(self.tableView_results, self.listWidget_autoDelRules)
        MainWindow.setTabOrder(self.listWidget_autoDelRules, self.pushButton_up)
        MainWindow.setTabOrder(self.pushButton_up, self.pushButton_down)
        MainWindow.setTabOrder(self.pushButton_down, self.pushButton_cancelOperation)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_8.setText(_translate("MainWindow", "Drag and drop files/folders into the box below..."))
        self.pushButton_addFilesFolders.setText(_translate("MainWindow", "Add fil&es/folders..."))
        self.label_no_of_items.setText(_translate("MainWindow", "Number of files: 0"))
        self.pushButton_selectAll.setText(_translate("MainWindow", "Select all"))
        self.pushButton_removeSelected.setText(_translate("MainWindow", "Remove selected"))
        self.groupBox_scanOptions.setTitle(_translate("MainWindow", "Scan options"))
        self.label_3.setText(_translate("MainWindow", "Match &threshold"))
        self.comboBox_algorithm.setItemText(0, _translate("MainWindow", "dHash"))
        self.comboBox_algorithm.setItemText(1, _translate("MainWindow", "pHash"))
        self.comboBox_algorithm.setItemText(2, _translate("MainWindow", "pHash-simple"))
        self.comboBox_algorithm.setItemText(3, _translate("MainWindow", "aHash"))
        self.comboBox_algorithm.setItemText(4, _translate("MainWindow", "wHash"))
        self.label_2.setText(_translate("MainWindow", "Dete&ction method"))
        self.pushButton_resetScanOptions.setText(_translate("MainWindow", "Reset to defaults"))
        self.pushButton_scan.setText(_translate("MainWindow", " &Scan"))
        self.checkBox_showOptions.setText(_translate("MainWindow", "Sho&w options"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_targets), _translate("MainWindow", "Scan targets"))
        self.pushButton_img1Delete.setToolTip(_translate("MainWindow", "Send the file to the recycle bin"))
        self.pushButton_img1Delete.setText(_translate("MainWindow", "Recycle (Z)"))
        self.pushButton_img1Delete.setShortcut(_translate("MainWindow", "Z"))
        self.pushButton_img1OpenFolder.setToolTip(_translate("MainWindow", "Open the folder that contains the image"))
        self.pushButton_img1OpenFolder.setText(_translate("MainWindow", "Open folder"))
        self.label_5.setText(_translate("MainWindow", "Size:"))
        self.label_7.setText(_translate("MainWindow", "Name:"))
        self.label_4.setText(_translate("MainWindow", "Dimension:"))
        self.pushButton_rotateImg1.setToolTip(_translate("MainWindow", "Rotate right"))
        self.label.setText(_translate("MainWindow", "Similarity"))
        self.pushButton_swap.setToolTip(_translate("MainWindow", "Swap the image on the left with the right one"))
        self.pushButton_swap.setText(_translate("MainWindow", " S&wap"))
        self.pushButton_delBoth.setText(_translate("MainWindow", "&Delete both"))
        self.toolButton_autoDel.setText(_translate("MainWindow", "Auto-delete (A)"))
        self.toolButton_autoDel.setShortcut(_translate("MainWindow", "A"))
        self.label_11.setText(_translate("MainWindow", "Dimension:"))
        self.label_13.setText(_translate("MainWindow", "Name:"))
        self.pushButton_img2Delete.setToolTip(_translate("MainWindow", "Send the file to the recycle bin"))
        self.pushButton_img2Delete.setText(_translate("MainWindow", "Recycle (M)"))
        self.pushButton_img2Delete.setShortcut(_translate("MainWindow", "M"))
        self.pushButton_img2OpenFolder.setToolTip(_translate("MainWindow", "Open the folder that contains the image"))
        self.pushButton_img2OpenFolder.setText(_translate("MainWindow", "Open folder"))
        self.pushButton_rotateImg2.setToolTip(_translate("MainWindow", "Rotate right"))
        self.label_12.setText(_translate("MainWindow", "Size:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_results), _translate("MainWindow", "Results"))
        __sortingEnabled = self.listWidget_autoDelRules.isSortingEnabled()
        self.listWidget_autoDelRules.setSortingEnabled(False)
        item = self.listWidget_autoDelRules.item(0)
        item.setText(_translate("MainWindow", "Image with smaller width"))
        item = self.listWidget_autoDelRules.item(1)
        item.setText(_translate("MainWindow", "Image with smaller height"))
        item = self.listWidget_autoDelRules.item(2)
        item.setText(_translate("MainWindow", "Image with smaller dimension (width x height)"))
        item = self.listWidget_autoDelRules.item(3)
        item.setText(_translate("MainWindow", "Image with smaller file size"))
        item = self.listWidget_autoDelRules.item(4)
        item.setText(_translate("MainWindow", "Image with larger width"))
        item = self.listWidget_autoDelRules.item(5)
        item.setText(_translate("MainWindow", "Image with larger height"))
        item = self.listWidget_autoDelRules.item(6)
        item.setText(_translate("MainWindow", "Image with larger file size"))
        item = self.listWidget_autoDelRules.item(7)
        item.setText(_translate("MainWindow", "Image with larger dimension (width x height)"))
        item = self.listWidget_autoDelRules.item(8)
        item.setText(_translate("MainWindow", "Image on the left"))
        item = self.listWidget_autoDelRules.item(9)
        item.setText(_translate("MainWindow", "Image on the right"))
        self.listWidget_autoDelRules.setSortingEnabled(__sortingEnabled)
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Auto-deletion is based on the following rules. The rules will be attempted in the order in which they are arranged. If a rule fails, the next one will be tried.</span></p><p>Drag the elements to reorder the list (or use the buttons)</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_autoDelRules), _translate("MainWindow", "Auto-delete Rules"))
        self.pushButton_cancelOperation.setText(_translate("MainWindow", "&Cancel"))
        self.label_operationLabel.setText(_translate("MainWindow", "Analyzing images..."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "E&xit"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionToggle_theme.setText(_translate("MainWindow", "&Toggle theme"))

from customtableview import CustomTableView
from dragdroplistwidget import DragDropListWidget
from dragorderablelist import DragOrderableList
from elidedlabel import ElidedLabel
