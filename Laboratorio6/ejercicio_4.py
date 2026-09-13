import numpy as np
import matplotlib.pyplot as plt

def punto_medio(f, x0, y0, x_end, h):
    x_vals = np.arange(x0, x_end + h, h)
    y_vals = np.zeros(len(x_vals))
    y_vals[0] = y0
    for i in range(1, len(x_vals)):
        x_i = x_vals[i-1]
        y_i = y_vals[i-1]
        
        t_half = x_i + h / 2
        y_half = y_i + f(x_i, y_i) * (h / 2)
        y_vals[i] = y_i + f(t_half, y_half) * h
    return x_vals, y_vals

def f_deriv(t, y):
    return -2*y + t**2

def f_analitica(t):
    return 0.75 * np.exp(-2*t) + 0.5*t**2 - 0.5*t + 0.25

t_num, y_num = punto_medio(f_deriv, 0, 1, 3, 0.5)

t_real = np.linspace(0, 3, 100)
y_real = f_analitica(t_real)

plt.plot(t_real, y_real, label="Solucion Analitica", color="black", linewidth=2)
plt.plot(t_num, y_num, label="Punto Medio (h=0.5)", linestyle="--", marker="o", color="orange")

plt.title("Metodo del Punto Medio: Dependencia Mixta")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid()
plt.legend()
plt.show()
