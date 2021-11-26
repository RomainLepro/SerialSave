#!/usr/bin/env python3
import serial
from time import *


if __name__ == '__main__':
    
    import serial.tools.list_ports as port_list
    
    
    f = open("serialSave.txt", "a")
    f.write("#"+str(time())+"\n")
    
    ports = list(port_list.comports())
    for p in ports:
        print (p)
    print(ports[0][0])
    try:
        #for ubuntu
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    except:
        #for windows
        ser = serial.Serial(ports[0][0], 9600, timeout=1)
        
    ser.reset_input_buffer()
    
    ser.write("start")
    
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            f.write(line)
            print(line)
