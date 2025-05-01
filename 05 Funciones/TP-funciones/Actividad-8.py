import math
#Definir funciones

def calcular_imc(peso, altura):
    imc = round(peso / math.pow(altura, 2),2)
    return imc

#Programa principal

peso_usuario = float(input("ingrese su peso en Kilogramos: "))
altura_usuario = float(input("Ingrese su altura en metros: "))

print(f"Su indice de masa corporal es: {calcular_imc(peso_usuario, altura_usuario)}")