# Programa que pida un número y diga si es positivo, negativo o 0.
num = int(input("ingrese un numero: "))
if  num < 0:
    print("el numero negativos es: ",num)
elif num > 0:
    print("el numero positivo es: ",num)
else:
    print("el numeron es igual a cero")
