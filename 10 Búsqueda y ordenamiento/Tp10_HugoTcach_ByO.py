import time
import random

# ==============================================================================
# PRIMER TRABAJO PRÁCTICO: ANÁLISIS DE ALGORITMOS
# Objetivo: Determinar la complejidad temporal de diferentes algoritmos
#           utilizando la notación Big-O. Comparar distintas soluciones
#           para un mismo problema y analizar cuál es más eficiente. [cite: 53]
# ==============================================================================

# Ejercicio 1: Suma de los primeros n números (con bucle)
def suma_numeros(n):
    """
    Calcula la suma de los primeros n números utilizando un bucle.
    Orden de complejidad T(n) y O(n). [cite: 54]
    """
    # T(n) = 1 (asignación de suma)
    suma = 0
    # El bucle for se ejecuta n veces. [cite: 54]
    # Dentro del bucle, hay 1 operación de suma y 1 operación de asignación.
    # T(n) = 1 + n * (1 + 1) = 1 + 2n
    for i in range(1, n + 1):
        suma += i
    # T(n) = 1 (retorno)
    return suma
    # T(n) total: 1 (inicialización) + 2n (operaciones dentro del bucle) + 1 (retorno) = 2n + 2
    # O(n) = O(2n + 2) = O(n) [cite: 54]
    # Justificación: El tiempo de ejecución crece linealmente con el tamaño de la entrada 'n' [cite: 55]
    # debido al bucle que itera 'n' veces.

# Ejercicio 2: Suma de los primeros n números (con fórmula)
def suma_numeros_formula(n):
    """
    Calcula la suma de los primeros n números utilizando la fórmula de Gauss.
    Orden de complejidad T(n) y O(n). [cite: 58]
    """
    # T(n) = 1 (operación de multiplicación) + 1 (operación de suma) + 1 (operación de división entera)
    # T(n) = 3 (operaciones constantes)
    return (n * (n + 1)) // 2
    # O(n) = O(3) = O(1) [cite: 58]
    # Justificación: El tiempo de ejecución es constante y no depende del tamaño de la entrada 'n' [cite: 55]
    # ya que realiza un número fijo de operaciones matemáticas, independientemente del valor de 'n'.

# Comparación Ejercicio 1 y 2
"""
Comparación de eficiencia entre suma_numeros (Ejercicio 1) y suma_numeros_formula (Ejercicio 2): [cite: 56]
La solución más eficiente es `suma_numeros_formula` (Ejercicio 2).

Explicación:
- `suma_numeros` tiene una complejidad temporal de O(n). Esto significa que el tiempo de ejecución
  crece linealmente con el número de entrada 'n'. A medida que 'n' se hace muy grande,
  el número de operaciones (iteraciones del bucle) también aumenta significativamente.
- `suma_numeros_formula` tiene una complejidad temporal de O(1). Esto significa que el tiempo de ejecución
  es constante, independientemente del tamaño de la entrada 'n'. Solo realiza unas pocas operaciones
  matemáticas fijas (multiplicación, suma, división entera), sin importar si 'n' es 10 o 1,000,000.

En un array grande, la suma gaussiana es mucho más rápida porque realiza una única operación matemática,
mientras que la suma con bucle tarda más al recorrer todos los elementos. Por lo tanto, para valores
grandes de 'n', la fórmula de Gauss es significativamente más eficiente.
"""

# Ejercicio 3: Búsqueda de un elemento en una lista desordenada
def buscar_elemento(lista, objetivo):
    """
    Busca un elemento en una lista desordenada.
    Determina el peor caso y la complejidad temporal de este algoritmo. [cite: 58]
    """
    # El bucle for itera sobre cada 'elemento' en la 'lista'.
    # En el peor caso, el elemento objetivo no está en la lista o es el último elemento.
    # Esto significa que el bucle recorrerá todos los 'n' elementos de la lista.
    for elemento in lista:
        # Dentro del bucle, la comparación 'elemento == objetivo' es 1 operación.
        # El 'return True' es 1 operación.
        if elemento == objetivo:
            return True
    # El 'return False' es 1 operación si el elemento no se encuentra.
    return False
    # Peor caso: El elemento no se encuentra en la lista o está al final.
    # T(n) = n (iteraciones del bucle) * 1 (comparación) + 1 (retorno final) = n + 1
    # Complejidad temporal en notación Big-O: O(n) [cite: 58]
    # Justificación: En el peor caso, el algoritmo debe examinar cada elemento de la lista
    # para determinar si el objetivo está presente, lo que lleva a un tiempo de ejecución
    # que crece linealmente con el tamaño de la lista 'n'.

