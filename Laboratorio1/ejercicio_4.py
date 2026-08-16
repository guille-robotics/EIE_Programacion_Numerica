import numpy as np
import matplotlib.pyplot as plt

amplitud = float(input("Ingrese la amplitud en V: "))
frecuencia = float(input("Ingrese la frecuencia en Hz: "))

periodo = 1.0 / frecuencia
tiempo = np.linspace(0.0, 2.0 * periodo, 200)
voltaje = amplitud * np.sin(2.0 * np.pi * frecuencia * tiempo)

print("Periodo:", periodo, "s")

plt.plot(tiempo, voltaje)
plt.title("Senal sinusoidal")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid()
plt.show()