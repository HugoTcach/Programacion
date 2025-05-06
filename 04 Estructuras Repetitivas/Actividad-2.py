#Le pide al usuario que ingrese un número.
numero = int(input("Ingrese un número entero: "))

num_original = numero  #Guarda el numero original para mostrar luego.

cont = 0    #Inicializa el contador en 0.

# Crea un ciclo while para iterar el número ingresado.
while numero > 0:
    numero //= 10     #En cada iteracion,elimina el ultimo digito dividiendo por 10,tomando solo la parte entera.
    cont += 1
print(f"La cantidad de digitos de {num_original} es: {cont}")#Imprime en pantalla el resultado.


