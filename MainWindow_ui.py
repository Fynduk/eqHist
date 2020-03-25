# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1400, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.inputImage_label = QLabel(self.centralwidget)
        self.inputImage_label.setObjectName(u"outputImage_label")
        self.inputImage_label.setMaximumWidth(640)
        self.inputImage_label.setMaximumHeight(480)

        self.horizontalLayout.addWidget(self.inputImage_label)

        self.outputImage_label = QLabel(self.centralwidget)
        self.outputImage_label.setObjectName(u"inputImage_label")
        self.outputImage_label.setMaximumWidth(640)
        self.outputImage_label.setMaximumHeight(480)

        self.horizontalLayout.addWidget(self.outputImage_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.openFile_button = QPushButton(self.centralwidget)
        self.openFile_button.setObjectName(u"openFile_button")
        self.openFile_button.setMaximumSize(QSize(100, 23))

        self.horizontalLayout_2.addWidget(self.openFile_button)

        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMaximumSize(QSize(100, 23))

        self.horizontalLayout_2.addWidget(self.start_button)

        self.console_textBrowser = QTextBrowser(self.centralwidget)
        self.console_textBrowser.setObjectName(u"console_textBrowser")
        self.console_textBrowser.setMaximumSize(QSize(200, 200))

        self.horizontalLayout_2.addWidget(self.console_textBrowser)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.inputImage_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.outputImage_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.openFile_button.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

