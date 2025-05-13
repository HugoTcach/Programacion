# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función 
# range. 

# multiples_de_4 = list(range(4, 101, 4))
# print(multiples_de_4)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el 
# penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
# indexing con números negativos! 

# mi_lista = ["libros", "música", "viajes", "programación", "café"]

# penultimo_positivo = mi_lista[3]
# print("Penúltimo elemento (indexación positiva):", penultimo_positivo)

# penultimo_negativo = mi_lista[-2]
# print("Penúltimo elemento (indexación negativa):", penultimo_negativo)

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por 
# pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por 
# ejemplo: 
# lista_vacia = [] 

# lista_vacia = [] 
# lista_vacia.append("python")
# lista_vacia.append("programación")
# lista_vacia.append("aprendizaje")
# print("lista_vacia: ", lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, 
# respectivamente.  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra 
# en los videos o bien investigar cómo funciona el indexing con números negativos! 
# animales = ["perro", "gato", "conejo", "pez"] 

# animales = ["perro", "gato", "conejo", "pez"] 
# print("Lista original ==> ", animales)

# animales[1]="loro"
# animales[3]="oso"

# print("Lista modificada con indexing positivo ==> ", animales)

# animales[-3] = "loro"  
# animales[-1] = "oso"   
# print("Lista modificada con indexing negativo ==> ", animales)

# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print(numeros)

# Se crea una lista con los elementos [8, 15, 3, 22, 7], luego a la lista numeros se le invoca ael metodo 'remove' para eliminar el elemento maximo calculado dentro del remove
# y finalmente se imprime por consola la lista numeros

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por 
# pantalla los dos primeros. 

# numeros = list(range(10 ,31 ,5))
# print("Lista completa:", numeros)

# print("Dos primeros elementos:", numeros[:2]) 

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores 
# cualesquiera. 
# autos = ["sedan", "polo", "suran", "gol"] 

# autos = ["sedan", "polo", "suran", "gol"] 
# print("Lista orgininal: ", autos)

# autos[1] = "ford"
# autos[2] = "chevrolet"
# print("Lista modificada por indexación positiva: ", autos)

# autos = ["sedan", "polo", "suran", "gol"]
# autos[1:3] = ["ford", "chevrolet"]  
# print("Lista modificada usando slicing: ", autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append 
# directamente. Imprimir la lista resultante por pantalla. 

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por 
# diferentes clientes: 
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
# a) Agregar "jugo" a la lista del tercer cliente usando append. 
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
# c) Eliminar "pan" de la lista del primer cliente.  
# d) Imprimir la lista resultante por pantalla 

# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 

# # a) Agregar "jugo" a la lista del tercer cliente usando append. 
# compras[2].append("jugo")
# print("Inciso a) ",compras)

# # b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente. 
# indice_fideos = compras[1].index("fideos")
# compras[1][indice_fideos] = "tallarines"
# print("Inciso b) ",compras)

# # c) Eliminar "pan" de la lista del primer cliente.  
# compras[0].remove("pan")
# print("Inciso c) ",compras)

# # d) Imprimir la lista resultante por pantalla 
# print("Inciso d) ",compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
# ● Posición lista_anidada[0]: 15 
# ● Posición lista_anidada[1]: True 
# ● Posición lista_anidada[2][0]: 25.5 
# ● Posición lista_anidada[2][1]: 57.9 
# ● Posición lista_anidada[2][2]: 30.6 
# ● Posición lista_anidada[3]: False 
# Imprimir la lista resultante por pantalla.

lista_anidada = [15, True]
print("primera parte: " ,lista_anidada)

lista2 = [25.5, 57.9, 30.6]
print("Lista para concatenar: ",lista2)

lista_anidada=lista_anidada+[lista2]
print("Lista concatenada: ",lista_anidada)

lista_anidada.append(False)
print("agrego el ultimo elemento: ", lista_anidada)