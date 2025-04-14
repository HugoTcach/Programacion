num=int(input("Ingresa un numero:"))
i=0
while num > 0:
    num = num // 10
    i = i + 1
print(f"El numero tiene {i} digitos")
