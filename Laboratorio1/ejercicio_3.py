import numpy as np

x1 = float(input("Ingrese x1 en cm: "))
y1 = float(input("Ingrese y1 en cm: "))
x2 = float(input("Ingrese x2 en cm: "))
y2 = float(input("Ingrese y2 en cm: "))

dx = x2 - x1
dy = y2 - y1
distancia = np.sqrt(dx**2 + dy**2)

print("Distancia entre los sensores:", distancia, "cm")