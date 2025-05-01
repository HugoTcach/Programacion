#Definir funciones

def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir entre 0"
    return(suma, resta, multiplicacion, division)

#Programa  principal

primer_numero = int(input("Ingrese el primer número por favor: "))
segundo_numero = int(input("Ingrese el segundo número por favor: "))

resultado = operaciones_basicas(primer_numero, segundo_numero)

print("Resultados:")
print(f"Suma: {resultado[0]}")
print(f"Resta: {resultado[1]}")
print(f"Multiplicación: {resultado[2]}")
print(f"División: {resultado[3]}")