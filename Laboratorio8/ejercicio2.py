import numpy as np
import matplotlib.pyplot as plt
from funciones import rk4, error_relativo_porcentual

def f2(t, y):
    return -2*t**3 + 12*t**2 - 20*t + 8.5

def y_analitica2(t):
    return -0.5*t**4 + 4*t**3 - 10*t**2 + 8.5*t + 1

t0, y0, t_end, h = 0, 1, 2.0, 0.5

t_vals, y_vals = rk4(f2, t0, y0, t_end, h)
y_real = y_analitica2(t_vals)
errores = error_relativo_porcentual(y_real, y_vals)

print("--- Ejercicio 2: Polinomio de Tercer Grado ---")
for i in range(len(t_vals)):
    print(f"t={t_vals[i]:.1f} | y_RK4={y_vals[i]:.5f} | y_real={y_real[i]:.5f} | Error={errores[i]:.5f}%")

plt.figure(figsize=(8,5))
plt.plot(t_vals, y_real, label='Solución Analítica', marker='o', color='blue')
plt.plot(t_vals, y_vals, label='Solución RK4', marker='x', linestyle='--', color='red')
plt.title("Ejercicio 2: RK4 vs Solución Analítica")
plt.xlabel("Tiempo (t) [s]")
plt.ylabel("Amplitud (y) [u]")
plt.grid(True)
plt.legend()
plt.show()