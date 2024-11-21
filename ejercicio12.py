#Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
#al lanzar un dado de seis caras y muestre por pantalla el número en letras 
#(dato cadena) de la cara opuesta al resultado obtenido.
#* Nota 1: En las caras opuestas de un dado de seis caras están los números: 
#1-6, 2-5 y 3-4.
#* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
#se mostrará el mensaje: "ERROR: número incorrecto.".
# Solicitar al usuario que ingrese el resultado del lanzamiento de un dado de seis caras
resultado = int(input("Ingresa el resultado del lanzamiento del dado (1-6): "))


numeros_en_letras = {
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis"
}

if resultado < 1 or resultado > 6:
    print("ERROR: número incorrecto.")
else:
    if resultado == 1:
        opuesto = 6
    elif resultado == 2:
        opuesto = 5
    elif resultado == 3:
        opuesto = 4
    elif resultado == 4:
        opuesto = 3
    elif resultado == 5:
        opuesto = 2
    elif resultado == 6:
        opuesto = 1
    
    print(f"La cara opuesta a {numeros_en_letras[resultado]} es {numeros_en_letras[opuesto]}.")



