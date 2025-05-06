#Le pide al usuario que ingrese un número
numero = int(input("Ingrese un número positivo entero: "))
if numero > 0: #Verifica que el número sea positivo.
    suma = 0   #Inicializa la suma en 0.

    for x in range(numero + 1):  
        suma += x  #En cada iteracion suma los números que estan dentro del rango.
    print(suma)  #Muestra el resultado.
else:
    print("El número debe ser positivo")
