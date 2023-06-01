from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    VDK="abc"
    MHS=""
    MPH=""

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.Arduino = QtWidgets.QComboBox(Dialog)
        self.Arduino.setGeometry(QtCore.QRect(100, 20, 73, 22))
        self.Arduino.setObjectName("Arduino")
        self.Osi = QtWidgets.QComboBox(Dialog)
        self.Osi.setGeometry(QtCore.QRect(100, 100, 73, 22))
        self.Osi.setObjectName("Osi")
        self.Twin = QtWidgets.QComboBox(Dialog)
        self.Twin.setGeometry(QtCore.QRect(100, 170, 73, 22))
        self.Twin.setObjectName("Twin")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 20, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 170, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 100, 91, 16))
        self.label_3.setObjectName("label_3")
        f = open('myfile.txt', 'r')
        for line in range (3):
            data = f.readline()
            data=data[4:len(data)]
            i=0
            while data.find(',',i+1,len(data))!=-1:
                if line==0:
                    self.Arduino.addItem(str(data[i+1:data.find(',',i+1,len(data))]))
                elif line==1:
                    self.Osi.addItem(str(data[i+1:data.find(',',i+1,len(data))]))
                elif line==2:
                    self.Twin.addItem(str(data[i+1:data.find(',',i+1,len(data))]))
                i=data.find(',',i+1,len(data))
        f.close()
        self.Arduino.setEditable(True)
        self.Osi.setEditable(True)
        self.Twin.setEditable(True)
        self.Arduino.editTextChanged.connect(self.newArduino)
        self.Osi.editTextChanged.connect(self.newOsi)
        self.Twin.editTextChanged.connect(self.newTwin)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def newArduino(self,i):
        print(self.Arduino.count())

    def newOsi(self,i):
        print(i)

    def newTwin(self,i):
        print(i)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Vi Điều Khiển"))
        self.label_2.setText(_translate("Dialog", "Máy Phát Hàm"))
        self.label_3.setText(_translate("Dialog", "Máy Hiện Sóng"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
