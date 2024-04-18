hora = float(input("quanto voce ganha por hora?:"))
hora_mes = float(input("quantas hora trabalhadas no mes?:"))

total_mes = hora * hora_mes

i = 0

while i < (i+1):

    print("\n\nDigite 1 Para saber seu salario")
    print("Digite 2 Para saber o desconto imposto de renda ")
    print("Digite 3 Para saber o desconto sindicato")
    print("Digite 4 Para saber o desconto INSS")
    print("Digite 5 Para saber seu salario liquido")
    print("Digite 6 Para saber o seu décimo terceiro")
    print("Digite 7 para cancelar\n\n")

    digito = int(input("Digite um número:"))



    if digito == 1:
        print("\nseu salario mensal é de:", total_mes)

        print("\n\nDigite 1 finalizar")
        print("Digite 2 para continuar\n\n")

        digito = int(input("Digite um número:"))

        if digito == 1:
            break
        elif digito == 2:
            i+=i
        else:
            print("\nNúmero inválido Digitado \n\n")
            break
        



    elif digito == 2:
        des_imp = total_mes * 0.11

        print("\ndesconto imposto de renda:", des_imp)
        
        print("\n\nDigite 1 finalizar")
        print("Digite 2 para continuar\n\n")

        digito = int(input("Digite um número:"))

        if digito == 1:
            break
        elif digito == 2:
            i+=i
        else:
            print("\nNúmero inválido Digitado \n\n")
            break



    elif digito == 3:
        sind = total_mes * 0.05

        print("\ndesconto sindicato:", sind)

        print("\n\nDigite 1 finalizar")
        print("Digite 2 para continuar\n\n")

        digito = int(input("Digite um número:"))

        if digito == 1:
            break
        elif digito == 2:
            i+=i
        else:
            print("\nNúmero inválido Digitado \n\n")
            break



    elif digito == 4:
        des_inss = total_mes * 0.08

        print("\ndesconto INSS:", des_inss)

        print("\n\nDigite 1 finalizar")
        print("Digite 2 para continuar\n\n")

        digito = int(input("Digite um número:"))

        if digito == 1:
            break
        elif digito == 2:
            i+=i
        else:
            print("\nNúmero inválido Digitado \n\n")
            break




    elif digito == 5:
        des_imp = total_mes * 0.11
        sind = total_mes * 0.05
        des_inss = total_mes * 0.08

        liquido = total_mes - des_imp - des_inss - sind

        print("\nseu salario liquido no mes será de:", liquido)

        print("\n\nDigite 1 finalizar")
        print("Digite 2 para continuar\n\n")

        digito = int(input("Digite um número:"))

        if digito == 1:
            break
        elif digito == 2:
            i+=i
        else:
            print("\nNúmero inválido Digitado \n\n")
            break




    elif digito == 6:
        des_imp = total_mes * 0.11
        sind = total_mes * 0.05
        des_inss = total_mes * 0.08

        liquido = total_mes - des_imp - des_inss - sind

        decimo_terceiro = liquido + total_mes

        print ("\no seu décimo terceiro sera de:", decimo_terceiro)

        print("\n\nDigite 1 finalizar")
        print("Digite 2 para continuar\n\n")

        digito = int(input("Digite um número:"))

        if digito == 1:
            break
        elif digito == 2:
            i+=i
        else:
            print("\nNúmero inválido Digitado \n\n")
            break



    elif digito == 7 :
        break




    else:
        print("\nNúmero inválido Digitado \n\n")
        break
