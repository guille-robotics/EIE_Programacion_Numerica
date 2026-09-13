import numpy as np
import matplotlib.pyplot as plt
from funciones import ralston

def f_ej4(t, y):
    return -2*y + t**2

def y_exacta(t):
    return 0.75 * np.exp(-2*t) + 0.5*t**2 - 0.5*t + 0.25

t0, y0 = 0, 1.0
t_end, h = 3, 0.5

t_num, y_num = ralston(f_ej4, t0, y0, t_end, h)
y_real = y_exacta(t_num)

# Mostrar tabla de errores en consola
error = np.abs((y_real - y_num) / y_real) * 100
print(" t   |  Error (%)")
print("-----------------")
for t_i, err in zip(t_num, error):
    print(f"{t_i:.1f}  |  {err:.2f}%")

# Gráfica
plt.figure(figsize=(8, 5))
t_fino = np.linspace(t0, t_end, 100)
plt.plot(t_fino, y_exacta(t_fino), 'k-', linewidth=2, label="Solución Analítica")
plt.plot(t_num, y_num, 'm--o', label="RK2 Ralston")

plt.title("Ecuación Diferencial Lineal con RK2 Ralston")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid(True)
plt.legend()
plt.show()