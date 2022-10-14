import matplotlib.pyplot as plt
from math import pi, sin

N = 512

A = [[5, 6, 0.2], [-6, -5, 0.1], [10, 12, 0.3]]
V = [[10, 12, 0.1], [5, 6, 0.3], [15, 16, 0.2]]
PH = [[2*pi, 2.2*pi, pi/8], [-1.1*pi, -pi, pi/6], [pi, 1.2*pi, pi/8]]
X = []
Y = []


def f(x, a, v, ph):
    res = 0
    for i in range(3):
        res += round(a[i] * sin(2 * pi * v[i] * x / N + ph[i]), 3)
    return res


a = [A[i][0] for i in range(3)]
v = [V[i][0] for i in range(3)]
ph = [PH[i][0] for i in range(3)]
for x in range(-100, 100, 10):
    X.append(x)
    Y.append(f(x, a, v, ph))
    for i in range(3):
        a[i] += A[i][2]
        if a[i] > A[i][1]:
            a[i] = A[i][0]
        v[i] += V[i][2]
        if v[i] > V[i][1]:
            v[i] = V[i][0]
        ph[i] += PH[i][2]
        if ph[i] > PH[i][1]:
            ph[i] = PH[i][0]

for i in range(len(X)):
    plt.plot(X, Y)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.show()
