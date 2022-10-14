from matplotlib import pyplot as plt
from numpy import pi, cos, arctan, sqrt, sin
from random import shuffle

A = [1, 3, 4, 10, 11, 14, 17]
PH = [pi / 6, pi / 4, pi / 3, pi / 2, 3 * pi / 4, pi]
N = 512


shuffle(A)
shuffle(PH)


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


def generateSignal(n):
    x = []
    for i in range(n):
        z = 0
        for j in range(30):
            z += A[j%len(A)]*cos(2*pi*j*i/n - PH[j%len(PH)])
        x.append(z)
    return x


def calcBackA(x):
    A = [calcAj(x, j) for j in range(N//2)]
    PH = [calcPh(x,j) for j in range(N//2)]
    res = []
    for i in range(len(x)):
        z = A[0]/2
        for j in range(1, N//2):
            z += A[j]*cos(2*pi*j*i/N - PH[j])
        res.append(z)
    return res


def calcBackB(x):
    A = [calcAj(x, j) for j in range(N//2)]
    res = []
    for i in range(len(x)):
        z = A[0]/2
        for j in range(1, N//2):
            z += A[j]*cos(2*pi*j*i/N)
        res.append(z)
    return res


x = generateSignal(N)
X = []
Y = []
for i in range(100):
    X.append(i)
    Y.append(x[i])

plt.subplot(3,2,1)
plt.plot(X, Y)
plt.xlabel('i')
plt.ylabel('f(i)')

X = []
Y = []
for i in range(N//2):
    X.append(i)
    Y.append(calcAj(x,i))

plt.subplot(3,2,2)
plt.plot(X, Y)
plt.xlabel('j')
plt.ylabel('A')

X = []
Y = []
for i in range(N//2):
    X.append(i)
    Y.append(calcPh(x,i))

plt.subplot(3,2,4)
plt.plot(X, Y)
plt.xlabel('j')
plt.ylabel('Ph')

X = []
Y = []
y = calcBackA(x)
for i in range(100):
    X.append(i)
    Y.append(y[i])

plt.subplot(3,2,3)
plt.plot(X, Y)
plt.xlabel('i')
plt.ylabel('F\'(i)')

X = []
Y = []
y = calcBackB(x)
for i in range(100):
    X.append(i)
    Y.append(y[i])

plt.subplot(3,2,5)
plt.plot(X, Y)
plt.xlabel('i')
plt.ylabel('F\'(i) - ph')

plt.show()





