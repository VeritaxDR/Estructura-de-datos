#Escribe un programa que pida al usuario un número y determine si es positivo, negativo o cero. 
# Pide al usuario que ingrese un número
num = float(input("Ingrese un número: "))
# Determina si el número es positivo, negativo o cero
if num > 0:
    resultado = "El número es positivo."
elif num < 0:
    resultado = "El número es negativo."
else:
    resultado = "El número es cero."
# Muestra el resultado
print(resultado)
