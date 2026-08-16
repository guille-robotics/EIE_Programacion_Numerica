import numpy as np
import matplotlib.pyplot as plt

voltaje = 12.0
dt = 1.0

tiempo = np.arange(0.0, 10.0, dt)

energia = 0.0

instantes = []
corrientes = []
energias = []

for t in tiempo:

    if t < 4.0:
        corriente = 0.2
    elif t < 7.0:
        corriente = 0.5
    else:
        corriente = 0.1

    potencia = voltaje * corriente

    energia = energia + potencia * dt

    instantes.append(t + dt)
    corrientes.append(corriente)
    energias.append(energia)

print("Energia total:",
      energia, "J")

plt.plot(instantes, energias, marker="o")

plt.title("Energia consumida por el sistema")
plt.xlabel("Tiempo (s)")
plt.ylabel("Energia acumulada (J)")
plt.grid()

plt.show()