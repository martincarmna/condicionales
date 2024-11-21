# Juego Piedra Papel y Tijera
# Programa que lea las opciones de 2 jugadores, y muestra el resultado
# Empate, gana jugador 1 o gana jugador 2
# Si introducimos una opción que no coindica con piedra, papel o tijera
# Diga que opción Incorrecta

jugador1 = input("Ingresa (piedra,papel o tijera): ")
jugador2 = input("jugador2 ingresa (piedra,papel o tijera): ")

if jugador1 == "piedra" and jugador2 == "tijeras":
    print("jugador1 gana")
elif jugador1 == "tijeras" and jugador2 == "piedras":
    print("jugador2 gana")
elif jugador1 == "papel" and jugador2 == "piedra":
    print("jugador1 gana")
elif jugador1 == "piedra" and jugador2 == "papel":
    print("judador2 gana")
elif jugador1 == "papel" and jugador2 == "tijeras":
    print("jugador2 gana")
elif jugador1 == "tijeras" and jugador2 == "papel":
    print("jugador1 gana")
elif jugador1 == "papel" and jugador2 == "papel":
    print("empate")
elif jugador1 == "tijeras" and jugador2 == "tijeras":
    print("empate")
elif jugador1 == "piedra" and jugador2 == "piedra":
    print("empate")
else:
    print(f"error: ingrese (piedra,papel o tijeras)")
