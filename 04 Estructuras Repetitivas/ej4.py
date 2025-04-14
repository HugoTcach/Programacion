suma=0
print("Ingresa numeros enteros. Ingresa 0 para finalizar")
while True:
    numero=int(input("Ingresa un numero:"))
    if numero == 0:
        break
    suma += numero
print("La suma total es:", suma)