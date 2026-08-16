import numpy as np
import matplotlib.pyplot as plt
import math

def maclaurin_exp(x, N):
    aprox = np.zeros_like(x)
    for n in range(N):
        aprox += (x**n) / math.factorial(n)
    return aprox

x = np.linspace(-3, 3, 100)
y_real = np.exp(x)

y_aprox_2 = maclaurin_exp(x, 2)
y_aprox_4 = maclaurin_exp(x, 4)
y_aprox_6 = maclaurin_exp(x, 6)

plt.plot(x, y_real, label="e^x Real", color="black", linewidth=2)
plt.plot(x, y_aprox_2, label="Maclaurin N=2", linestyle="--")
plt.plot(x, y_aprox_4, label="Maclaurin N=4", linestyle="-.")
plt.plot(x, y_aprox_6, label="Maclaurin N=6", linestyle=":")

plt.title("Aproximacion de la Exponencial por Maclaurin")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.ylim(0, 25)
plt.grid()
plt.legend()

plt.show()