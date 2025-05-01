import math #Importo math para utilizar la constante PI y elevar al cuadrado el radio con la funcion: math.pow()

#definir funciones
def calcular_area_circulo(radio):
    area = round(math.pi * math.pow(radio, 2), 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = round(2 * math.pi * radio, 2)
    return perimetro

#Programa pricipal

radio = int(input("Ingrese el radio del circulo: "))

print(f"El area del circulo es: {calcular_area_circulo(radio)}")
print(f"El perimetro del circulo es: {calcular_perimetro_circulo(radio)}")