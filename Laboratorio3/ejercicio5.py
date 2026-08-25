import numpy as np
import matplotlib.pyplot as plt

def amplificar_senal(senal_entrada, ganancia, vmax):
    senal_salida = []
    for vin in senal_entrada:
        v_amp = vin * ganancia
        
        # Recorte de la senal (clipping)
        if v_amp > vmax:
            senal_salida.append(vmax)
        elif v_amp < -vmax:
            senal_salida.append(-vmax)
        else:
            senal_salida.append(v_amp)
            
    return senal_salida

tiempo = np.linspace(0, 0.1, 500)
frecuencia = 20.0
# Senal de entrada
entrada = 2.0 * np.sin(2.0 * np.pi * frecuencia * tiempo)

# Llamado a la funcion
salida_recortada = amplificar_senal(entrada, ganancia=4.0, vmax=5.0)

plt.plot(tiempo, entrada, label="Entrada (V)")
plt.plot(tiempo, salida_recortada, label="Salida Amplificada (V)", 
         linestyle="--", linewidth=2)

plt.title("Saturacion de un amplificador de audio")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.grid()
plt.legend()

plt.show()