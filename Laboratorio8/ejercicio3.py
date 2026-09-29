import numpy as np
import matplotlib.pyplot as plt
from funciones import rk4, error_relativo_porcentual

def f3(t, y):
    return 4*np.exp(0.8*t) - 0.5*y

def y_analitica3(t):
    return (40/13)*np.exp(0.8*t) - (14/13)*np.exp(-0.5*t)

t0, y0, t_end, h = 0, 2, 2.0, 0.5

t_vals, y_vals = rk4(f3, t0, y0, t_end, h)
y_real = y_analitica3(t_vals)
errores = error_relativo_porcentual(y_real, y_vals)

print("--- Ejercicio 3: Ecuación Exponencial ---")
for i in range(len(t_vals)):
    print(f"t={t_vals[i]:.1f} | y_RK4={y_vals[i]:.5f} | y_real={y_real[i]:.5f} | Error={errores[i]:.5f}%")

plt.figure(figsize=(8,5))
plt.plot(t_vals, y_real, label='Solución Analítica', marker='o', color='blue')
plt.plot(t_vals, y_vals, label='Solución RK4', marker='x', linestyle='--', color='red')
plt.title("Ejercicio 3: RK4 vs Solución Analítica")
plt.xlabel("Tiempo (t) [s]")
plt.ylabel("Amplitud (y) [u]")
plt.grid(True)
plt.legend()
plt.show()