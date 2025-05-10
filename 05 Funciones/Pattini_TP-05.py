### Actividad 1

cont_a = True
list_a = []
while cont_a != 0:
    for i in range(0, 100 + 1, 4):
        if i % 4 == 0:
            num = i
            list_a.append(num)
    cont_a = False
print(list_a)

### Actividad 2

list_b = ["gatos", "helado", "juegos", "cine", "musica"]
list_b[3]

### Actividad 3

list_c = []
list_c.append("teclado")
list_c.append("mouse")
list_c.append("monitor")
print(list_c)

### Actividad 4

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"
print(animales)

### Actividad 5

## El programa elimina el valor mas alto, o máximo ("max"); e imprime el resultado final de la lista.

### Actividad 6

list_d = []
for i in range(10, 30 + 1, 5):
    if i < 20:
        num = i
        list_d.append(num)
    else:
        pass
print(list_d)

### Actividad 7

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = True
autos[2] = False
print(autos)

### Actividad 8

dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

### Actividad 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

### Actividad 10

lista_anidada = [[15], [True], [25.5, 57.9, 30.6], [False]]
print(lista_anidada)

# Interpreté de esta forma la consigna 10.