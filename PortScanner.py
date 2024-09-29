import sys
import time
import socket
from datetime import datetime

def menu():
    print("Port Scanner..")
    print("[1] All Ports")
    print("[2] Specific Ports")
    print("[3] Exit")

    while True:
        selection = input()
        if selection == "1":
            target = input("Please Input Target IP Address: ")
            portScan(target, 1, 65535)
        elif selection == "2":
            rangePorts()
        elif selection == "3":
            print("Exiting. . .")
            sys.exit()
        else:
            print("Please Enter a Valid Choice.")

def portScan(target, low, high):
    print("Scan Started at", str(datetime.now()))
    startTime = time.time()
    print("Scanning Now. . .")
    try:
        for port in range(low, high):
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          socket.setdefaulttimeout(1)

          # returns an error indicator
          result = s.connect_ex((target, port))
          if result == 0:
              print("Port {} is open".format(port))
          s.close()

    except socket.error:
        print("\ Server is Not Responding!")
        input()
        sys.exit()

    print("Scan Complete!")
    timeComplete = time.time()-startTime[3:]
    print("Completed in ", str(timeComplete), " seconds.")
    menu()

def rangePorts():
    target = input("Please Input Target IP Address: ")
    low = int(input("Input Lower Bound: "))
    high = int(input("Input Higher Bound: "))
    portScan(target, low, high)
menu()
