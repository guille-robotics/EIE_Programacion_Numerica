import numpy as np
import matplotlib.pyplot as plt

amplitud = 5.0
frecuencia = 50.0

tiempo = np.arange(0.0, 0.0401, 0.0005)

entrada = amplitud * np.sin(
    2.0 * np.pi * frecuencia * tiempo
)

salida = []

for voltaje in entrada:

    if voltaje >= 0:
        salida.append(voltaje)
    else:
        salida.append(0.0)

plt.plot(tiempo, entrada, label="Entrada")
plt.plot(tiempo, salida, label="Salida")

plt.title("Rectificador ideal de media onda")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid()
plt.legend()

plt.show()