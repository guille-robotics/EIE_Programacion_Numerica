import numpy as np

numeros = np.arange(0, 21)

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Numeros originales:")
print(numeros)

print("Numeros pares:")
print(pares)

print("Numeros impares:")
print(impares)