# Ejercicio 4: Encontrar el número máximo en una lista
def encontrar_maximo(lista):
    """
    Encuentra el número máximo en una lista.
    Determina el orden de complejidad de este algoritmo. [cite: 59]
    """
    # 1 operación de asignación
    maximo = lista[0]
    # El bucle for itera sobre cada 'elemento' en la 'lista'.
    # Si la lista tiene n elementos, el bucle se ejecuta n veces.
    for elemento in lista:
        # Dentro del bucle, hay 1 operación de comparación 'elemento > maximo'.
        # Si la condición es verdadera, hay 1 operación de asignación 'maximo = elemento'.
        if elemento > maximo:
            maximo = elemento
    # 1 operación de retorno
    return maximo
    # T(n) = 1 (inicialización) + n (iteraciones) * (1 a 2 operaciones por iteración) + 1 (retorno)
    # T(n) = 1 + n * k + 1, donde k es una constante.
    # Orden de complejidad en notación Big-O: O(n) [cite: 59]
    # Justificación: El algoritmo debe recorrer todos los elementos de la lista una vez
    # para encontrar el valor máximo, lo que resulta en un tiempo de ejecución
    # que crece linealmente con el tamaño de la lista 'n'.

# Ejercicio 5: Ordenamiento por selección
def ordenamiento_seleccion(lista):
    """
    Implementa el algoritmo de ordenamiento por selección.
    Determina la complejidad temporal y explica su comportamiento en el peor caso. [cite: 60]
    """
    # 1 operación de asignación
    n = len(lista)
    # Bucle externo: se ejecuta 'n' veces.
    for i in range(n):
        # 1 operación de asignación
        min_idx = i
        # Bucle interno: se ejecuta desde 'i+1' hasta 'n-1'.
        # La primera vez que i=0, se ejecuta n-1 veces.
        # La segunda vez que i=1, se ejecuta n-2 veces.
        # ...
        # La última vez, se ejecuta 1 vez.
        # La suma de las iteraciones es (n-1) + (n-2) + ... + 1 = n*(n-1)/2, que es O(n^2).
        for j in range(i + 1, n):
            # 1 operación de comparación
            if lista[j] < lista[min_idx]:
                # 1 operación de asignación
                min_idx = j
        # Fuera del bucle interno, se realizan 3 operaciones de asignación (intercambio).
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    # 1 operación de retorno
    return lista
    # T(n) total:
    # El bucle externo es O(n).
    # El bucle interno es O(n) en cada iteración del bucle externo.
    # Por lo tanto, los bucles anidados dan una complejidad de O(n*n) = O(n^2).
    # Las operaciones de asignación e intercambio son constantes dentro de cada iteración.
    # Complejidad temporal en notación Big-O: O(n^2) [cite: 60]
    # Comportamiento en el peor caso:
    # El algoritmo de ordenamiento por selección siempre realiza la misma cantidad de comparaciones y
    # aproximadamente la misma cantidad de intercambios, independientemente del orden inicial de la lista.
    # Esto significa que su peor caso y su caso promedio tienen la misma complejidad temporal: O(n^2).
    # Las comparaciones (el factor dominante) siempre son $n*(n-1)/2$.

# --- PRUEBAS Y RESULTADOS DEL PRIMER TRABAJO PRÁCTICO ---

print("=" * 50)
print("--- RESULTADOS DEL PRIMER TRABAJO PRÁCTICO (ANÁLISIS DE ALGORITMOS) ---")
print("=" * 50)

