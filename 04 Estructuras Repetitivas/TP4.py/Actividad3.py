#solicito 2 numeros
inicio = int(input("Introduce el primer valor: "))
fin = int(input("Introduce el segundo valor: "))
#sumo todos los numeros entre esos 2 solicitados
suma = sum(range(inicio + 1, fin))
print(f"La suma de los números entre {inicio} y {fin} (excluyendo los límites) es: {suma}")
