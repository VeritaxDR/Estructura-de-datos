#Escribe un programa que pida al usuario dos números y muestre la suma, resta, multiplicación y división de esos números. 
# Pide al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
# Realiza las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "Error: División por cero"
# Muestra los resultados
print("Resultados:")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)