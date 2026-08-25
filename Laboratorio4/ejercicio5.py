import numpy as np

def f(x):
    return -0.3*x**4 + 0.2*x**3 - 0.6*x**2 + 1.5*x - 1.0

def df_real(x):
    return -1.2*x**3 + 0.6*x**2 - 1.2*x + 1.5

x_eval = 1.0
h = 0.1

derivada_exacta = df_real(x_eval)

derivada_atras = (f(x_eval) - f(x_eval - h)) / h

error = abs(derivada_exacta - derivada_atras)

print("--- Diferencia Finita Hacia Atras ---")
print(f"Derivada real en x=1.0: {derivada_exacta}")
print(f"Derivada aproximada: {derivada_atras}")
print(f"Error absoluto: {error}")