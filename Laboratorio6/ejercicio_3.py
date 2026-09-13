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

def f_deriv(t, y):
    return (1 + 4*t) * np.sqrt(y)

def f_analitica(t):
    return (t**2 + 0.5*t + 1)**2

t_num, y_num = heun(f_deriv, 0, 1, 1, 0.25)

t_real = np.linspace(0, 1, 100)
y_real = f_analitica(t_real)

plt.plot(t_real, y_real, label="Solucion Analitica", color="black", linewidth=2)
plt.plot(t_num, y_num, label="Heun (h=0.25)", linestyle="--", marker="o", color="blue")

plt.title("Metodo de Heun: Ecuacion No Lineal")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid()
plt.legend()
plt.show()
