from PyQt6.QtWidgets import QApplication, QMainWindow,QDialog
from PyQt6 import uic
import sys
#from PyQt6 import QtCore, QtGui, QtWidgets
from random import randint
from PySide6.QtCore import QTimer
import pyqtgraph as pg
import serial.tools.list_ports
import serial
TaiKhoan=""
Password=""
Mode=0
Drive_Arduino="USB Serial Device"
Com_Arduino=""
Com_Osi=""
Com_Twin=""
Drive_Osi="SDS1052DL"
Drive_Twin="33509B"
def lay_ports():
    ports = serial.tools.list_ports.comports() 
    return ports

def find_Com(portsFound,Drive):
    commPort = 'None'
    numConnection = len(portsFound)
    for i in range(0,numConnection):
        port = portsFound[i]
        strPort = str(port)
        if Drive in strPort: 
            splitPort = strPort.split(' ')
            commPort = (splitPort[0])
    return commPort

class Ui(QMainWindow):
    HCh1=2
    HCh2=2
    ZCh1=1
    ZCh2=1
    PCh1=0
    PCh2=0
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        #self.CH1.setChecked(True)
        #self.CH2.setChecked(True)
        self.bieudo.scene().sigMouseClicked.connect(self.mousePressEvent)
        self.CH1.stateChanged.connect(self.stateCh1)
        self.CH2.stateChanged.connect(self.stateCh2)
        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,100) for _ in range(100)]  # 100 data points
        self.bieudo.setTitle("Biểu đồ điện áp theo thời gian",color="r", size="30pt")
        pen = pg.mkPen(color=(255, 0, 0))
        self.bieudo.setLabel('left', 'Vertical Values',pen='b',left=False)
        self.bieudo.setLabel('bottom', 'Vertical Values',pen='b',left=False)
        self.bieudo.showAxes((True,False,False,False), True)
        self.bieudo.showLabel('bottom', show=True)
        self.data_line1=self.bieudo.plot(pen=pen, name ='blue')
        self.data_line2=self.bieudo.plot(pen='b',name='Red')
        self.bieudo.setBackground("white")
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
        self.comboMach.currentIndexChanged.connect(self.changed_mach)
        self.PositionCh1.setSuffix("mV")
        self.PositionCh2.setSuffix("mV")
        self.ZoomCh1.setSuffix("x")
        self.ZoomCh2.setSuffix("x")
        self.PositionCh1.valueChanged.connect(self.setPosCh1)
        self.PositionCh2.valueChanged.connect(self.setPosCh2)
        self.ZoomCh1.valueChanged.connect(self.setZoomCh1)
        self.ZoomCh2.valueChanged.connect(self.setZoomCh2)
        self.Setting.clicked.connect(self.onSetting)
        self.Pause.clicked.connect(self.onPause)
        self.Status_Arduino.setVisible(False)
        self.Status_Osi.setVisible(False)
        self.Status_Twin.setVisible(False)
        #self.data_line1.setCurveClickable(state=True)
        self.vLine = pg.InfiniteLine(angle=90, movable=False)
        self.hLine = pg.InfiniteLine(angle=0, movable=False)
        self.show()

    def mousePressEvent(self, event):
        #x_y = event.pos()
        pos=event
        print(event)
        '''
        if self.bieudo.sceneBoundingRect().contains(pos):
            mousePoint = self.bieudo.plotItem.vb.mapSceneToView(pos)
            self.x = int(mousePoint.x())
            self.y = int(mousePoint.y())
            print(self.x)
            print(self.y)
        '''
    def onPause(self):
        self.HCh1=1
        self.HCh2=1

    def onSetting(self):
        dlg = EmployeeDlg(self)
        dlg.exec()

    def setPosCh1(self, i):
        self.PCh1=i
        print(self.PCh1)

    def setPosCh2(self, i):
        self.PCh2=i
        print(i)

    def setZoomCh1(self, i):
        self.ZCh1=i
        print(i)

    def setZoomCh2(self, i):
        self.ZCh2=i
        print(i)

    def stateCh1(self,s):
        self.HCh1=s
        print(s)

    def stateCh2(self,s):
        self.HCh2=s
        print(s)

    def changed_mach(self,index):
        print(index)
        self.comboInput.clear()
        if index==0:
            self.comboInput.addItem("TP1.1")
        elif index==1:
            self.comboInput.addItem("TP2.1")
        elif index==2:
            self.comboInput.addItems(["TP3.1","TP3.2","TP3.1, TP3.2"])
        elif index==3:
            self.comboInput.addItems(["TP4.1","TP4.2","TP4.1, TP4.2"])
        elif index==4:
            self.comboInput.addItem("TP5.1")
        self.comboInput.addItem("No")
        print(Com_Arduino)
        if Com_Arduino !="None":
            try:
                ser=serial.Serial(Com_Arduino)
                ser.write('test'.encode()) 
                ser.flush()
                ser.close()
            except Exception:
                print("Error")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CH1"))
        self.label_2.setText(_translate("MainWindow", "CH2"))
        self.comboMode.setItemText(0, _translate("MainWindow", "Host"))
        self.comboMode.setItemText(1, _translate("MainWindow", "Online"))
        self.comboMode.setItemText(2, _translate("MainWindow", "Offline"))
        self.comboMach.setItemText(0, _translate("MainWindow", "Mạch1"))
        self.comboMach.setItemText(1, _translate("MainWindow", "Mạch2"))
        self.comboMach.setItemText(2, _translate("MainWindow", "Mạch3"))
        self.comboMach.setItemText(3, _translate("MainWindow", "Mạch4"))
        self.comboMach.setItemText(4, _translate("MainWindow", "Mạch5"))
        self.comboMach.setItemText(5, _translate("MainWindow", "Mạch6"))
        self.comboInput.setItemText(0, _translate("MainWindow", "TP1.1"))
        self.comboInput.setItemText(1, _translate("MainWindow", "No"))

    def update_plot_data(self):
        global Com_Arduino,Com_Osi,Com_Twin
        Com=find_Com(lay_ports(),Drive_Arduino) 
        if Com!='None':
            self.Status_Arduino.setVisible(False)
            Com_Arduino=Com
        else :
            self.Status_Arduino.setVisible(True)
            self.Status_Arduino.setText("Không có cổng Com "+Drive_Arduino)
            Com_Arduino="None"

        Com=find_Com(lay_ports(),Drive_Osi)
        if  Com!='None':
            self.Status_Osi.setVisible(False)
            Com_Osi=Com
        else :
            self.Status_Osi.setVisible(True)
            self.Status_Osi.setText("Không có cổng Com "+Drive_Osi)
            Com_Osi="None"
        Com=find_Com(lay_ports(),Drive_Twin)
        if  Com!='None':
            self.Status_Twin.setVisible(False)
            Com_Twin=Com
        else :
            self.Status_Twin.setVisible(True)
            self.Status_Twin.setText("Không có cổng Com "+Drive_Twin)
            Com_Twin="None"

        #self.x = self.x[1:]  # Remove the first y element.
        #self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
        self.y = self.y[1:]  # Remove the first
        self.y.append(randint(0,100))  # Add a new random value.
        self.list_y=[0 for _ in range(100)]
        for i in range(len(self.y)):
            self.list_y[i]=self.ZCh1*int(self.y[i])+self.PCh1
        ######
        if self.HCh1==2:
            self.data_line1.setData(self.x,self.list_y)
        elif self.HCh1==0:
            self.data_line1.clear()
            self.HCh1=1

            ########
        for i in range(len(self.y)):
            self.list_y[i]=self.ZCh2*int(self.y[i])+self.PCh2
            #######
        if self.HCh2==2:
            self.data_line2.setData(self.x, self.list_y)  # Update the data.
        elif self.HCh2==0:
            self.data_line2.clear()
            self.HCh2=1

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

class EmployeeDlg(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Load the dialog's GUI
        uic.loadUi("dialog.ui", self)
        f = open('myfile.txt', 'r')
        for line in range (3):
            data = f.readline()
            data=data[4:len(data)]
            i=0
            while data.find(',',i+1,len(data))!=-1:
                if line==0:
                    self.Arduino.setCurrentText(Drive_Arduino)
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

    def newArduino(self,i):
        COM_Arrduino=str(i)
        print(COM_Arrduino)
        

    def newOsi(self,i):
        print(i)

    def newTwin(self,i):
        print(i)

app = QApplication(sys.argv)
window = Ui()
app.exec() # app.exec_() in PyQt5 #