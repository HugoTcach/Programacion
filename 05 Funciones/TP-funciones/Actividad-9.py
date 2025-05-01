#Definir funciones

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

#Programa principal

grados_usuario = int(input("ingrese los grados celsius: "))

print(f"La conversion a grados Fahrentheit es: {celsius_a_fahrenheit(grados_usuario)}")