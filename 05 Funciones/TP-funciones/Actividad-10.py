#Definir funciones

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

#Programa principal

n_1 = int(input("Ingrese el primer número: "))
n_2 = int(input("Ingrese el segundo número: "))
n_3 = int(input("Ingrese el tercer número: "))

print(f"El promedio de los 3 números ingresados es: {calcular_promedio(n_1, n_2, n_3)}")