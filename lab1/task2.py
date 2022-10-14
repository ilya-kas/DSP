import matplotlib.pyplot as plt
from math import pi, sin

N = 512
#a
X = []
Y = []

def f(x, a, v, ph):
    return round(a * sin(2 * pi * v * x / N + ph), 3)


for ph in [pi / 6, pi / 3, 2 * pi / 3, pi / 4, 0]:
    X.append([])
    Y.append([])
    for x in range(-100, 100, 1):
        X[-1].append(x)
        Y[-1].append(f(x, 8, 4, ph))

for i in range(len(X)):
    plt.plot(X[i], Y[i], label=i)
plt.legend()
plt.xlabel('n')
plt.ylabel('x(n)')
plt.show()

#b
X = []
Y = []

for v in [8,1,5,4,9]:
    X.append([])
    Y.append([])
    for x in range(-100, 100, 1):
        X[-1].append(x)
        Y[-1].append(f(x, 4, v, 0))

for i in range(len(X)):
    plt.plot(X[i], Y[i], label=i)
plt.legend()
plt.xlabel('n')
plt.ylabel('x(n)')
plt.show()

#c
X = []
Y = []

for a in [8,3,2,1,4]:
    X.append([])
    Y.append([])
    for x in range(-100, 100, 1):
        X[-1].append(x)
        Y[-1].append(f(x, a, 2, 0))

for i in range(len(X)):
    plt.plot(X[i], Y[i], label=i)
plt.legend()
plt.xlabel('n')
plt.ylabel('x(n)')
plt.show()
