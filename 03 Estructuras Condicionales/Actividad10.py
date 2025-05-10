# Solicitar datos al usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ")
mes = input("¿Qué mes es? (ej: marzo): ")
dia = int(input("¿Qué día es?: "))

# Determinar estación según hemisferio
estacion = ""

if hemisferio == "N":
    if (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia <= 20):
        estacion = "Invierno"
    elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
        estacion = "Primavera"
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
        estacion = "Verano"
    elif (mes == "septiembre" and dia >= 21) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia <= 20):
        estacion = "Verano"
    elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
        estacion = "Otoño"
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 20):
        estacion = "Invierno"
    elif (mes == "septiembre" and dia >= 21) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):
        estacion = "Primavera"

# Mostrar resultado
if estacion:
    print(f"Estás en {estacion}.")