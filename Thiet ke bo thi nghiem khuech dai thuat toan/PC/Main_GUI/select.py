# Form implementation generated from reading ui file 'select_com.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_selectCom(object):
    def setupUi(self, selectCom):
        selectCom.setObjectName("selectCom")
        selectCom.resize(400, 200)
        selectCom.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(selectCom)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(54, 20, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(50, 80, 302, 46))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        selectCom.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(selectCom)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 26))
        self.menubar.setObjectName("menubar")
        selectCom.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(selectCom)
        self.statusbar.setObjectName("statusbar")
        selectCom.setStatusBar(self.statusbar)
        list_com=[]
        for i in range (1,21):
            list_com.append("COM"+str(i))
        self.comboBox_2.addItems(list_com)
        self.pushButton_2.clicked.connect(self.click)
        self.retranslateUi(selectCom)
        QtCore.QMetaObject.connectSlotsByName(selectCom)


    def click(self):
        self.close()

    def retranslateUi(self, selectCom):
        _translate = QtCore.QCoreApplication.translate
        selectCom.setWindowTitle(_translate("selectCom", "MainWindow"))
        self.label_3.setText(_translate("selectCom", "Chọn cổng Com"))
        self.label_2.setText(_translate("selectCom", "Com thông thường"))
        self.pushButton_2.setText(_translate("selectCom", "Tiếp tục"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    selectCom = QtWidgets.QMainWindow()
    ui = Ui_selectCom()
    ui.setupUi(selectCom)
    selectCom.show()
    sys.exit(app.exec())
