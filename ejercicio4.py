# Crea un programa que pida al usuario dos números y muestre su división 
# si el segundo no es cero, o un mensaje de aviso en caso contrario.

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
if num2 != 0:
    division = num1/num2
    print(f"la division entre {num1} y {num2} es: ",division)
else:
    print("no se puede dividir entre cero")