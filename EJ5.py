import random
aleatorio = random.randint(0,9)
intentos=0
print("Adivina el numero entre 0 y 9 ")
while True: 
    num = int(input("Ingrese un numero entre 0 y 9"))
    intentos=intentos+1
    if num == aleatorio:
        print("Felicidades, adivinaste l numero")
        print("Cantidad de intentos:", intentos)
        break
    else:
        print("Incorrecto, intenta de nuevo")