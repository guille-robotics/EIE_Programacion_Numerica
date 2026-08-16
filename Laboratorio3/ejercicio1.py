import numpy as np
import matplotlib.pyplot as plt
import math

def taylor_seno(x, N):
    aprox = np.zeros_like(x)
    for n in range(N):
        termino = ((-1)**n / math.factorial(2*n + 1)) * (x**(2*n + 1))
        aprox += termino
    return aprox

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y_real = np.sin(x)

y_aprox_1 = taylor_seno(x, 1)
y_aprox_3 = taylor_seno(x, 3)
y_aprox_5 = taylor_seno(x, 5)

print(y_aprox_1)

plt.plot(x, y_real, label="sin(x) Real", color="black", linewidth=2)
plt.plot(x, y_aprox_1, label="Taylor N=1", linestyle="--")
plt.plot(x, y_aprox_3, label="Taylor N=3", linestyle="-.")
plt.plot(x, y_aprox_5, label="Taylor N=5", linestyle=":")

plt.title("Aproximacion del Seno por Serie de Taylor")
plt.xlabel("Angulo (rad)")
plt.ylabel("Amplitud")
plt.ylim(-2, 2)
plt.grid()
plt.legend()

plt.show()