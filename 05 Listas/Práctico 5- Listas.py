# Práctico 5: Listas - UTN a Distancia

# Objetivo:
# Desarrollar la comprensión y la capacidad de manipular listas en Python
# mediante la aplicación de conceptos fundamentales como la indexación, la
# modificación de elementos, el uso de métodos integrados y el manejo de
# listas anidadas. [cite: 21]

# Resultados de aprendizaje:
# 1. Reconocer y aplicar correctamente la indexación y el slicing para acceder a elementos
# individuales o subconjuntos dentro de una lista. [cite: 22, 23, 24]
# 2. Utilizar los métodos básicos de listas para crear, modificar y gestionar estructuras de
# datos simples. [cite: 22, 23, 24]
# 3. Modificar listas mediante la actualización de valores y el manejo de listas anidadas,
# comprendiendo cómo acceder a datos en estructuras más complejas. [cite: 22, 23, 24]

# Actividades

# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range. [cite: 25]
multiplos_de_4 = list(range(4, 101, 4))
print("1) Lista de múltiplos de 4:", multiplos_de_4)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. [cite: 26, 27]
mi_lista = ["manzana", "banana", "cereza", "dátiles", "frambuesa"]
print("2) Penúltimo elemento:", mi_lista[-2])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. [cite: 28, 29, 30]
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print("3) Lista con palabras:", lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista "animales" con las palabras "loro" y "oso", respectivamente. [cite: 30, 31, 32]
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("4) Lista de animales modificada:", animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. [cite: 32, 33, 34]
# El programa identifica el número más grande dentro de la lista 'numeros' y lo elimina de la lista.
numeros_ej5 = [8, 15, 3, 22, 7]
numeros_ej5.remove(max(numeros_ej5))
print("5) Lista después de eliminar el máximo:", numeros_ej5)

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros. [cite: 34, 35]
numeros_saltos = list(range(10, 31, 5))
print("6) Dos primeros elementos:", numeros_saltos[:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista "autos" por dos nuevos valores cualesquiera. [cite: 35, 36]
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["corsa", "fiesta"]
print("7) Lista de autos modificada:", autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. [cite: 36, 37]
# Imprimir la lista resultante por pantalla.
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("8) Lista de dobles:", dobles)

# 9) Dada la lista "compras", cuyos elementos representan los productos comprados por diferentes clientes: [cite: 37, 38, 39]
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append. [cite: 37, 38, 39]
compras[2].append("jugo")
print("9a) Compras con jugo:", compras)

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. [cite: 37, 38, 39]
compras[1][1] = "tallarines"
print("9b) Compras con tallarines:", compras)

# c) Eliminar "pan" de la lista del primer cliente. [cite: 37, 38, 39]
compras[0].remove("pan")
print("9c) Compras sin pan:", compras)

# d) Imprimir la lista resultante por pantalla [cite: 37, 38, 39]
print("9d) Lista de compras final:", compras)

# 10) Elaborar una lista anidada llamada "lista_anidada" que contenga los siguientes elementos: [cite: 39, 40]
# Posición lista_anidada[0]: 15
# Posición lista_anidada[1]: True
# Posición lista_anidada[2][0]: 25.5
# Posición lista_anidada[2][1]: 57.9
# Posición lista_anidada[2][2]: 30.6
# Posición lista_anidada [3]: False
# Imprimir la lista resultante por pantalla.
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("10) Lista anidada:", lista_anidada)