print("\n--- Ejercicio 1: Suma de los primeros n números (bucle) ---")
n_ej1 = 100000
start_time = time.time()
resultado_ej1 = suma_numeros(n_ej1)
end_time = time.time()
print(f"Suma de los primeros {n_ej1} números (bucle): {resultado_ej1}")
print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
print(f"Orden de complejidad T(n): 2n + 2")
print(f"Orden de complejidad O(n): O(n)")


print("\n--- Ejercicio 2: Suma de los primeros n números (fórmula) ---")
n_ej2 = 100000
start_time = time.time()
resultado_ej2 = suma_numeros_formula(n_ej2)
end_time = time.time()
print(f"Suma de los primeros {n_ej2} números (fórmula): {resultado_ej2}")
print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
print(f"Orden de complejidad T(n): 3")
print(f"Orden de complejidad O(n): O(1)")

print("\n--- Comparación Ejercicio 1 y 2 ---")
print("La solución con la fórmula (Ejercicio 2) es más eficiente (O(1)) que la solución con bucle (Ejercicio 1) (O(n)).")
print("Para valores grandes de n, la diferencia en tiempo de ejecución será muy significativa.")
print("La suma gaussiana es mucho más rápida porque realiza una única operación matemática, mientras que la suma con bucle tarda más al recorrer todos los elementos.")


print("\n--- Ejercicio 3: Búsqueda de un elemento en una lista desordenada ---")
lista_ej3_existente = list(range(100000))
lista_ej3_no_existente = list(range(100000))

# Peor caso: elemento no encontrado o al final
objetivo_ej3_peor = 100001
start_time = time.time()
encontrado_ej3_peor = buscar_elemento(lista_ej3_no_existente, objetivo_ej3_peor)
end_time = time.time()
print(f"Búsqueda (peor caso - no encontrado): {encontrado_ej3_peor}")
print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
print(f"Peor caso y complejidad temporal: O(n)")


print("\n--- Ejercicio 4: Encontrar el número máximo en una lista ---")
lista_ej4 = [random.randint(0, 1000000) for _ in range(100000)]
start_time = time.time()
maximo_ej4 = encontrar_maximo(lista_ej4)
end_time = time.time()
print(f"Número máximo encontrado: {maximo_ej4}")
print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
print(f"Orden de complejidad: O(n)")


print("\n--- Ejercicio 5: Ordenamiento por selección ---")
# Para n grandes, el ordenamiento por selección puede ser muy lento (O(n^2)).
# Usaremos un tamaño de lista más pequeño para la demostración práctica.
lista_ej5_seleccion = [random.randint(0, 1000) for _ in range(500)] # Reducimos el tamaño para la prueba
# print(f"Lista original (parcial): {lista_ej5_seleccion[:10]}...") # Imprime solo los primeros 10 elementos para no saturar

start_time = time.time()
lista_ordenada_ej5_seleccion = ordenamiento_seleccion(lista_ej5_seleccion.copy()) # .copy() para no modificar la original
end_time = time.time()
# print(f"Lista ordenada (parcial): {lista_ordenada_ej5_seleccion[:10]}...") # Imprime solo los primeros 10 elementos
print(f"Tamaño de la lista para ordenamiento por selección: {len(lista_ej5_seleccion)}")
print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
print(f"Complejidad temporal: O(n^2)")
print("Comportamiento en el peor caso: El ordenamiento por selección siempre realiza aproximadamente n^2/2 comparaciones e n intercambios, independientemente del estado inicial de la lista. Su peor caso es igual a su caso promedio.")
print("=" * 50)


# ==============================================================================
# SEGUNDO TRABAJO PRÁCTICO: BÚSQUEDA Y ORDENAMIENTO
# Objetivo: Comprender y aplicar las estructuras condicionales en la programación,
#           desarrollando algoritmos que involucren tomas de decisiones. [cite: 31]
# ==============================================================================

