import numpy as np
import matplotlib.pyplot as plt

def euler(f, x0, y0, x_end, h):
    x_vals = np.arange(x0, x_end + h, h)
    y_vals = np.zeros(len(x_vals))
    y_vals[0] = y0
    for i in range(1, len(x_vals)):
        y_vals[i] = y_vals[i-1] + f(x_vals[i-1], y_vals[i-1]) * h
    return x_vals, y_vals

def f_deriv(t, y):
    return y * t**2 - 1.1 * y

t_euler_1, y_euler_1 = euler(f_deriv, 0, 1, 2, 0.5)
t_euler_2, y_euler_2 = euler(f_deriv, 0, 1, 2, 0.25)

plt.plot(t_euler_1, y_euler_1, label="Euler (h=0.5)", linestyle="--", marker="o")
plt.plot(t_euler_2, y_euler_2, label="Euler (h=0.25)", linestyle="-.", marker="s")

plt.title("Metodo de Euler: Comparacion de pasos")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid()
plt.legend()
plt.show()
