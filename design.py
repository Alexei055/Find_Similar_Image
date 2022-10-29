# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(734, 650)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.145251 rgba(255, 151, 7, 255), stop:0.586592 rgba(248, 64, 18, 255), stop:0.994413 rgba(214, 2, 62, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.folder_horizontal_layout = QHBoxLayout()
        self.folder_horizontal_layout.setObjectName(u"folder_horizontal_layout")
        self.folder_horizontal_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.folder_left_horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.folder_horizontal_layout.addItem(self.folder_left_horizontal_spacer)

        self.folder_line_edit = QLineEdit(self.centralwidget)
        self.folder_line_edit.setObjectName(u"folder_line_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folder_line_edit.sizePolicy().hasHeightForWidth())
        self.folder_line_edit.setSizePolicy(sizePolicy)
        self.folder_line_edit.setMinimumSize(QSize(400, 0))
        self.folder_line_edit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.folder_horizontal_layout.addWidget(self.folder_line_edit)

        self.open_folder_button = QPushButton(self.centralwidget)
        self.open_folder_button.setObjectName(u"open_folder_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.open_folder_button.sizePolicy().hasHeightForWidth())
        self.open_folder_button.setSizePolicy(sizePolicy1)
        self.open_folder_button.setStyleSheet(u"#open_folder_button {\n"
"	background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"border-color: back;\n"
"padding: 2px;\n"
"}\n"
"\n"
"#open_folder_button:hover {\n"
"background-color: rgba(229,241,251, 200);\n"
"transition: all 0.2s 0s ease;\n"
"}")

        self.folder_horizontal_layout.addWidget(self.open_folder_button)

        self.folder_right_horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.folder_horizontal_layout.addItem(self.folder_right_horizontal_spacer)


        self.verticalLayout.addLayout(self.folder_horizontal_layout)

        self.images_horizontal_layout = QHBoxLayout()
        self.images_horizontal_layout.setObjectName(u"images_horizontal_layout")
        self.images_horizontal_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.back_button = QPushButton(self.centralwidget)
        self.back_button.setObjectName(u"back_button")
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(200)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet(u"#back_button {\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"icon/back_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QSize(16, 509))

        self.images_horizontal_layout.addWidget(self.back_button)

        self.original = QLabel(self.centralwidget)
        self.original.setObjectName(u"original")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.original.sizePolicy().hasHeightForWidth())
        self.original.setSizePolicy(sizePolicy2)
        self.original.setStyleSheet(u"border-style: transparent;\n"
"background-color:transparent")
        self.original.setAlignment(Qt.AlignCenter)

        self.images_horizontal_layout.addWidget(self.original)

        self.original_vertical_line = QFrame(self.centralwidget)
        self.original_vertical_line.setObjectName(u"original_vertical_line")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.original_vertical_line.sizePolicy().hasHeightForWidth())
        self.original_vertical_line.setSizePolicy(sizePolicy3)
        self.original_vertical_line.setFrameShape(QFrame.VLine)
        self.original_vertical_line.setFrameShadow(QFrame.Sunken)

        self.images_horizontal_layout.addWidget(self.original_vertical_line)

        self.duble_vertical_line = QFrame(self.centralwidget)
        self.duble_vertical_line.setObjectName(u"duble_vertical_line")
        sizePolicy3.setHeightForWidth(self.duble_vertical_line.sizePolicy().hasHeightForWidth())
        self.duble_vertical_line.setSizePolicy(sizePolicy3)
        self.duble_vertical_line.setFrameShape(QFrame.VLine)
        self.duble_vertical_line.setFrameShadow(QFrame.Sunken)

        self.images_horizontal_layout.addWidget(self.duble_vertical_line)

        self.duble = QLabel(self.centralwidget)
        self.duble.setObjectName(u"duble")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.duble.sizePolicy().hasHeightForWidth())
        self.duble.setSizePolicy(sizePolicy4)
        self.duble.setStyleSheet(u"border-style: transparent;\n"
"background-color:transparent")
        self.duble.setAlignment(Qt.AlignCenter)

        self.images_horizontal_layout.addWidget(self.duble)

        self.next_button = QPushButton(self.centralwidget)
        self.next_button.setObjectName(u"next_button")
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)
        self.next_button.setStyleSheet(u"background-color:transparent\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"icon/next_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_button.setIcon(icon1)
        self.next_button.setIconSize(QSize(16, 509))

        self.images_horizontal_layout.addWidget(self.next_button)


        self.verticalLayout.addLayout(self.images_horizontal_layout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.duble_count = QLabel(self.centralwidget)
        self.duble_count.setObjectName(u"duble_count")
        self.duble_count.setStyleSheet(u"background-color:transparent;")

        self.horizontalLayout.addWidget(self.duble_count)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.controls_horizontal_layout = QHBoxLayout()
        self.controls_horizontal_layout.setObjectName(u"controls_horizontal_layout")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(50)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy5)
        self.progressBar.setMaximumSize(QSize(200, 16777215))
        self.progressBar.setBaseSize(QSize(0, 0))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)

        self.controls_horizontal_layout.addWidget(self.progressBar)

        self.controls_horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.controls_horizontal_layout.addItem(self.controls_horizontal_spacer)

        self.open_restore_window = QPushButton(self.centralwidget)
        self.open_restore_window.setObjectName(u"open_restore_window")
        self.open_restore_window.setStyleSheet(u"#open_restore_window {\n"
"	background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"border-color: back;\n"
"padding: 2px;\n"
"}\n"
"\n"
"#open_restore_window:hover {\n"
"background-color: rgba(229,241,251, 200);\n"
"transition: all 0.2s 0s ease;\n"
"}")

        self.controls_horizontal_layout.addWidget(self.open_restore_window)

        self.delete_button_2 = QPushButton(self.centralwidget)
        self.delete_button_2.setObjectName(u"delete_button_2")
        sizePolicy.setHeightForWidth(self.delete_button_2.sizePolicy().hasHeightForWidth())
        self.delete_button_2.setSizePolicy(sizePolicy)
        self.delete_button_2.setStyleSheet(u"#delete_button_2 {\n"
"	background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-radius: 3px;\n"
"border-color: back;\n"
"padding: 2px;\n"
"}\n"
"\n"
"#delete_button_2:hover {\n"
"background-color: rgba(229,241,251, 200);\n"
"transition: all 0.2s 0s ease;\n"
"}")

        self.controls_horizontal_layout.addWidget(self.delete_button_2)


        self.verticalLayout.addLayout(self.controls_horizontal_layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Поиск одинаковых изображений", None))
        self.open_folder_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443", None))
        self.back_button.setText("")
        self.original.setText("")
        self.duble.setText("")
        self.next_button.setText("")
        self.duble_count.setText("")
        self.progressBar.setFormat(QCoreApplication.translate("MainWindow", u"%p%", None))
        self.open_restore_window.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0443\u0434\u0430\u043b\u0435\u043d\u043d\u044b\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.delete_button_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

