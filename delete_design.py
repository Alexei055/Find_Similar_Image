# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'delete.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_DeleteWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(509, 520)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"#centralwidget {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.145251 rgba(255, 151, 7, 255), stop:0.586592 rgba(248, 64, 18, 255), stop:0.994413 rgba(214, 2, 62, 255));\n"
"}\n"
"\n"
"QLabel, QListView, QWidget, QMainWindow {\n"
"	background-color:transparent;\n"
"    background-attachment: scroll;\n"
"	border-style: transparent;\n"
"}\n"
"QScrollArea {\n"
"background-color:transparent;\n"
"border-style: transparent;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(229,241,251, 200) !important;\n"
"transition: all 0.2s 0s ease !important;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: rgb(225, 225, 225) !important;\n"
"border-style: solid !important;\n"
"border-width: 1px !important;\n"
"border-radius: 3px !important;\n"
"border-color: back !important;\n"
"padding: 2px !important;\n"
"}\n"
"\n"
"QHBoxLayout {\n"
"border-style: transparent;\n"
"background-color:transparent\n"
"}\n"
"\n"
"#controls_horizontal_layout_7 {\n"
"border-style: transparent;\n"
"back"
                        "ground-color:transparent\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.sizePolicy1.setHorizontalStretch(0)
        self.sizePolicy1.setVerticalStretch(0)
        self.sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(self.sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(49)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setMinimumSize(QSize(491, 0))
        self.scrollArea.setMaximumSize(QSize(491, 16777215))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 470, 300))
        self.sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(self.sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")


        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Удаленные изображения", None))

    # retranslateUi

