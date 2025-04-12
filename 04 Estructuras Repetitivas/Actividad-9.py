#Inicializo las variables en 0
cant_numeros = 10
suma = 0
media = 0
#Inicializa el ciclo desde la vuelta 1 y no se la vuelta 0 como es comunmente.
for x in range(1,cant_numeros + 1):

    numeros = int(input(f"Número {x}: ")) #Le muestra la iteracion en la que esta.
    suma += numeros   #Calcula la suma.
    
media = suma / cant_numeros #Calcula la media.
print(f"La media de estos {cant_numeros} números es: {media}") #Muestra en pantalla el resultado.