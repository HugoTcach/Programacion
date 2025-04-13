num1=int(input("Ingrese el primer numero:"))
num2=int(input("Ingrese el segundo numero:"))
if num1 > num2:
    mayor=num1
    menor=num2
else: 
    mayor=num2
    menor=num1
suma=0
contador=mayor-1
while contador>menor:
    suma=suma+contador 
    contador=contador-1
print("La suma es:", suma )