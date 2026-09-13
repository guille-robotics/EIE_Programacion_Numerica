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

def f_deriv(x, y):
    return -2*x**3 + 12*x**2 - 20*x + 8.5

def f_analitica(x):
    return -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1

x_num, y_num = heun(f_deriv, 0, 1, 4, 0.5)

x_real = np.linspace(0, 4, 100)
y_real = f_analitica(x_real)

plt.plot(x_real, y_real, label="Solucion Analitica", color="black", linewidth=2)
plt.plot(x_num, y_num, label="Heun (h=0.5)", linestyle="--", marker="o", color="red")

plt.title("Metodo de Heun: Ecuacion Polinomica")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()
