#Definir funcion

def tabla_multiplicar(numero):
    tabla = []     #Crea una lista vacia
    for i in range(1, 11):
        tabla.append(numero * i)   # tabla.append() para ir agregando los resultados al final de la lista.
    return tabla
numero = int(input("Ingrese un número: "))

print(tabla_multiplicar(numero))