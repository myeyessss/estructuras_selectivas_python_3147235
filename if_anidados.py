edad = int(input("Ingrese su edad: "))
if edad >= 18:
    documento = input ("TIene documento? (si/no)")
    if documento == "si":
        print("sapo")
    else:
        print ("doble sapo")
else: 
    print("No puede votar, es menor de edad")