import numpy as np
import matplotlib.pyplot as plt

resistencia = 220.0
voltaje_led = 2.0

voltajes = np.arange(0.0, 5.1, 0.1)

corrientes = []

for voltaje in voltajes:

    if voltaje <= voltaje_led:
        corriente = 0.0
    else:
        corriente = (
            voltaje - voltaje_led
        ) / resistencia

    corriente_mA = corriente * 1000.0
    corrientes.append(corriente_mA)

print("Corriente para 5 V:",
      corrientes[-1], "mA")

plt.plot(voltajes, corrientes)

plt.title("Corriente de un LED")
plt.xlabel("Voltaje de alimentacion (V)")
plt.ylabel("Corriente (mA)")
plt.grid()

plt.show()