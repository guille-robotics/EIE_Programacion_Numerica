import numpy as np
import matplotlib.pyplot as plt

def euler(f, x0, y0, x_end, h):
    x_vals = np.arange(x0, x_end + h, h)
    y_vals = np.zeros(len(x_vals))
    y_vals[0] = y0
    
    for i in range(1, len(x_vals)):
        y_vals[i] = y_vals[i-1] + f(x_vals[i-1], y_vals[i-1]) * h
        
    return x_vals, y_vals

def f_deriv(x, y):
    return -2*x**3 + 12*x**2 - 20*x + 8.5

def f_exacta(x):
    return -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1

x_euler, y_euler = euler(f_deriv, 0, 1, 4, 0.5)

x_exact = np.linspace(0, 4, 100)
y_exact = f_exacta(x_exact)

plt.plot(x_exact, y_exact, label="Solucion Exacta", color="black", linewidth=2)
plt.plot(x_euler, y_euler, label="Euler (h=0.5)", linestyle="--", marker="o", color="red")

plt.title("Metodo de Euler: Ecuacion Polinomica")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()
