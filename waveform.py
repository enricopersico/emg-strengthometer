import numpy as np
import matplotlib.pyplot as plt


txt = "data/data3.txt"
hz = 1000

with open(txt) as f:
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
        val+=0.001
    except ValueError:
        data.pop()
        break

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Plot title")    
ax1.set_xlabel('x label')
ax1.set_ylabel('y label')

ax1.plot(x,y, c='r', label='the data')

leg = ax1.legend()

plt.show()