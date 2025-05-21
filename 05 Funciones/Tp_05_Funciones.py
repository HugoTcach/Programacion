import math

# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”.
def imprimir_hola_mundo():
    """Imprime el mensaje 'Hola Mundo!'."""
    print("Hola Mundo!")

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
def saludar_usuario(nombre):
    """
    Recibe un nombre y devuelve un saludo personalizado.

    Args:
        nombre (str): El nombre del usuario.

    Returns:
        str: Un saludo personalizado.
    """
    return f"Hola {nombre}!"

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia)
def informacion_personal(nombre, apellido, edad, residencia):
    """
    Recibe datos personales e imprime una cadena con esa información.

    Args:
        nombre (str): El nombre de la persona.
        apellido (str): El apellido de la persona.
        edad (int): La edad de la persona.
        residencia (str): La ciudad de residencia de la persona.
    """
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4. Crear dos funciones: calcular_area_circulo(radio) y calcular_perimetro_circulo(radio)
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Args:
        radio (float): El radio del círculo.

    Returns:
        float: El área del círculo.
    """
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    """
    Calcula el perímetro de un círculo dado su radio.

    Args:
        radio (float): El radio del círculo.

    Returns:
        float: El perímetro del círculo.
    """
    return 2 * math.pi * radio

# 5. Crear una función llamada segundos_a_horas(segundos)
def segundos_a_horas(segundos):
    """
    Convierte una cantidad de segundos a horas.

    Args:
        segundos (int): La cantidad de segundos.

    Returns:
        float: La cantidad de horas.
    """
    return segundos / 3600

# 6. Crear una función llamada tabla_multiplicar(numero)
def tabla_multiplicar(numero):
    """
    Imprime la tabla de multiplicar de un número del 1 al 10.

    Args:
        numero (int): El número del cual se imprimirá la tabla.
    """
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Crear una función llamada operaciones_basicas(a, b)
def operaciones_basicas(a, b):
    """
    Realiza operaciones básicas (suma, resta, multiplicación, división) con dos números.

    Args:
        a (float): El primer número.
        b (float): El segundo número.

    Returns:
        tuple: Una tupla con los resultados (suma, resta, multiplicación, división).
               La división será None si el divisor es 0.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = None
    if b != 0:
        division = a / b
    return (suma, resta, multiplicacion, division)

# 8. Crear una función llamada calcular_imc(peso, altura)
def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).

    Args:
        peso (float): Peso en kilogramos.
        altura (float): Altura en metros.

    Returns:
        float: El valor del IMC.
    """
    if altura <= 0:
        return 0.0 # Evitar división por cero o altura inválida
    return peso / (altura ** 2)

# 9. Crear una función llamada celsius_a_fahrenheit(celsius)
def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.

    Args:
        celsius (float): Temperatura en grados Celsius.

    Returns:
        float: Temperatura equivalente en Fahrenheit.
    """
    return (celsius * 9/5) + 32

# 10. Crear una función llamada calcular_promedio(a, b, c)
def calcular_promedio(a, b, c):
    """
    Calcula el promedio de tres números.

    Args:
        a (float): El primer número.
        b (float): El segundo número.
        c (float): El tercer número.

    Returns:
        float: El promedio de los tres números.
    """
    return (a + b + c) / 3

# --- Programa Principal ---
if __name__ == "__main__":
    print("--- Actividad 1: Hola Mundo ---")
    imprimir_hola_mundo()
    print("-" * 30)

    print("--- Actividad 2: Saludo Personalizado ---")
    nombre_usuario = input("Ingresa tu nombre para un saludo personalizado: ")
    print(saludar_usuario(nombre_usuario))
    print("-" * 30)

    print("--- Actividad 3: Información Personal ---")
    nom = input("Ingresa tu nombre: ")
    ape = input("Ingresa tu apellido: ")
    eda = int(input("Ingresa tu edad: "))
    resi = input("Ingresa tu residencia: ")
    informacion_personal(nom, ape, eda, resi)
    print("-" * 30)

    print("--- Actividad 4: Área y Perímetro del Círculo ---")
    radio_circulo = float(input("Ingresa el radio del círculo: "))
    area = calcular_area_circulo(radio_circulo)
    perimetro = calcular_perimetro_circulo(radio_circulo)
    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")
    print("-" * 30)

    print("--- Actividad 5: Segundos a Horas ---")
    segundos_input = int(input("Ingresa una cantidad de segundos: "))
    horas_resultado = segundos_a_horas(segundos_input)
    print(f"{segundos_input} segundos equivalen a {horas_resultado:.2f} horas.")
    print("-" * 30)

    print("--- Actividad 6: Tabla de Multiplicar ---")
    num_tabla = int(input("Ingresa un número para ver su tabla de multiplicar (1 al 10): "))
    tabla_multiplicar(num_tabla)
    print("-" * 30)

    print("--- Actividad 7: Operaciones Básicas ---")
    num1_op = float(input("Ingresa el primer número para operaciones: "))
    num2_op = float(input("Ingresa el segundo número para operaciones: "))
    resultados_op = operaciones_basicas(num1_op, num2_op)
    print(f"Suma: {resultados_op[0]}")
    print(f"Resta: {resultados_op[1]}")
    print(f"Multiplicación: {resultados_op[2]}")
    if resultados_op[3] is not None:
        print(f"División: {resultados_op[3]:.2f}")
    else:
        print("División: No se puede dividir por cero.")
    print("-" * 30)

    print("--- Actividad 8: Cálculo de IMC ---")
    peso_imc = float(input("Ingresa tu peso en kilogramos: "))
    altura_imc = float(input("Ingresa tu altura en metros: "))
    imc_calculado = calcular_imc(peso_imc, altura_imc)
    print(f"Tu Índice de Masa Corporal (IMC) es: {imc_calculado:.2f}")
    print("-" * 30)

    print("--- Actividad 9: Celsius a Fahrenheit ---")
    celsius_input = float(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit_resultado = celsius_a_fahrenheit(celsius_input)
    print(f"{celsius_input}°C equivalen a {fahrenheit_resultado:.2f}°F.")
    print("-" * 30)

    print("--- Actividad 10: Calcular Promedio ---")
    p_num1 = float(input("Ingresa el primer número para el promedio: "))
    p_num2 = float(input("Ingresa el segundo número para el promedio: "))
    p_num3 = float(input("Ingresa el tercer número para el promedio: "))
    promedio_calculado = calcular_promedio(p_num1, p_num2, p_num3)
    print(f"El promedio de los tres números es: {promedio_calculado:.2f}")
    print("-" * 30)