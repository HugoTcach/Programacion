# 1)
num = 0
for num in range(101):
    print(num)
    
# 2)
num = input("Ingrese num")
cont = 0
for i in num:
    cont += 1

print(f"Tiene {cont} digitos")

# 3)
num = int(input("Ingrese numero 1"))
num2 = int(input("Ingrese numero 2"))
cont = 0

for i in range(num+1, num2):
    cont += i
    
print(cont)


# 4)
num = int(input("Ingrese num"))
cont = 0

while num != 0:
    cont += num
    num = int(input("Ingrese num"))
    
print(f"Total: {cont}")


# 5)
from random import randrange

random = randrange(10)
num = int(input("Ingrese un numero entre el 0 y 9"))
intentos = 1
while num != random:
    intentos += 1
    num = int(input("Ingrese un numero entre el 0 y 9"))
    
print(f"intentos: {intentos}")


# 6)
for i in range(100, -2, -2):
    print(i)
    
    
# 7)
num = int(input("Ingrese un num"))
cont = 0
for i in range(0, num + 1):
    cont += i

print(cont)



# 8)
cont = 0
numPares = 0
numImpares = 0
numPositivos = 0
numNegativos = 0
while cont < 100:
    cont += 1
    num = int(input("Ingrese 100 numeros"))
    if (num % 2 == 0) & (num > 0):
        numPares += 1
        numPositivos += 1
    elif (num % 2 == 1) & (num > 0):
        numImpares += 1
        numPositivos += 1
    else:
        numNegativos += 1
        
print(f"Positivos: {numPositivos}")
print(f"Negativos: {numNegativos}")
print(f"Pares: {numPares}")
print(f"Impares: {numImpares}")



# 9)
num = int(input("Ingrese un num"))
cont = 0
suma = 0
media = 0

while cont < 100:
    suma += num
    num = int(input("Ingrese un num"))
    cont += 1

media = suma/100
print(f"La media es: {media}")




# 10)
n = input("Ingrese valor")
num = n[::-1]
print(num)