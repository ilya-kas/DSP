from numpy import exp, pi, arange, concatenate, sin
from matplotlib import pyplot as plt

def FFT(x):
    N = len(x)

    if N == 1:
        return x
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = exp(-2j * pi * arange(N) / N)

        X = concatenate([X_even + factor[:int(N / 2)] * X_odd,
                        X_even + factor[int(N / 2):] * X_odd])
        return X

# sampling rate
N = 128
# sampling interval
ts = 1.0 / N
t = arange(0,1,ts)

freq = 1
x = 3*sin(2*pi*freq*t)

freq = 4
x += sin(2*pi*freq*t)

freq = 7
x += 0.5*sin(2*pi*freq*t)

plt.subplot(121)
plt.plot(t, x)
plt.ylabel('f(x)')

X=FFT(x)

# calculate the frequency
lX = len(X)
n = arange(lX)
T = lX / N
freq = n/T

plt.subplot(122)
plt.stem(freq[:50], abs(X)[:50])
plt.xlabel('Freq')
plt.ylabel('Amplitude')

plt.show()