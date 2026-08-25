import numpy as np
import matplotlib.pyplot as plt

def simular_termostato(T_inicial, T_objetivo):
    dt = 0.5
    tiempos = np.arange(0, 30.5, dt)
    
    temperaturas = [T_inicial]
    estado_calefactor = 0 # 0 = apagado, 1 = encendido
    
    # Iteramos considerando que ya tenemos el primer punto evaluado
    for t in tiempos[:-1]:
        T_actual = temperaturas[-1]
        
        # Logica del termostato
        if T_actual < (T_objetivo - 1.0):
            estado_calefactor = 1
        elif T_actual > (T_objetivo + 1.0):
            estado_calefactor = 0
            
        # Actualizacion de la ecuacion
        T_nuevo = T_actual + dt * (1.5 * estado_calefactor 
                                   - 0.2 * (T_actual - 15.0))
        
        temperaturas.append(T_nuevo)
        
    return tiempos, temperaturas

# Parametros de prueba
T_ini = 16.0
T_obj = 22.0

# Ejecucion de la funcion
tiempos_sim, temps_sim = simular_termostato(T_ini, T_obj)

plt.plot(tiempos_sim, temps_sim, label="Temperatura Habitacion", color="blue")
plt.axhline(y=T_obj, color='red', linestyle='--', label="Objetivo (22 C)")
plt.axhline(y=T_obj - 1.0, color='green', linestyle=':', label="Limites")
plt.axhline(y=T_obj + 1.0, color='green', linestyle=':')

plt.title("Control On/Off de Termostato")
plt.xlabel("Tiempo (min)")
plt.ylabel("Temperatura (C)")
plt.grid()
plt.legend()

plt.show()