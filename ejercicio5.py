# Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
# sino se da un error.

usuario = input("Ingrese el usuario: ")
contraseña = input("Ingrese la contraseña: ")

if usuario == "pepe" and contraseña == "asdsd":
    print("Has entrado al sistema ._.")
else:
    print(f"Error: Al ingresar usuario y contraseña.")
