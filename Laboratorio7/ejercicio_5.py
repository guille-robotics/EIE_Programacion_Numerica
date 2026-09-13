import numpy as np
import matplotlib.pyplot as plt
from funciones import punto_medio

def f_rc(t, v):
    return 10 - 2*v

def v_exacta(t):
    return 5 * (1 - np.exp(-2*t))

t0, v0 = 0, 0.0
t_end, h = 2, 0.25

t_num, v_num = punto_medio(f_rc, t0, v0, t_end, h)

# Gráfica
plt.figure(figsize=(8, 5))
t_fino = np.linspace(t0, t_end, 100)
plt.plot(t_fino, v_exacta(t_fino), 'k-', linewidth=2, label="Curva Analítica")
plt.plot(t_num, v_num, 'c--s', label="RK2 Punto Medio (h=0.25)")
plt.axhline(5, color='r', linestyle=':', label="Voltaje Fuente (5V)")

plt.title("Carga de un Condensador de Desacople")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid(True)
plt.legend()
plt.show()