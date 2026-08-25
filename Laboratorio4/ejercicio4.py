import numpy as np

def f(x):
    return 0.25*x**4 - 0.5*x**3 + 0.15*x**2 - 0.1*x + 2.0

def df_real(x):
    return 1.0*x**3 - 1.5*x**2 + 0.3*x - 0.1

x_eval = 0.5
h = 0.25

derivada_exacta = df_real(x_eval)

derivada_adelante = (f(x_eval + h) - f(x_eval)) / h

error = abs(derivada_exacta - derivada_adelante)

print("--- Diferencia Finita Hacia Adelante ---")
print(f"Derivada real: {derivada_exacta}")
print(f"Derivada aproximada: {derivada_adelante}")
print(f"Error absoluto: {error}")