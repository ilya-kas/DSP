from numpy import sin, pi
from random import randint
from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq
import numpy as np

B1 = 1000
B2 = 10
N = 512
COUNT = 1000

def generateSignal(n):
    y = []
    for i in range(n):
        z = B1*sin(2*pi*i/N)
        for j in range(50,71):
            z += ((-1)**randint(0, 1))*B2*sin(2*pi*j*i/N)
        y.append(z)
    return y


y = generateSignal(COUNT)

plt.subplot(221)
plt.plot(y)



yf = rfft(y)
xf = rfftfreq(COUNT)

plt.subplot(222)
plt.plot(xf, np.abs(yf))


W1 = 7
W2 = 9
F1 = []
for i in range(COUNT):
    z = y[i]
    c = 1
    for j in range(max(0, i-W1//2),i):
        z += y[j]
        c += 1
    for j in range(i+1, min(len(y), i+W1//2)):
        z += y[j]
        c += 1
    F1.append(z/c)

plt.subplot(223)
plt.plot(F1)

yf = rfft(F1)
xf = rfftfreq(COUNT)

plt.subplot(224)
plt.plot(xf, np.abs(yf))

plt.show()



F2 = [y[0], y[1], y[2]]
for i in range(3, COUNT-3):
    F2.append(1/231*(5*y[i-3] - 30*y[i-2] + 75*y[i-1] + 131*y[i] + 75*y[i+1] - 30*y[i+2] + 5*y[i+3]))
F2.append(y[-3])
F2.append(y[-2])
F2.append(y[-1])

plt.subplot(221)
plt.plot(F2)

yf = rfft(F2)
xf = rfftfreq(COUNT)

plt.subplot(222)
plt.plot(xf, np.abs(yf))



F3 = []
for i in range(COUNT):
    l = max(0, i - W2 // 2)
    r = min(len(y), i + W1 // 2)
    z = y[l:r]
    z = sorted(z)
    F3.append(z[len(z)//2])

plt.subplot(223)
plt.plot(F3)

yf = rfft(F3)
xf = rfftfreq(COUNT)

plt.subplot(224)
plt.plot(xf, np.abs(yf))

plt.show()
