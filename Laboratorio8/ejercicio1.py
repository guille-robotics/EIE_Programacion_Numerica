import numpy as np
from funciones import rk4

def f_prueba(t, y):
    return -y + t

t0, y0 = 0, 1
t_end = 1.0
h = 0.5

t_vals, y_vals = rk4(f_prueba, t0, y0, t_end, h)

print("--- Ejercicio 1: Ecuación de Prueba RK4 ---")
print(f"Tiempos (t): {t_vals}")
print(f"Soluciones (y): {y_vals}")