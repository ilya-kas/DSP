from math import sin, pi, sqrt
import matplotlib.pyplot as plt
import numpy as np

N = 512
K = 3 * N // 4
ph = pi / 4


def f(x):
    return round(sin(2 * pi * x / N), 3)


def findXA(M):
    usum = 0
    for i in range(M):
        usum += (f(i) ** 2)
    return sqrt(1 / (M + 1) * usum)


def findXB(M):
    sumA = 0
    sumB = 0
    for i in range(M):
        z = f(i)
        sumA += (z ** 2)
        sumB += z
    return sqrt(1 / (M + 1) * sumA - (1 / (M + 1) * sumB) ** 2)


def findA(M):
    y = [f(i) for i in range(M)]
    fft = np.fft.fft(y)
    amplitudes = 2 / M * np.abs(fft)
    return max(amplitudes)


X = []
Y = [[], [], []]
for M in range(K, 2 * N):
    xa = findXA(M)
    xb = findXB(M)
    a = findA(M)
    da = 0.707 - xa
    db = 0.707 - xb
    delA = 1 - a
    print("-----------")
    print(f"deltaX a: {xa}")
    print(f"deltaX b: {xb}")
    print(f"A: {a}")
    print(f"delta mid a: {da}")
    print(f"delta mid b: {db}")
    print(f"delta A: {delA}")
    X.append(M)
    Y[0].append(da)
    Y[1].append(db)
    Y[2].append(delA)


plt.plot(X, Y[0], label='delta by 1')
plt.plot(X, Y[1], label='delta by 2')
plt.plot(X, Y[2], label='delta A')
plt.legend()
plt.xlabel('M')
plt.ylabel('Погрешность')
plt.show()
