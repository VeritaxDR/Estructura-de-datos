#Escribe un programa que pida al usuario un número y determine si es par o impar.
# Pide al usuario que ingrese un número
num = int(input("Ingrese un número: "))
# Determina si el número es par o impar
num = num % 2
if num == 0:
    resultado = "El número es par."
elif num == 1:
    resultado = "El número es impar."
else:
    resultado = "El número no es par ni impar."
# Muestra el resultado
print(resultado)