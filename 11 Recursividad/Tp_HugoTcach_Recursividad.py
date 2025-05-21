import math

# Ejercicio 1: Factorial de un número
def factorial(n): # [cite: 5]
    """
    Calcula el factorial de un número de forma recursiva.
    Args:
        n (int): El número entero no negativo.
    Returns:
        int: El factorial de n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def calcular_factoriales_hasta_n():
    """
    Solicita un número al usuario y muestra el factorial de todos los números
    enteros entre 1 y ese número.
    """
    try:
        num_usuario = int(input("Ingrese un número entero positivo para calcular sus factoriales: "))
        if num_usuario < 0:
            print("Por favor, ingrese un número entero positivo.")
            return
        
        print(f"Factoriales desde 1 hasta {num_usuario}:")
        for i in range(1, num_usuario + 1):
            print(f"El factorial de {i} es: {factorial(i)}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

# Ejercicio 2: Serie de Fibonacci
def fibonacci_recursivo(pos): # [cite: 7]
    """
    Calcula el valor de la serie de Fibonacci en la posición indicada de forma recursiva.
    Args:
        pos (int): La posición en la serie de Fibonacci (empezando desde 0).
    Returns:
        int: El valor de Fibonacci en la posición dada.
    """
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        # La formula dada en el ejemplo de la imagen es incorrecta para Fibonacci,
        # la formula correcta es fibonacci_recursivo(pos-1) + fibonacci_recursivo(pos-2)
        # return fibonacci_recursivo(pos - 3) + fibonacci_recursivo(pos - 2)
        return fibonacci_recursivo(pos - 1) + fibonacci_recursivo(pos - 2)

def mostrar_serie_fibonacci_hasta_pos(): # [cite: 7]
    """
    Solicita una posición al usuario y muestra la serie completa de Fibonacci hasta esa posición.
    """
    try:
        pos_usuario = int(input("Ingrese la posición hasta la cual desea ver la serie de Fibonacci: "))
        if pos_usuario < 0:
            print("Por favor, ingrese una posición no negativa.")
            return
        
        print(f"Serie de Fibonacci hasta la posición {pos_usuario}:")
        serie = [fibonacci_recursivo(i) for i in range(pos_usuario + 1)]
        print(serie)
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

# Ejercicio 3: Potencia de un número
def potencia_recursiva(base, exponente): # [cite: 8]
    """
    Calcula la potencia de un número base elevado a un exponente de forma recursiva.
    Args:
        base (int/float): La base.
        exponente (int): El exponente (entero no negativo).
    Returns:
        int/float: El resultado de la potencia.
    """
    if exponente == 0:
        return 1
    elif exponente < 0:
        # Manejo de exponentes negativos si fuera necesario, para este ejercicio asumimos positivo.
        return 1 / (base * potencia_recursiva(base, abs(exponente) - 1))
    else:
        return base * potencia_recursiva(base, exponente - 1)

def probar_potencia(): # [cite: 9]
    """
    Solicita la base y el exponente al usuario y muestra el resultado de la potencia.
    """
    try:
        base_num = float(input("Ingrese la base: "))
        exp_num = int(input("Ingrese el exponente (entero no negativo): "))
        
        if exp_num < 0:
            print("El exponente debe ser un entero no negativo para este ejercicio.")
            return

        resultado = potencia_recursiva(base_num, exp_num)
        print(f"{base_num} elevado a la {exp_num} es: {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números válidos.")

# Ejercicio 4: Decimal a Binario
def decimal_a_binario_recursivo(n): # [cite: 10]
    """
    Convierte un número entero positivo en base decimal a su representación binaria
    como una cadena de texto de forma recursiva.
    Args:
        n (int): El número entero positivo en base decimal.
    Returns:
        str: La representación binaria del número.
    """
    if n == 0: # [cite: 11]
        return "0"
    elif n == 1: # [cite: 11]
        return "1"
    else:
        resto = n % 2 # [cite: 11]
        cociente = n // 2 # [cite: 11]
        return decimal_a_binario_recursivo(cociente) + str(resto) # [cite: 11]

def probar_decimal_a_binario():
    """
    Solicita un número decimal al usuario y muestra su representación binaria.
    """
    try:
        num_decimal = int(input("Ingrese un número entero positivo para convertir a binario: "))
        if num_decimal < 0:
            print("Por favor, ingrese un número entero positivo.")
            return
        
        if num_decimal == 0:
            print(f"El número {num_decimal} en binario es: 0")
        else:
            binario = decimal_a_binario_recursivo(num_decimal)
            print(f"El número {num_decimal} en binario es: {binario}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

# Ejercicio 5: Es Palíndromo
def es_palindromo(palabra): # [cite: 14]
    """
    Verifica si una cadena de texto es un palíndromo de forma recursiva.
    No usa [::-1] ni reversed().
    Args:
        palabra (str): La cadena de texto sin espacios ni tildes.
    Returns:
        bool: True si es un palíndromo, False en caso contrario.
    """
    # Caso base: Si la palabra tiene 0 o 1 caracter, es un palíndromo.
    if len(palabra) <= 1:
        return True
    # Caso recursivo: Compara el primer y último caracter y llama recursivamente para el resto de la palabra.
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

def probar_es_palindromo():
    """
    Solicita una palabra al usuario y verifica si es un palíndromo.
    """
    palabra_input = input("Ingrese una palabra (sin espacios ni tildes) para verificar si es un palíndromo: ").lower().replace(" ", "")
    if es_palindromo(palabra_input):
        print(f"'{palabra_input}' es un palíndromo.")
    else:
        print(f"'{palabra_input}' NO es un palíndromo.")

# Ejercicio 6: Suma de Dígitos
def suma_digitos(n): # [cite: 16]
    """
    Calcula la suma de los dígitos de un número entero positivo de forma recursiva.
    No convierte el número a string.
    Args:
        n (int): El número entero positivo.
    Returns:
        int: La suma de sus dígitos.
    """
    # Caso base: Si el número es de un solo dígito
    if n < 10:
        return n
    # Caso recursivo: Suma el último dígito y llama recursivamente con el resto del número.
    else:
        return (n % 10) + suma_digitos(n // 10) # [cite: 17]

def probar_suma_digitos():
    """
    Solicita un número al usuario y muestra la suma de sus dígitos.
    """
    try:
        num_suma = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
        if num_suma < 0:
            print("Por favor, ingrese un número entero positivo.")
            return
        
        resultado_suma_digitos = suma_digitos(num_suma)
        print(f"La suma de los dígitos de {num_suma} es: {resultado_suma_digitos}")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

# Ejercicio 7: Contar Bloques en una Pirámide
def contar_bloques(n): # [cite: 20]
    """
    Calcula el total de bloques necesarios para construir una pirámide.
    Args:
        n (int): El número de bloques en el nivel más bajo.
    Returns:
        int: El total de bloques.
    """
    # Caso base: Si solo hay un nivel, se necesita un bloque.
    if n == 1:
        return 1
    # Caso recursivo: Suma los bloques del nivel actual y los de la pirámide restante.
    else:
        return n + contar_bloques(n - 1)

def probar_contar_bloques():
    """
    Solicita el número de bloques en el nivel más bajo y muestra el total de bloques.
    """
    try:
        n_bloques = int(input("Ingrese el número de bloques en el nivel más bajo de la pirámide: "))
        if n_bloques <= 0:
            print("Por favor, ingrese un número entero positivo.")
            return
        
        total_bloques = contar_bloques(n_bloques)
        print(f"Se necesitan {total_bloques} bloques para construir la pirámide con {n_bloques} bloques en la base.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

# Ejercicio 8: Contar Dígito
def contar_digito(numero, digito): # [cite: 22]
    """
    Cuenta cuántas veces aparece un dígito específico dentro de un número entero positivo de forma recursiva.
    Args:
        numero (int): El número entero positivo.
        digito (int): El dígito a buscar (entre 0 y 9).
    Returns:
        int: El número de veces que aparece el dígito.
    """
    # Asegurarse de que el dígito sea válido
    if not (0 <= digito <= 9):
        print("El dígito a buscar debe estar entre 0 y 9.")
        return 0
        
    # Caso base: Si el número es 0 (y ya no tiene más dígitos para procesar)
    if numero == 0:
        return 0
    # Caso recursivo:
    else:
        # Obtener el último dígito del número
        ultimo_digito = numero % 10
        # Contar si el último dígito coincide con el dígito buscado
        contador = 1 if ultimo_digito == digito else 0
        # Llamar recursivamente con el resto del número (sin el último dígito)
        return contador + contar_digito(numero // 10, digito)

def probar_contar_digito():
    """
    Solicita un número y un dígito al usuario y muestra cuántas veces aparece el dígito en el número.
    """
    try:
        num_contar = int(input("Ingrese un número entero positivo: "))
        if num_contar < 0:
            print("Por favor, ingrese un número entero positivo.")
            return
        
        dig_buscar = int(input("Ingrese el dígito a buscar (0-9): "))
        
        if not (0 <= dig_buscar <= 9):
            print("Dígito a buscar inválido. Debe ser entre 0 y 9.")
            return

        # Caso especial si el número ingresado es 0 y se busca el dígito 0
        if num_contar == 0 and dig_buscar == 0:
            print(f"El dígito {dig_buscar} aparece 1 vez en el número {num_contar}.")
        else:
            cantidad_apariciones = contar_digito(num_contar, dig_buscar)
            print(f"El dígito {dig_buscar} aparece {cantidad_apariciones} veces en el número {num_contar}.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números enteros.")


# --- Menú principal para ejecutar los ejercicios ---
if __name__ == "__main__":
    while True:
        print("\n--- MENÚ DE EJERCICIOS DE RECURSIVIDAD ---")
        print("1. Calcular Factorial de un número y mostrar hasta N")
        print("2. Mostrar Serie de Fibonacci hasta una posición")
        print("3. Calcular Potencia de un número")
        print("4. Convertir Decimal a Binario")
        print("5. Verificar si una palabra es Palíndromo")
        print("6. Sumar Dígitos de un número")
        print("7. Contar Bloques de una Pirámide")
        print("8. Contar Apariciones de un Dígito en un número")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            calcular_factoriales_hasta_n()
        elif opcion == '2':
            mostrar_serie_fibonacci_hasta_pos()
        elif opcion == '3':
            probar_potencia()
        elif opcion == '4':
            probar_decimal_a_binario()
        elif opcion == '5':
            probar_es_palindromo()
        elif opcion == '6':
            probar_suma_digitos()
        elif opcion == '7':
            probar_contar_bloques()
        elif opcion == '8':
            probar_contar_digito()
        elif opcion == '0':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")