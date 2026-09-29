import numpy as np
import matplotlib.pyplot as plt
from funciones import rk4, error_relativo_porcentual

def f4(t, y):
    return (1 + 4*t)*np.sqrt(y)

def y_analitica4(t):
    return (t**2 + 0.5*t + 1)**2

t0, y0, t_end, h = 0, 1, 1.0, 0.25

t_vals, y_vals = rk4(f4, t0, y0, t_end, h)
y_real = y_analitica4(t_vals)
errores = error_relativo_porcentual(y_real, y_vals)

print("--- Ejercicio 4: Ecuación No Lineal ---")
for i in range(len(t_vals)):
    print(f"t={t_vals[i]:.2f} | y_RK4={y_vals[i]:.5f} | y_real={y_real[i]:.5f} | Error={errores[i]:.5e}%")

plt.figure(figsize=(8,5))
plt.plot(t_vals, y_real, label='Solución Analítica', marker='o', color='blue')
plt.plot(t_vals, y_vals, label='Solución RK4', marker='x', linestyle='--', color='red')
plt.title("Ejercicio 4: RK4 vs Solución Analítica")
plt.xlabel("Tiempo (t) [s]")
plt.ylabel("Amplitud (y) [u]")
plt.grid(True)
plt.legend()
plt.show()