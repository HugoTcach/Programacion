"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""

from statistics import mean


print("Calular la media de 100 numeros!!\n")
print("Ingresar 100 numeros, la aplicacion devolvera el promedio de los numeros ingresados")
list = []
for i in range(0,5):
    num = int(input("Ingrese un numero: "))
    list.append(num)

print(f"El promedio de los numeros ingresados es: {mean(list)}")