# Ejercicio 1: Búsqueda Lineal
def busqueda_lineal_tp2(lista, objetivo): # Renombrada para evitar conflicto con el primer TP
    """
    Escribe una función busqueda_lineal(lista, objetivo) que recorra la lista y
    devuelva el índice del elemento si se encuentra, o -1 si no está. [cite: 35]
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Prueba Ejercicio 1
lista_tp2_ej1 = [10, 20, 30, 40, 50] # [cite: 36]
print("\n--- TP 10: Ejercicio 1 - Búsqueda Lineal ---")
print(f"Buscando 30 en {lista_tp2_ej1}: {busqueda_lineal_tp2(lista_tp2_ej1, 30)}") # Debe imprimir el índice correcto [cite: 36]
print("-" * 40)

# Ejercicio 2: Búsqueda Lineal Contando Comparaciones
def busqueda_lineal_contando_tp2(lista, objetivo): # Renombrada para evitar conflicto
    """
    Modifica la función de búsqueda lineal para contar cuántas comparaciones realiza
    antes de encontrar el número 50 en [10, 20, 30, 40, 50]. [cite: 37]
    """
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i] == objetivo:
            return i, comparaciones
    return -1, comparaciones

# Prueba Ejercicio 2
lista_tp2_ej2 = [10, 20, 30, 40, 50] # [cite: 38]
print("\n--- TP 10: Ejercicio 2 - Búsqueda Lineal Contando ---")
indice_tp2_ej2, comps_tp2_ej2 = busqueda_lineal_contando_tp2(lista_tp2_ej2, 50)
print(f"Buscando 50 en {lista_tp2_ej2}: Índice {indice_tp2_ej2}, Comparaciones: {comps_tp2_ej2}") # ¿Cuántas comparaciones se hicieron? [cite: 38]
print("-" * 40)

# Ejercicio 3: Búsqueda Binaria
def busqueda_binaria_tp2(lista, objetivo): # Renombrada para evitar conflicto
    """
    Implementa la función busqueda_binaria(lista, objetivo), que tome una lista ordenada
    y devuelva el índice del elemento encontrado o -1 si no está. [cite: 39]
    """
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Prueba Ejercicio 3
lista_tp2_ej3 = [1, 3, 5, 7, 9, 11, 13, 15] # [cite: 40]
print("\n--- TP 10: Ejercicio 3 - Búsqueda Binaria ---")
print(f"Buscando 7 en {lista_tp2_ej3}: {busqueda_binaria_tp2(lista_tp2_ej3, 7)}") # Debe imprimir el índice correcto [cite: 40]
print("-" * 40)

# Ejercicio 4: Búsqueda Binaria Contando Pasos
def busqueda_binaria_contando_tp2(lista, objetivo): # Renombrada para evitar conflicto
    """
    Modifica la búsqueda binaria para contar cuántos pasos se necesitan para encontrar
    el número 11 en [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]. [cite: 41]
    """
    izquierda, derecha = 0, len(lista) - 1
    pasos = 0
    while izquierda <= derecha:
        pasos += 1
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio, pasos
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1, pasos

# Prueba Ejercicio 4
lista_tp2_ej4 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21] # [cite: 42]
print("\n--- TP 10: Ejercicio 4 - Búsqueda Binaria Contando ---")
indice_tp2_ej4, pasos_tp2_ej4 = busqueda_binaria_contando_tp2(lista_tp2_ej4, 11)
print(f"Buscando 11 en {lista_tp2_ej4}: Índice {indice_tp2_ej4}, Pasos: {pasos_tp2_ej4}") # ¿Cuántos pasos se hicieron? [cite: 42]
print("-" * 40)

# Ejercicio 5: Búsqueda Lineal en lista aleatoria
print("\n--- TP 10: Ejercicio 5 - Búsqueda Lineal en lista aleatoria ---")
lista_tp2_ej5 = [random.randint(1, 100) for _ in range(20)] # [cite: 44]
print(f"Lista generada: {lista_tp2_ej5}")
# Reutilizamos la función busqueda_lineal_tp2
resultado_tp2_ej5 = busqueda_lineal_tp2(lista_tp2_ej5, 50) # [cite: 44]
print(f"Buscando 50 en la lista generada: Índice {resultado_tp2_ej5}")
print("-" * 40)

# Ejercicio 6: Búsqueda Binaria en lista ordenada
print("\n--- TP 10: Ejercicio 6 - Búsqueda Binaria en lista ordenada ---")
lista_ordenada_tp2_ej6 = sorted(lista_tp2_ej5) # [cite: 45]
print(f"Lista ordenada: {lista_ordenada_tp2_ej6}")
# Reutilizamos la función busqueda_binaria_tp2
resultado_tp2_ej6 = busqueda_binaria_tp2(lista_ordenada_tp2_ej6, 50) # [cite: 45]
print(f"Buscando 50 en la lista ordenada: Índice {resultado_tp2_ej6}")
print("-" * 40)

# Ejercicio 7: Contar ocurrencias
def contar_ocurrencias_tp2(lista, numero): # Renombrada para evitar conflicto
    """
    Escribe una función que cuente cuántas veces aparece el número 5 en la lista [1, 5, 2, 5, 3, 5, 4, 5]. [cite: 46]
    """
    contador = 0
    for elemento in lista:
        if elemento == numero:
            contador += 1
    return contador

# Prueba Ejercicio 7
lista_tp2_ej7 = [1, 5, 2, 5, 3, 5, 4, 5] # [cite: 46]
print("\n--- TP 10: Ejercicio 7 - Contar ocurrencias ---")
print(f"Ocurrencias de 5 en {lista_tp2_ej7}: {contar_ocurrencias_tp2(lista_tp2_ej7, 5)}") # Debe imprimir 4 [cite: 46]
print("-" * 40)

# Ejercicio 8: Generar una lista ordenada de 10,000 números y medir el tiempo
# que tarda la búsqueda lineal y la búsqueda binaria en encontrar un número. [cite: 47]
print("\n--- TP 10: Ejercicio 8 - Comparación de tiempos (Búsqueda Lineal vs. Binaria) ---")
lista_grande_tp2_ej8 = list(range(10000)) # [cite: 48]
numero_a_buscar_tp2_ej8 = 7500 # Un número intermedio para la prueba

# Implementa búsqueda lineal y mide su tiempo [cite: 48]
start_time_lineal_tp2 = time.time()
indice_lineal_tp2_ej8 = busqueda_lineal_tp2(lista_grande_tp2_ej8, numero_a_buscar_tp2_ej8)
end_time_lineal_tp2 = time.time()
tiempo_lineal_tp2_ej8 = end_time_lineal_tp2 - start_time_lineal_tp2
print(f"Búsqueda Lineal (elemento {numero_a_buscar_tp2_ej8}): Índice {indice_lineal_tp2_ej8}, Tiempo: {tiempo_lineal_tp2_ej8:.6f} segundos")

# Implementa búsqueda binaria y mide su tiempo [cite: 48]
start_time_binaria_tp2 = time.time()
indice_binaria_tp2_ej8 = busqueda_binaria_tp2(lista_grande_tp2_ej8, numero_a_buscar_tp2_ej8)
end_time_binaria_tp2 = time.time()
tiempo_binaria_tp2_ej8 = end_time_binaria_tp2 - start_time_binaria_tp2
print(f"Búsqueda Binaria (elemento {numero_a_buscar_tp2_ej8}): Índice {indice_binaria_tp2_ej8}, Tiempo: {tiempo_binaria_tp2_ej8:.6f} segundos")
print("-" * 40)

# Ejercicio 9: Búsqueda en Diccionarios por Valor
def buscar_por_edad(diccionario, edad):
    """
    Busca una edad dada en un diccionario y devuelve el nombre asociado. [cite: 50]
    """
    for nombre, edad_persona in diccionario.items():
        if edad_persona == edad:
            return nombre
    return None

# Prueba Ejercicio 9
personas_tp2_ej9 = {"Alice": 25, "Bob": 30, "Charlie": 22} # [cite: 51]
print("\n--- TP 10: Ejercicio 9 - Búsqueda en Diccionario por Valor ---")
print(f"Buscando edad 30 en {personas_tp2_ej9}: {buscar_por_edad(personas_tp2_ej9, 30)}") # Debe imprimir "Bob" [cite: 51]
print("-" * 40)