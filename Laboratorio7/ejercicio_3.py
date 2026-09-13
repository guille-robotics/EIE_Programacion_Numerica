import numpy as np
import matplotlib.pyplot as plt
from funciones import euler, heun

def f_ej3(t, y):
    return (1 + 4*t) * np.sqrt(max(y, 0))

def y_exacta(t):
    return (t**2 + 0.5*t + 1)**2

t0, y0 = 0, 1.0
t_end, h = 1, 0.25

# Soluciones numéricas
t_e, y_e = euler(f_ej3, t0, y0, t_end, h)
t_h, y_h = heun(f_ej3, t0, y0, t_end, h)
y_real = y_exacta(t_e) # Se calculan en los mismos puntos discretos

# Cálculo de Error Relativo Porcentual Verdadero
error_e = np.abs((y_real - y_e) / y_real) * 100
error_h = np.abs((y_real - y_h) / y_real) * 100

# Gráficos (1x2 para ver curvas y errores)
plt.figure(figsize=(12, 5))

# Subplot 1: Soluciones
plt.subplot(1, 2, 1)
t_fino = np.linspace(t0, t_end, 100)
plt.plot(t_fino, y_exacta(t_fino), 'k-', label="Analítica")
plt.plot(t_e, y_e, 'b--o', label="RK1 Euler")
plt.plot(t_h, y_h, 'g--s', label="RK2 Heun")
plt.title("Comparación de Métodos (h=0.25)")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid(True)
plt.legend()

# Subplot 2: Errores
plt.subplot(1, 2, 2)
plt.plot(t_e, error_e, 'b--o', label="Error Euler (%)")
plt.plot(t_h, error_h, 'g--s', label="Error Heun (%)")
plt.title("Error Relativo Porcentual")
plt.xlabel("t")
plt.ylabel("Error (%)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()