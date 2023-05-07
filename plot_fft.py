"""
DESCRIPTION: 
Script that prints fft of data file.
AUTHOR: ENRICO PERSICO
"""
from numpy.fft import fft
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sr = 1000 # sampling rate of data in Hz
data_file = "data/data3.txt" # name of data file

data = pd.read_csv(data_file, header=None)
x = data.loc[:, 0]
X = fft(x)

# sampling interval
ts = 1.0/sr
t = np.arange(0,1,ts)
N = len(X)
n = np.arange(N)
T = N/sr
freq = n/T
print(freq)

plt.figure(figsize = (12, 6))
plt.subplot(121)

plt.stem(freq, np.abs(X), 'r', \
         markerfmt="-r", basefmt="-r")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.xlim(0, sr)
plt.ylim(0, 10000)
plt.show()