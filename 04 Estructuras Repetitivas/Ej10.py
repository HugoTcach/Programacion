num=int(input("Ingresa un numero:"))
num_original=abs(num)
num_invertido=0
while num_original > 0:
    digito = num_original % 10
    num_invertido = num_invertido * 10 + digito
    num_original = num_original // 10
if num < 0:
    num_invertido = num_invertido * -1
print("Numero invertido:", num_invertido)