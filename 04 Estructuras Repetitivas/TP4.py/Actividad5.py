#importo libreria random
import random
#incio variables
numero_aleatorio = random.randint(0, 9)
intentos = 0
acertado = False
#solicito al usuario un numero
while not acertado:
    intento = int(input("Adivina un número entre 0 y 9: "))
    intentos += 1
    if intento == numero_aleatorio:
        acertado = True
        print(f"¡Correcto! El número era {numero_aleatorio}. Necesitaste {intentos} intentos.")
    else:
        #indico que siga intentando
        print("Intenta de nuevo.")
