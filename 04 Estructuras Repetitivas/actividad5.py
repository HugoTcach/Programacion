"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""
from random import randint

print("Intenta adividar el numero aleatorio!")
userNum = int(input("Ingrese un numero entero entre 0 y 9: "))
randomNum = randint(0,9)
intentos = 1
while userNum != randomNum:
    userNum = int(input("Numero incorrecto, intente nuevamente!: "))
    intentos += 1

print(f"Numero ADIVINADO!!!\nIntentos necesarios: {intentos}")

