#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

texto = input("Ingresa un texto: ")
if texto == texto.upper():
    print("El texto es mayuscula")
else:
    print(f"el texto es miniscula")
