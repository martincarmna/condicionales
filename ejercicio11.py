#La política de cobro de una compañía telefónica es: cuando se realiza una 
#llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
#cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
#los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
#de mañana, 15 %, y en turno de tarde, 10 %. 
#Realice un programa para determinar cuánto debe pagar por cada concepto 
#una persona que realiza una llamada.

llamada = int(input("Ingrese la duracion de la llamada: "))
turno = input("Ingrese el turno: ").upper ()
dia = input("Ingrese el dia: ").upper ()

if llamada >= 5:
    costo = llamada * 1.00
elif llamada >= 8:
    costo = llamada * 0.8
elif llamada >= 10:
    costo = llamada * 0.7
elif llamada >= 15:
    costo = llamada * 0.5

if llamada == "domingo":
    impuesto = 0.03
elif turno == "mañana":
    impuesto = 0.15
else:
    impuesto = 0.10

    costo_total = costo * (1 + impuesto)

print(f"costo de la llamada sin impuestos: {costo }")
print(f"impuesto aplicado: {impuesto * 100}%")
print(f"costo total de la llamada: ",costo_total)

