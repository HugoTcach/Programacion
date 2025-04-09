hemisferio = input("Ingrese en que hemisferio se encuentra (Norte o Sur) : ").lower()
mes = int(input("Ingrese que mes del año (formato mm): "))
dia = int(input("Ingrese que dia del año (formato dd): "))

if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
    if hemisferio == "norte":
        estacion = "Invierno"
    else:
        estacion = "Verano"
elif (dia >= 21 and mes == 3) or (mes <= 6 and dia <= 20):
    if hemisferio == "norte":
        estacion = "Primavera"
    else:
        estacion = "Otoño"
elif (dia >= 21 and mes == 6) or (mes <= 9 and dia <= 20):
    if hemisferio == "norte":
        estacion = "Verano"
    else:
        estacion = "Invierno"
else:
    if hemisferio == "norte":
        estacion = "Otoño"
    else:
        estacion = "Primavera"


print(f"Usted se encuentra en la estacion de {estacion}")
