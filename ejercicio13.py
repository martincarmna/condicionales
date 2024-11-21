#Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba 
#el dí­a correspondiente. 
# Si introducimos otro número nos da un error.

dia = int(input("ingresa el dia de la semana (1-7): "))
if dia == 1:
    print("lunes")
elif dia == 2:
    print("martes")
elif dia ==3:
    print("miercoles")
elif dia == 4:
    print("jueves")
elif dia == 5:
    print("viernes")
elif dia == 6:
    print("sabado")
elif dia == 7:
    print("domingo")
else:
 print(f"Error: Ingrese otro dia")  
