import numpy as np
import matplotlib.pyplot as plt

v0 = 20.0
angulo = 45.0
g = 9.81

angulo_rad = np.deg2rad(angulo)

tiempos = np.arange(0.0, 3.1, 0.1)

tiempos_validos = []
posicion_x = []
posicion_y = []

for t in tiempos:

    x = v0 * np.cos(angulo_rad) * t

    y = (v0 * np.sin(angulo_rad) * t
         - 0.5 * g * t**2)

    if y >= 0:
        tiempos_validos.append(t)
        posicion_x.append(x)
        posicion_y.append(y)

plt.plot(posicion_x, posicion_y)

plt.title("Movimiento parabolico")
plt.xlabel("Posicion horizontal (m)")
plt.ylabel("Altura (m)")
plt.grid()

plt.show()