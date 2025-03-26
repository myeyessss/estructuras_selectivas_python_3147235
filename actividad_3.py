Contrato = (input("Que cargo ocupas (A/B/C/D) "))
Salario_neto = 0

if Contrato == "A":
    print ("A. Contrato a termino indefinido")
elif Contrato == "B":
        print ("B. Contrato por prestacion de serviicios")
elif Contrato == "C":
        print ("C. Contrato Aprendizaje")
        salario_minimo = int(input("Ingrese el valor de el salario minimo: "))
        Salario_neto = salario_minimo - (salario_minimo * 0.25)
elif Contrato == "D":
        print ("D. Contrato por Jornal")
Horas = int(input("Ingresa el numero de horas: "))
ValorxHora = int(input("Ingresa tu pago por hora: "))
Salario_neto = Horas * ValorxHora
print ("Tu salario es: ", Salario_neto)

