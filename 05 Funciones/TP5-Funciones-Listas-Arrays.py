#Ejercicio 1: Lista de múltiplos de 4
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#Ejercicio 2: Penúltimo elemento
cosas_que_me_gustan = ["pizza", "música", "viajar", "películas", "gatos"]
print(cosas_que_me_gustan[-2])

#Ejercicio 3: Agregar palabras con append
lista_vacia = []
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")
print(lista_vacia)

#Ejercicio 4: Reemplazar segundo y último valor
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#Ejercicio 5: Analizar el código y explicar
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
#Este código remueve el número de mayor valor de la lista, usando max para encontrarlo y remove para eliminarlo.

#Ejercicio 6: Números del 10 al 30, con saltos de 5
numeros_saltando = list(range(10, 31, 5))
print(numeros_saltando[:2])

#Ejercicio 7: Reemplazar los dos valores centrales
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["civic", "corolla"]
print(autos)

#Ejercicio 8: Lista de dobles con append
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

#Ejercicio 9: Lista de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines"
compras[1][1] = "tallarines"

# c) Eliminar "pan" del primer cliente
compras[0].remove("pan")

print(compras)

#Ejercicio 10: Lista anidada
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print(lista_anidada)