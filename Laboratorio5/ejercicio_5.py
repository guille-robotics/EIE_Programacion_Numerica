import numpy as np
import matplotlib.pyplot as plt

def euler(f, x0, y0, x_end, h):
    x_vals = np.arange(x0, x_end + h, h)
    y_vals = np.zeros(len(x_vals))
    y_vals[0] = y0
    for i in range(1, len(x_vals)):
        y_vals[i] = y_vals[i-1] + f(x_vals[i-1], y_vals[i-1]) * h
    return x_vals, y_vals

Ta = 20
k = 0.1

def enfriamiento(t, T):
    return -k * (T - Ta)

t_euler, T_euler = euler(enfriamiento, 0, 80, 20, 2.0)

plt.plot(t_euler, T_euler, label="Temperatura (Euler)", marker="o", color="red")
plt.axhline(Ta, color='black', linestyle=':', label="Temperatura Ambiente (20 C)")

plt.title("Enfriamiento de Newton")
plt.xlabel("Tiempo (min)")
plt.ylabel("Temperatura (C)")
plt.ylim(10, 90)
plt.grid()
plt.legend()
plt.show()
