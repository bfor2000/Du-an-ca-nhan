import serial.tools.list_ports
import serial

Drive=["USB Serial Device","SDS1052DL","33509B"]
Com=['None' for _ in range (0,3)]

def lay_ports():
    ports = serial.tools.list_ports.comports() 
    return ports

def find_Com(portsFound,Drive):
    global Com
    numConnection = len(portsFound)
    for i in range(0,numConnection):
        port = portsFound[i]
        strPort = str(port)
        print(strPort)
        for j in range(0,3):
            if Drive[j] in strPort: 
                splitPort = strPort.split(' ')
                Com[j] = (splitPort[0])

while True:
    print(serial.tools.list_ports.comports())

