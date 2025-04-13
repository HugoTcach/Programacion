cantidad=100
suma=0
print("Ingresa 100 numeros enteros:")
for i in range(cantidad):
    numero=int(input(f"Numero {i+1}:"))
    suma=numero+1
media=suma/cantidad
print("La media de los 100 numeros ingresados es:", media)