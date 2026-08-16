voltaje = float(input("Ingrese el voltaje en V: "))
resistencia = float(input("Ingrese la resistencia en ohm: "))

corriente = voltaje / resistencia
potencia = voltaje * corriente

print("Corriente:", corriente, "A")
print("Potencia:", potencia, "W")