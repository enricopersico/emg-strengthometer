from numpy.fft import fft
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read("analog-data.txt", header=None, sep="\n")
x = data.loc[:, 0]
X = fft(x)

# sampling rate
sr = 100
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

plt.stem(freq, np.abs(X), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.xlim(0, sr)
plt.show()