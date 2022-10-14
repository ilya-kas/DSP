import matplotlib.pyplot as plt
from math import pi, sin

N = 512

A = [3, 3, 3, 3, 3]
V = [1, 2, 3, 4, 5]
PH = [pi / 4, 3 * pi / 4, 2 * pi / 3, pi / 2, pi / 3]
X = []
Y = []


def f(x):
    res = 0
    for i in range(5):
        res += round(A[i] * sin(2 * pi * V[i] * x / N + PH[i]), 3)
    return res


for x in range(-1000, 1000, 10):
    X.append(x)
    Y.append(f(x))

for i in range(len(X)):
    plt.plot(X, Y)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.show()
