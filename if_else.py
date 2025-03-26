edad = int(input("Ingrese su edad: "))
documento = input("Tiene documento di/do: ")
if edad >= 18 and documento == "di":
    print ("Ud es mayor de edad")
    print ("Puede votar")
else:
    print("Ud es menor de edad")
    print("o")
    print("No puede votar")
print("Fin del programa")