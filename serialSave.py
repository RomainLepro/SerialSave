#!/usr/bin/env python3
import serial
import time
from time import *

import os

def main():

    i = 0
    
    import serial.tools.list_ports as port_list
    
    
    f = open("serialSave.txt", "a")
    f.write("\n#"+str(time())+"\n")
    f.close()
    #header of each log
    
    ports = list(port_list.comports())
    for p in ports:
        print (p)
    print(ports[0][0])
    try:
        #for ubuntu
        ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
        path = "/home/pi/Desktop/imageDetection/SerialSave/Save"
    except:
        #for windows
        ser = serial.Serial(ports[0][0], 115200, timeout=1)
        path = "./Save"
        
    ser.reset_input_buffer()
    print("input buffer initiated")
    paths, dirs, files = next(os.walk(path))
    print(path)
    print(files)
    FileName = "serialSave" + str(len(files)) +".txt"
    print(FileName)
    f = open(os.path.join(path,FileName),"w")
    f.close()
    print("file created")
    #ser.write("start")
    try:
        print("trying")
        while True:
            i+=1
            sleep(0.1)
            if ser.in_waiting > 0:
                f = open(os.path.join(path,FileName),"a")
                line = ser.readline().decode('utf-8').rstrip()
                f.write(line+"\n")
                print(line)
                #close and reopen each time u write data 
                f.close()
    except:
        print("except")
        f = open("serialSave.txt","a")
        f.write("\nan error occured, closing log file (usb deconected ?)\n")
        f.close()

main()
