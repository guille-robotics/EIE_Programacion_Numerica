import matplotlib.pyplot as plt

def procesar_sensores(*args):
    # Si no se entregan argumentos, la tupla args estara vacia
    if len(args) == 0:
        return []
    
    valores_validos = []
    
    for lectura in args:
        # Ignorar valores negativos (errores de lectura)
        if lectura >= 0:
            valores_validos.append(lectura)
            
    return valores_validos

# Llamado pasando argumentos separados por coma
datos_limpios = procesar_sensores(15.2, 16.4, -3.1, 14.8, -0.5, 17.1)

# Para el eje x creamos una lista de indices del mismo tamano
indices = range(1, len(datos_limpios) + 1)

plt.plot(indices, datos_limpios, marker="o", linestyle="--")

plt.title("Lecturas validas del sensor")
plt.xlabel("Numero de muestra")
plt.ylabel("Temperatura (C)")
plt.grid()

plt.show()