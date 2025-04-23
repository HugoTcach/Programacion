#TP LISTAS Díaz_Monroy_Yohanna 
#Práctico 5: Listas - PROGRAMACION 1 - UTN  
#Programacion a Distancia

#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

multiplos = list(range(4, 101, 4))
print(multiplos)

print ################################


#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!

lista = ["codigo", 2, 3.5,False , True]

posicion_3_lista = lista[3]

print(posicion_3_lista)
print(type(posicion_3_lista))

print ########################

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Porejemplo:lista_vacia = []

notas = []
notas.append("False1")
notas.append("False2")
notas.append("False3")

print (notas)

print ###########################

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]

animales = ["cocodrilo", "jirafa","pato","rana" ,"perro","gato ", "conejo"]
animales[2] = "loro"
animales[6] = "oso"
print (animales)

print ###########################

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8,15,3,22,7]
numeros.remove(max(numeros))
print (numeros)
# el programa remueve el numero de mayor valor de la lista .


print#####################################

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#pantalla los dos primeros.

lista_saltos_cinco = list(range(10, 31, 5))
print(lista_saltos_cinco)


print ######################################


#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
#autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"]

# Reemplazamos los valores en los índices 1 y 2
autos[1] = "toyota"
autos[2] = "dodge"


print ####################################


#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print (dobles)

print #############################################

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
if "fideos" in compras[1]:
    indice_fideos = compras[1].index("fideos")
    compras[1][indice_fideos] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
if "pan" in compras[0]:
    compras[0].remove("pan")

print (compras)

print ###############################

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.


lista_anidada = [15,["True"],[25.5,57.9,30.6],["false"]]
print(lista_anidada)


print##########################################
