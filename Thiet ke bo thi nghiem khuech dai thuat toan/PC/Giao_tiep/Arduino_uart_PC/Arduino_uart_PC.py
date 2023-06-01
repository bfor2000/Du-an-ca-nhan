import serial
import time
ser=serial.Serial("COM4")
while True:
    if ser.in_waiting:
        s = ser.readline()
        data = s.decode()			
        data = data.rstrip()
        print("read data")	
        ser.write("send data".encode()) 
        ser.flush()
        print("send data")
    print(ser.in_waiting)