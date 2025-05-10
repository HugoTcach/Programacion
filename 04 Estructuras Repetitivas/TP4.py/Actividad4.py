#inicio el contador en 0
total = 0
#indico que pongan numeros hasta q apreten el 0 para sumarlos
while True:
    num = int(input("Ingresa varios numeros para sumarlos (0 para detener): "))
    if num == 0:
        break
    total += num
    #sumo el total
print(f"La suma total es: {total}")
