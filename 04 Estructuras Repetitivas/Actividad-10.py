#Le pide al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

#Invierte el número,primero lo convierte en cadena luego usando Slicing [::-1] Invierte la cadena.
numero_invertido = str(numero)[::-1]

print(f"Número invertido: {numero_invertido}")#Muestra el resultado en pantalla.