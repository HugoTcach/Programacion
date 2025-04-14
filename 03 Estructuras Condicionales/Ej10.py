#Pedir al usuario los datos
hemisferio=input("¿En que hemisferio se encuentra, n o s? ")
mes=int(input("¿En que mes del año? (1-12)"))
dia=int(input("¿Que dia es? (1-31)"))
if (mes== 12 and dia >= 21) or (mes == 1) or (mes== 2) or (mes == 3 and dia <= 20):
   if hemisferio == "n":
      print("La estacion del año es Invierno")
   else:
      print("La estacion del año es Verano ")
elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
   if hemisferio == "n":
      print("La estacion del año es Primavera")
   else:
      print("La estacion del año es Otoño")
elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
   if hemisferio == "n":
      print("La estacion del año es Verano")
   else:
      print("La estacion del año es Invierno")
elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20 ):
   if hemisferio == "n":
      print("La estacion del año es Otoño")
   else:
      print("La estacion del año es Primavera")

                
