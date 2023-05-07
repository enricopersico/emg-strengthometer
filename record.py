import serial, time, datetime

ser = serial.Serial("/dev/cu.usbmodem2101", 50000)
print("Connected to Arduino")


dt = str(datetime.datetime.now())
f = open(f"data/data3.txt", "a")

start = time.time()
end = time.time()
while end - start < 10:
    print(time.time()-end)
    getData=ser.readline()
    dataString = getData.decode('utf-8')
    f.write(dataString)
    end = time.time()

f.close()