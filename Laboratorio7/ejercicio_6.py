import numpy as np
import matplotlib.pyplot as plt
from funciones import heun

def f_motor(t, w):
    return -5*w + 50

def w_exacta(t):
    return 10 * (1 - np.exp(-5*t))

t0, w0 = 0, 0.0
t_end, h = 0.6, 0.1

t_num, w_num = heun(f_motor, t0, w0, t_end, h)

# Gráfica
plt.figure(figsize=(8, 5))
t_fino = np.linspace(t0, t_end, 100)
plt.plot(t_fino, w_exacta(t_fino), 'k-', linewidth=2, label="Respuesta Analítica")
plt.plot(t_num, w_num, 'g--^', label="RK2 Heun (h=0.1)")
plt.axhline(10, color='orange', linestyle=':', label="Velocidad Estacionaria (10 rad/s)")

plt.title("Transitorio de Micromotor DC N20")
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad Angular (rad/s)")
plt.grid(True)
plt.legend()
plt.show()