import numpy as np
import matplotlib.pyplot as plt
import math

x0 = np.pi / 3
valor_real = np.cos(x0)

terminos = np.arange(1, 11)
errores = []

for N in terminos:
    aprox = 0.0
    for n in range(N):
        aprox += ((-1)**n / math.factorial(2*n)) * (x0**(2*n))
        
    error_abs = abs(valor_real - aprox)
    errores.append(error_abs)

print("Error absoluto con N=5:", errores[4])

plt.plot(terminos, errores, marker="o", color="red")
plt.title("Error de aproximacion del Coseno (x = pi/3)")
plt.xlabel("Numero de terminos (N)")
plt.ylabel("Error absoluto")
plt.yscale("log") # Escala logaritmica para visualizar mejor la caida
plt.grid()

plt.show()