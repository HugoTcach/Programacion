
# Ejercicio 1:
# Crear una lista con los numeros del 1 al 100 que sean multiplos de 4. Utilizar la funcion range.
lista_multiplos_4 = list(range(4, 101, 4))
print("Ejercicio 1:", lista_multiplos_4)

# Ejercicio 2:
# Crear una lista con cinco elementos (a eleccion) y mostrar el penultimo.
gustos = ['pizza', 'musica', 'cine', 'futbol', 'helado']
print("Ejercicio 2:", gustos[-2])  # Indice -2 accede al penultimo elemento

# Ejercicio 3:
# Crear una lista vacia, agregar tres palabras con append e imprimir la lista.
lista_vacia = []
lista_vacia.append('sol')
lista_vacia.append('luna')
lista_vacia.append('estrella')
print("Ejercicio 3:", lista_vacia)

# Ejercicio 4:
# Reemplazar el segundo y ultimo valor de la lista "animales" por 'loro' y 'oso'.
animales = ['perro', 'gato', 'conejo', 'pez']
animales[1] = 'loro'      # Reemplaza segundo elemento (indice 1)
animales[-1] = 'oso'      # Reemplaza ultimo elemento
print("Ejercicio 4:", animales)

# Ejercicio 5:
#En el siguiente programa se crea una lista llamada numeros con valores enteros y se busca eliminar el valor maximo.
numeros = [8, 15, 3, 22, 7] #lista con valores enteros  
numeros.remove(max(numeros)) #se busca eliminar el valor maximo, en este caso seria 22
print(numeros) #Se muestra por pantalla como quedaria la lista despues de eliminar el numero maximo.
      
# Ejercicio 6:
# Crear una lista con numeros del 10 al 30 (incluido), haciendo saltos de 5 en 5.
# Mostrar por pantalla los dos primeros.
lista_saltos = list(range(10, 31, 5))
print("Ejercicio 6:", lista_saltos[:2])  # Muestra los dos primeros elementos

# Ejercicio 7:
# Reemplazar los valores centrales de la lista "autos" por dos nuevos valores.
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["mustang", "camaro"]  # Reemplaza los elementos en indices 1 y 2
print("Ejercicio 7:", autos)

# Ejercicio 8:
# Crear una lista vacia llamada "dobles" y agregar el doble de 5, 10 y 15 usando append.
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Ejercicio 8:", dobles)

# Ejercicio 9:
# Modificar la lista de compras de diferentes clientes.
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")              # a) Agregar "jugo" al tercer cliente
compras[1][1] = "tallarines"           # b) Reemplazar "fideos" por "tallarines"
compras[0].remove("pan")               # c) Eliminar "pan" del primer cliente
print("Ejercicio 9:", compras)

# Ejercicio 10:
# Crear una lista anidada con valores especificos en cada posicion.
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print("Ejercicio 10:", lista_anidada)




