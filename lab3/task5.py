import numpy as np
from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq, irfft

SAMPLE_RATE = 6000  # Гц
DURATION = 1  # Секунды


def generateSignal(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    # 2pi для преобразования в радианы
    y = np.sin((2 * np.pi) * frequencies)
    return x, y


# Генерируем волну с частотой 2 Гц, которая длится 5 секунд
x, f1 = generateSignal(40, SAMPLE_RATE, DURATION)
_, f2 = generateSignal(400, SAMPLE_RATE, DURATION)
_, f3 = generateSignal(800, SAMPLE_RATE, DURATION)
signal = f1 + f2 + f3

countToShow = 80
plt.subplot(221)
plt.plot(x[:countToShow], f1[:countToShow], label="f1")
plt.plot(x[:countToShow], f2[:countToShow], label="f2")
plt.plot(x[:countToShow], f3[:countToShow], label="f3")
plt.plot(x[:countToShow], signal[:countToShow], label="combo")
plt.legend()



N = SAMPLE_RATE * DURATION

yf = rfft(signal)
xf = rfftfreq(N, 1 / SAMPLE_RATE)

plt.subplot(222)
plt.plot(xf, np.abs(yf))



F1 = yf.copy()
for i in range(100):
    F1[i] = 0
f1 = irfft(F1)
plt.subplot(223)
plt.plot(x[:countToShow], f1[:countToShow])
plt.subplot(224)
plt.plot(xf, np.abs(F1))
plt.show()



F2 = yf.copy()
for i in range(300,600):
    F2[i] = 0
f2 = irfft(F2)
plt.subplot(221)
plt.plot(x[:countToShow], f2[:countToShow])
plt.subplot(222)
plt.plot(xf, np.abs(F2))



F3 = yf.copy()
for i in range(600, len(F3)):
    F3[i] = 0
f3 = irfft(F3)
plt.subplot(223)
plt.plot(x[:countToShow], f3[:countToShow])
plt.subplot(224)
plt.plot(xf, np.abs(F3))
plt.show()
