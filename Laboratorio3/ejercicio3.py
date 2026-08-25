import numpy as np
import matplotlib.pyplot as plt

def posicion_balon(t, v0, angulo_rad, g):
    x = v0 * np.cos(angulo_rad) * t
    y = v0 * np.sin(angulo_rad) * t - 0.5 * g * t**2
    return x, y

v0 = 25.0
angulo = 30.0
g = 9.81
angulo_rad = np.deg2rad(angulo)

tiempos = np.arange(0.0, 3.0, 0.05)

x_lista = []
y_lista = []

for t in tiempos:
    x_actual, y_actual = posicion_balon(t, v0, angulo_rad, g)
    
    # Solo almacenar si el balon esta sobre el suelo
    if y_actual >= 0:
        x_lista.append(x_actual)
        y_lista.append(y_actual)

plt.plot(x_lista, y_lista, marker=".", linestyle="-")

plt.title("Trayectoria del balon de futbol")
plt.xlabel("Distancia horizontal (m)")
plt.ylabel("Altura (m)")
plt.grid()
plt.legend(["Trayectoria valida"])

plt.show()