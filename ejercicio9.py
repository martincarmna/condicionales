#Programa que pida tres números y los muestre ordenados (de mayor a menor);

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))


if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        ordenados = [num1, num2, num3]
    else:
        ordenados = [num1, num3, num2]
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        ordenados = [num2, num1, num3]
    else:
        ordenados = [num2, num3, num1]
else:
    if num1 >= num2:
        ordenados = [num3, num1, num2]
    else:
        ordenados = [num3, num2, num1]

print("Números ordenados de mayor a menor:")
for numero in ordenados:
    print(numero)



     
