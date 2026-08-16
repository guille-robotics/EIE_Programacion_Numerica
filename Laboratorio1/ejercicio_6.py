import numpy as np
import matplotlib.pyplot as plt

voltaje_fuente = float(input("Ingrese Vs en V: "))
resistencia = float(input("Ingrese R en ohm: "))
capacitancia_uF = float(input("Ingrese C en microfaradios: "))

capacitancia = capacitancia_uF * 1e-6
tau = resistencia * capacitancia

tiempo = np.linspace(0.0, 5.0 * tau, 300)
voltaje_capacitor = voltaje_fuente * (1.0 - np.exp(-tiempo / tau))
voltaje_en_tau = voltaje_fuente * (1.0 - np.exp(-1.0))

print("Constante de tiempo:", tau, "s")
print("Voltaje del capacitor en t = tau:", voltaje_en_tau, "V")

plt.plot(tiempo, voltaje_capacitor)
plt.title("Carga de un capacitor en un circuito RC")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje del capacitor (V)")
plt.grid()
plt.show()