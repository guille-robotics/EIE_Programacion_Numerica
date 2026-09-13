import numpy as np
import matplotlib.pyplot as plt

def heun(f, x0, y0, x_end, h):
    x_vals = np.arange(x0, x_end + h, h)
    y_vals = np.zeros(len(x_vals))
    y_vals[0] = y0
    for i in range(1, len(x_vals)):
        x_i = x_vals[i-1]
        y_i = y_vals[i-1]
        x_next = x_vals[i]
        
        y_predict = y_i + f(x_i, y_i) * h
        y_vals[i] = y_i + (f(x_i, y_i) + f(x_next, y_predict)) / 2 * h
    return x_vals, y_vals

Ta = 20
k = 0.1

def enfriamiento(t, T):
    return -k * (T - Ta)

t_num, T_num = heun(enfriamiento, 0, 80, 20, 2.0)

plt.plot(t_num, T_num, label="Temperatura (Heun)", marker="o", color="red")
plt.axhline(Ta, color='black', linestyle=':', label="Temperatura Ambiente (20 C)")

plt.title("Enfriamiento de Newton con Heun")
plt.xlabel("Tiempo (min)")
plt.ylabel("Temperatura (C)")
plt.ylim(10, 90)
plt.grid()
plt.legend()
plt.show()
