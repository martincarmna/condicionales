# Programa que pida dos números e indique Cuál es el mayor
# Si los dos son iguales que muestre el mensaje "Son iguales"

n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))
if  n2 < n1:
    print("el numero menor es: ",n1)
elif n1 < n2:
        print("el numero mayor es: ",n2)
else:
    print(f"los numeros son iguales")

