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
    return (1 + 4*t) * np.sqrt(y)

def f_exacta(t):
    return (t**2 + 0.5*t + 1)**2

t_euler, y_euler = euler(f_deriv, 0, 1, 1, 0.25)

t_exact = np.linspace(0, 1, 100)
y_exact = f_exacta(t_exact)

plt.plot(t_exact, y_exact, label="Solucion Exacta", color="black", linewidth=2)
plt.plot(t_euler, y_euler, label="Euler (h=0.25)", linestyle="--", marker="o", color="blue")

plt.title("Metodo de Euler: Ecuacion No Lineal")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid()
plt.legend()
plt.show()
