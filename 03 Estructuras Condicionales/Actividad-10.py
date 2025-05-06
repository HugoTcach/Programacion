#Le pregunta al usuario en que hemisferio se encuentra,mes y dia.
hemisferio = input("Por favor indique,¿En que hemisferio se encuentra? (N/S): ").upper()
mes = int(input("Ahora,indique ¿En que mes se encuentra? (1-12):"))
dia = int(input("¿Que dia es?"))


#Verifico que el texto sea valido.
if hemisferio != "N" and hemisferio != "S":
    print("Hemisferio invalido.Utilice N(norte) o S(sur)")
else:
    #Con condicionales "if" y "elif" va verificando en que estacion del año se encuentra.
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        if hemisferio == "N":
            print("Estas en Invierno")
        else:
            print("Estas en Verano")
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        if hemisferio == "N":
            print("Estas en Primavera")
        else:
            print("Estas en Otoño")
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        if hemisferio == "N":
            print("Estas en Verano")
        else:
            print("Estas en Invierno")
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        if hemisferio == "N":
            print("Estas en Otoño")
        else:
            print("Estas en Primavera")
    else:
        print("Fecha invalida")

    