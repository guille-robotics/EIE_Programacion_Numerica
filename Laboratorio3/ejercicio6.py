import numpy as np

def f(x):
    return -0.15*x**4 - 0.1*x**3 - 0.4*x**2 - 0.2*x + 1.5

def df_real(x):
    return -0.6*x**3 - 0.3*x**2 - 0.8*x - 0.2

x_eval = 0.5
h = 0.5

derivada_exacta = df_real(x_eval)

derivada_centrada = (f(x_eval + h) - f(x_eval - h)) / (2 * h)

error = abs(derivada_exacta - derivada_centrada)

print("--- Diferencia Finita Centrada ---")
print(f"Derivada real en x=0.5: {derivada_exacta}")
print(f"Derivada aproximada: {derivada_centrada}")
print(f"Error absoluto: {error}")