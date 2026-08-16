import numpy as np
import matplotlib.pyplot as plt

altura_inicial = float(input("Ingrese la altura inicial en m: "))
g = 9.81

tiempo_impacto = np.sqrt(2.0 * altura_inicial / g)
tiempo = np.linspace(0.0, tiempo_impacto, 200)
altura = altura_inicial - 0.5 * g * tiempo**2

print("Tiempo de impacto:", tiempo_impacto, "s")

plt.plot(tiempo, altura)
plt.title("Caida libre")
plt.xlabel("Tiempo (s)")
plt.ylabel("Altura (m)")
plt.grid()
plt.show()