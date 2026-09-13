import numpy as np
import matplotlib.pyplot as plt

def punto_medio(f, x0, y0, x_end, h):
    x_vals = np.arange(x0, x_end + h, h)
    y_vals = np.zeros(len(x_vals))
    y_vals[0] = y0
    for i in range(1, len(x_vals)):
        x_i = x_vals[i-1]
        y_i = y_vals[i-1]
        
        t_half = x_i + h / 2
        y_half = y_i + f(x_i, y_i) * (h / 2)
        y_vals[i] = y_i + f(t_half, y_half) * h
    return x_vals, y_vals

r = 0.5
K = 100

def crecimiento(t, P):
    return r * P * (1 - P / K)

t_num, P_num = punto_medio(crecimiento, 0, 10, 15, 1.0)

plt.plot(t_num, P_num, label="Poblacion (Punto Medio)", marker="o", color="green")
plt.axhline(K, color='black', linestyle=':', label="Capacidad de Carga K (100)")

plt.title("Crecimiento Logistico de Poblacion (Punto Medio)")
plt.xlabel("Tiempo (anos)")
plt.ylabel("Cantidad de Individuos")
plt.grid()
plt.legend()
plt.show()
