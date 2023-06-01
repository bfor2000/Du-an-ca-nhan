# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_com.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_selectCom(object):
    def setupUi(self, selectCom):
        if not selectCom.objectName():
            selectCom.setObjectName(u"selectCom")
        selectCom.resize(400, 200)
        selectCom.setStyleSheet(u"")
        self.centralwidget = QWidget(selectCom)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(54, 20, 301, 41))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(15)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(50, 80, 302, 46))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(self.widget_2)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_2.addWidget(self.comboBox_2)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        selectCom.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(selectCom)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 26))
        selectCom.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(selectCom)
        self.statusbar.setObjectName(u"statusbar")
        selectCom.setStatusBar(self.statusbar)

        self.retranslateUi(selectCom)

        QMetaObject.connectSlotsByName(selectCom)
    # setupUi

    def retranslateUi(self, selectCom):
        selectCom.setWindowTitle(QCoreApplication.translate("selectCom", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("selectCom", u"Ch\u1ecdn c\u1ed5ng Com", None))
        self.label_2.setText(QCoreApplication.translate("selectCom", u"Com th\u00f4ng th\u01b0\u1eddng", None))
        self.pushButton_2.setText(QCoreApplication.translate("selectCom", u"Ti\u1ebfo t\u1ee5c", None))
    # retranslateUi

