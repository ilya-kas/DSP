from matplotlib import pyplot as plt
from numpy import cos, pi, sin, sqrt, arctan

N = 100


def calcAcj(x, j):
    res = 0
    N = len(x)
    for i in range(N):
        res += x[i] * cos(2 * pi * j * i / N)
    return 2 / N * res


def calcAsj(x, j):
    res = 0
    N = len(x)
    for i in range(N):
        res += x[i] * sin(2 * pi * j * i / N)
    return 2 / N * res


def calcAj(x, j):
    return sqrt(calcAsj(x, j) ** 2 + calcAcj(x, j) ** 2)


def calcPh(x, j):
    return arctan(calcAsj(x, j) / calcAcj(x, j))


def calcBack(x):
    A = [calcAj(x, j) for j in range(N//2)]
    PH = [calcPh(x,j) for j in range(N//2)]
    res = []
    for i in range(len(x)):
        z = 0
        for j in range(N//2):
            z += A[j]*cos(2*pi*j*i/N - PH[j])
        res.append(z)
    return res


def generateSignal(n):
    x = []
    for i in range(n):
        x.append(20*cos(2*pi*10*i/n))
    return x


x = generateSignal(N)
X = []
Y = []
for i in range(100):
    X.append(i)
    Y.append(x[i])

plt.subplot(2,2,1)
plt.plot(X, Y)
plt.xlabel('i')
plt.ylabel('f(i)')

X = []
Y = []
for i in range(N//2):
    X.append(i)
    Y.append(calcAj(x,i))

plt.subplot(2,2,2)
plt.plot(X, Y)
plt.xlabel('j')
plt.ylabel('A')

X = []
Y = []
for i in range(N//2):
    X.append(i)
    Y.append(calcPh(x,i))

plt.subplot(2,2,4)
plt.plot(X, Y)
plt.xlabel('j')
plt.ylabel('Ph')

X = []
Y = []
y = calcBack(x)
for i in range(100):
    X.append(i)
    Y.append(y[i])

plt.subplot(2,2,3)
plt.plot(X, Y)
plt.xlabel('i')
plt.ylabel('F\'(i)')

plt.show()
