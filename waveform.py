"""
DESCRIPTION: 
Script that prints the waveform of data file.
AUTHOR: ENRICO PERSICO
"""
import numpy as np
import matplotlib.pyplot as plt

hz = 1000 # sampling rate of data in Hz
data_file = "data/data3.txt" # name of data file

with open(data_file) as f:
    data = f.read()

data = data.split('\n')

x = []
y = []
val=0
tt = 1.0/float(hz)
for item in data:
    try:
        y.append( int(item))
        x.append(val)
        val += 0.001
    except ValueError:
        data.pop()
        break

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("ARDUINO EMG READOUT")    
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('ADC Score')

ax1.plot(x,y, c='b')

leg = ax1.legend()

plt.show()