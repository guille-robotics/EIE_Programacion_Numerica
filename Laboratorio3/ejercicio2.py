import numpy as np
import matplotlib.pyplot as plt

def velocidad_caida_libre(t, v0, g):
    # La funcion evalua la ecuacion de velocidad de forma vectorizada
    return v0 - g * t

# Parametros iniciales
v0 = 0.0
g = 9.81

# Arreglo de tiempo usando np.linspace
tiempo = np.linspace(0, 5, 50)

# Llamado a la funcion
velocidades = velocidad_caida_libre(tiempo, v0, g)

# Creacion del grafico
plt.plot(tiempo, velocidades, color="red")

plt.title("Velocidad en caida libre")
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.grid()

plt.show()