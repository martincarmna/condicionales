#Programa que pida dos números 'nota' y 'edad' y un carácter 'sexo' 
#y muestre el mensaje 'ACEPTADA' si la nota es mayor o igual a cinco, 
#la edad es mayor o igual a dieciocho y el sexo es 'F'. 
#En caso de que se cumpla lo mismo, pero el sexo sea 'M', debe imprimir 'POSIBLE'. 
#Si no se cumplen dichas condiciones se debe mostrar 'NO ACEPTADA'.

num = int(input("Ingresa  nota: "))
num2 = int(input("Ingresa edad: "))
caracter = input("Ingrese el sexo (F o M): ").upper

if num2 > 18: 
    print("posible")
elif num2 < 18:
    print(f"no aceptad@")
