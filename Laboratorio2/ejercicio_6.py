import numpy as np
import matplotlib.pyplot as plt

voltaje_fuente = 5.0

resistencia = 1000.0
capacitancia_uF = 1000.0

capacitancia = capacitancia_uF * 1e-6

dt = 0.05
tiempo_final = 6.0
tiempo_cambio = 3.0

tiempo = np.arange(
    0.0,
    tiempo_final + dt,
    dt
)

voltaje_capacitor = [0.0]
fuente = []

for k in range(len(tiempo) - 1):

    t = tiempo[k]

    if t < tiempo_cambio:
        vs = voltaje_fuente
    else:
        vs = 0.0

    fuente.append(vs)

    v_actual = voltaje_capacitor[-1]

    dvdt = (
        vs - v_actual
    ) / (resistencia * capacitancia)

    v_nuevo = v_actual + dt * dvdt

    voltaje_capacitor.append(v_nuevo)

if tiempo[-1] < tiempo_cambio:
    fuente.append(voltaje_fuente)
else:
    fuente.append(0.0)

plt.plot(
    tiempo,
    fuente,
    label="Fuente"
)

plt.plot(
    tiempo,
    voltaje_capacitor,
    label="Capacitor"
)

plt.title(
    "Circuito RC mediante el metodo de Euler"
)
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid()
plt.legend()

plt.show()