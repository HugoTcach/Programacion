import random

numero_secreto = random.randint(0,9) #Crea un número random entre 0 y 9.
intentos = 1 #Incializa el contador de intentos en 1

print("Adivina el número entre 0 y 9..")
intento = int(input("Número: "))

#Si el intento es distinto del número random entra al while y ejecuta.
while intento != numero_secreto : 
    intento = int(input("Número: "))
    intentos += 1   #Va sumando la cantidad de intentos.

if intento == numero_secreto:  #Si  adivina el número,muestra en pantalla el resultado con los intentos.
        print(f"Adivinaste el número en {intentos} intentos!")

