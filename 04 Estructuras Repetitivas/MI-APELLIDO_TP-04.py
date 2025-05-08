#for x in range(1,11,2):
#    print(f"{x}")

#umbral = 10
#sumatoria = 0
#cont = 0

#while sumatoria < umbral:
#    cont += 1
#    num = int(input("Ingrese un numero: "))
#    sumatoria += num
    

#print("El primedio es",(sumatoria / cont))

#cant_numeros = 5
#sumatoria = 0

#for cont in range(1,cant_numeros+1):
#    print("Ingrese numero",cont)
#    num = int(input())
#    sumatoria += num
#    print()

#print("La sumatoria de los valores es",sumatoria)
#print("El primedio",(sumatoria/cant_numeros))

#sueldoAnual = 0

#for contMeses in range(1,13):
#    print("Ingrese su sueldo para el mes n°",contMeses)
#    sueldoMensual = int(input())
#    sueldoAnual+= sueldoMensual

#print("Su sueldo anual es" ,sueldoAnual)

#max_numero = float("-inf")
#min_numero = float("inf")
#pos_max = -1
#pos_min = -1

#for cont in range(1,5):
#    print("Ingrese numero",(cont))
#    num = int(input())
#    if num > max_numero:
#        max_numero = num
#        pos_max = cont
#    if num < min_numero:
#        min_numero = num 
#        pos_min = cont
    
#print("El maximo es",max_numero)
#print("El minimo es",min_numero)
#print("Posicion maxima es",pos_max)
#print("Posicion minima es",pos_min)

#numero = int(input("Ingrese un numero positivo: "))

#if numero > 0:
#    if numero % 2 != 0:
#       numero = numero - 1
#    cont = numero
#    while cont >= 0:
#        print(str(cont) + " ", end="")
#        cont = cont -2

#else:
#    print("El numero no es positivo")

#corte = "*"
#nombre_invalido = "XXXXXXXXXX"
#edad_min = float("inf")
#nombre_mas_joven = nombre_invalido

#nombre = input(f"Ingrese nombre({ corte } para cortar): ")

#while nombre != corte:
#    edad = int(input(f"Ingrese la edad de {nombre}: "))
#    if edad < edad_min:
#        edad_min = edad
#        nombre_mas_joven = nombre
#    nombre = input("Ingrese otro nombre("+ corte +" para cortar): ")

#if nombre_mas_joven == nombre_invalido:
#    print("No se ingresaron nombre")
#else:
#    print(f"La persona mas joven de {edad} años es {nombre_mas_joven}" )

#numero = int(input("Ingrese un numero entre 1 y 10: "))

#if numero >=1 and numero <=10:
#    for cont in range(1,11):
#        print(f"{numero} x {cont} = {numero * cont}" )
#else:
#    print("No ingresaste un numero de 1 a 10")

cant_personas = int(input("Ingrese una cantidad de persona: "))
edad_minima = 18
cant_personas_mayores = 0

for cont in range(1,cant_personas+1):
    print(f"Ingrese la edad n° {cont}")
    edad = int(input()) 
    if edad >= edad_minima:
        cant_personas_mayores += 1

porc = (cant_personas_mayores/cant_personas) * 100 
print(f"El porcentaje de personas mayores de edad es {porc}%")
