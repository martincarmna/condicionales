#Escribe un programa que pida un número entero entre uno y doce e imprima el 
#número de días que tiene el mes correspondiente.
# Si introducimos otro número nos da un error.
# Solicitar al usuario que ingrese un número entero entre 1 y 12
mes = int(input("Ingresa un número entero entre 1 y 12: "))

if mes == 1:
    print("Enero tiene 31 días.")
elif mes == 2:
    print("Febrero tiene 28 o 29 días.")
elif mes == 3:
    print("Marzo tiene 31 días.")
elif mes == 4:
    print("Abril tiene 30 días.")
elif mes == 5:
    print("Mayo tiene 31 días.")
elif mes == 6:
    print("Junio tiene 30 días.")
elif mes == 7:
    print("Julio tiene 31 días.")
elif mes == 8:
    print("Agosto tiene 31 días.")
elif mes == 9:
    print("Septiembre tiene 30 días.")
elif mes == 10:
    print("Octubre tiene 31 días.")
elif mes == 11:
    print("Noviembre tiene 30 días.")
elif mes == 12:
    print("Diciembre tiene 31 días.")
else:
    print("Error: Debes ingresar un número entre 1 y 12.")
