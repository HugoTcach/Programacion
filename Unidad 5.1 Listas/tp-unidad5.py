#1)
multiplos_de_4 = list(range(4, 101, 4))
print(multiplos_de_4)

#2)
lista = [3,2,43,"Hola",True,2.3]
print(lista[-2])

#3)
palabras = []
palabras.append("Hola")
palabras.append("Mundo")
palabras.append("!")
print(palabras)

#4)
animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#5)
# Lo que realiza el programa es primero definir una lista de numeros, luego llama a la funcion
#.remove() para remover un numero y como parametro de la funcion llama a la funcion max()
#que recorre la lista num para devolver el valor mal alto, para finalmente tomarlo como parametro
#de la funcoion remove y quitarlo de la lista, dejando de los 5 elementos originales, solo los 4 mas chicos

elementos = list(range(10, 31, 5))
print(elementos[0:2])

#7)
autos = ["sedan", "polo", "suran", "gol"]
print(autos)
autos[1] = "fit"
autos[-2] = "civic"
print(autos)

#8)
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#9)
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
print(compras)
compras[2].append("jugo")
compras[1][1] = "tallarins"
compras[0].remove("pan")
print(compras)

#10)
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)