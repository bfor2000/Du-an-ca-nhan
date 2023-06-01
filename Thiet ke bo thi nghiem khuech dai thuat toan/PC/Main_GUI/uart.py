'''
import serial
import time
Ch1=[]
ser=serial.Serial("COM4",baudrate = 19200, parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
while True:
    ser.write("test".encode()) 
    ser.flush()
    s = ser.readline()
    data = s.decode()			# decode s
    data = data.rstrip()			# cut "\r\n" at last of string
    if(len(data)!=0):
        print(data[4:data.find(' ')])
        #Ch1.append(data[4:data.find(' ')])
        print(data[data.find(' ')+5:data.find(' ',data.find(' ')+1)])
        print(data[data.find(' ',data.find(' ')+1)+7:len(data)-1])
        '''

print(100/1000)