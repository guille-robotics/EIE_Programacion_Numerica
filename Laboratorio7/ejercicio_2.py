import numpy as np
import matplotlib.pyplot as plt
from funciones import ralston

def f_tanque(t, y):
    # max(y, 0) evita raíces negativas si el método numérico traspasa levemente el 0
    return -0.06 * np.sqrt(max(y, 0))

def y_exacta(t):
    val = np.sqrt(3) - 0.03 * t
    return np.where(val > 0, val**2, 0) # Si val < 0, el tanque ya está vacío (y=0)

t0, y0 = 0, 3.0
t_end, h = 60, 0.5

# Simulación numérica
t_num, y_num = ralston(f_tanque, t0, y0, t_end, h)

# Tiempo de vaciado analítico: y(t) = 0 => (sqrt(3) - 0.03t) = 0 => t = sqrt(3)/0.03
t_vaciado = np.sqrt(3) / 0.03
print(f"El tanque se vacía teóricamente a los {t_vaciado:.2f} minutos.")

# Gráfica
plt.figure(figsize=(8, 5))
t_fino = np.linspace(t0, t_end, 200)
plt.plot(t_fino, y_exacta(t_fino), 'k-', linewidth=2, label="Solución Analítica")
plt.plot(t_num, y_num, 'r--', marker='.', label="RK2 Ralston (h=0.5)")
plt.axvline(t_vaciado, color='gray', linestyle=':', label="Vaciado completo")

plt.title("Vaciado de Tanque Cilíndrico")
plt.xlabel("Tiempo (min)")
plt.ylabel("Nivel de agua (m)")
plt.grid(True)
plt.legend()
plt.show()