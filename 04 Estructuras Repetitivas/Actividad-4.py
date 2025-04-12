#Le pide al usuario que ingrese un número.
numeros = int(input("Ingrese un número: "))

suma = 0   #Incializa la suma en 0

#Incializa un while con la condicion numeros != de 0
while numeros != 0: 
    suma += numeros  #Suma los números ingresados por el usuario.

    numeros = int(input("Ingrese otro número: ")) #Dentro del ciclo le pide al usuario que ingrese otro número.

print(f"La suma total de los números ingresados es: {suma}") #Imprime por pantalla el resultado.
