"""
DESCRIPTION: 
This script reads data from the arduino for t seconds. Make sure to edit
the variables with comments at the top to configure it for one's own 
specifications.
AUTHOR: ENRICO PERSICO
"""
import serial, time, datetime

t = 10 # how many seconds of data user wishes to record
port = "/dev/cu.usbmodem2101" # port that Arduino is using
baud = 50000 # baud rate set on Arduino script

ser = serial.Serial(port, baud)
dt = str(datetime.datetime.now())
f = open(f"data/{dt}.txt", "a")

start = time.time()
end = time.time()
while end - start < t:
    print(time.time()-end)
    getData=ser.readline()
    dataString = getData.decode('utf-8')
    f.write(dataString)
    end = time.time()

f.close()