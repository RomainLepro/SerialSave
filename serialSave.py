#!/usr/bin/env python3
import serial
import time
from time import *



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
    except:
        #for windows
        ser = serial.Serial(ports[0][0], 115200, timeout=1)    
    ser.reset_input_buffer()
    
    sleep(1000)
    
    #ser.write("start")
    try:
        while True:
            i+=1
            sleep(0.1)
            if ser.in_waiting > 0:
                f = open("serialSave.txt","a")
                line = ser.readline().decode('utf-8').rstrip()
                f.write(line+"\n")
                print(line)
                #close and reopen each time u write data 
                f.close()
    except:
        f = open("serialSave.txt","a")
        f.write("\nan error occured, closing log file (usb deconected ?)\n")
        f.close()

main()
