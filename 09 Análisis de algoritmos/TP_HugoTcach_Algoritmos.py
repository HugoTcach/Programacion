import time

# Ejercicio 1: Suma de los primeros n números (con bucle)
def suma_numeros(n):
    """
    Calcula la suma de los primeros n números utilizando un bucle.
    Orden de complejidad T(n) y O(n).
    """
    # T(n) = 1 (asignación de suma)
    suma = 0 
    # El bucle for se ejecuta n veces.
    # Dentro del bucle, hay 1 operación de suma y 1 operación de asignación.
    # T(n) = 1 + n * (1 + 1) = 1 + 2n
    for i in range(1, n + 1): 
        suma += i
    # T(n) = 1 (retorno)
    return suma
    # T(n) total: 1 + 2n + 1 = 2n + 2
    # O(n) = O(2n + 2) = O(n)
    # Justificación: El tiempo de ejecución crece linealmente con el tamaño de la entrada 'n'
    # debido al bucle que itera 'n' veces. [cite: 6]

# Ejercicio 2: Suma de los primeros n números (con fórmula)
def suma_numeros_formula(n):
    """
    Calcula la suma de los primeros n números utilizando la fórmula de Gauss.
    Orden de complejidad T(n) y O(n).
    """
    # T(n) = 1 (operación de multiplicación) + 1 (operación de suma) + 1 (operación de división entera)
    # T(n) = 3 (operaciones constantes)
    return (n * (n + 1)) // 2
    # O(n) = O(3) = O(1)
    # Justificación: El tiempo de ejecución es constante y no depende del tamaño de la entrada 'n'
    # ya que realiza un número fijo de operaciones matemáticas, independientemente del valor de 'n'.

# Comparación Ejercicio 1 y 2
"""
Comparación de eficiencia entre suma_numeros (Ejercicio 1) y suma_numeros_formula (Ejercicio 2):
La solución más eficiente es `suma_numeros_formula` (Ejercicio 2)[cite: 5].

Explicación:
- `suma_numeros` tiene una complejidad temporal de O(n)[cite: 6]. Esto significa que el tiempo de ejecución crece linealmente con el número de entrada 'n'. A medida que 'n' se hace muy grande, el número de operaciones (iteraciones del bucle) también aumenta significativamente.
- `suma_numeros_formula` tiene una complejidad temporal de O(1). Esto significa que el tiempo de ejecución es constante, independientemente del tamaño de la entrada 'n'. Solo realiza unas pocas operaciones matemáticas fijas (multiplicación, suma, división entera), sin importar si 'n' es 10 o 1,000,000.

En un array grande, la suma gaussiana es mucho más rápida porque realiza una única operación matemática, mientras que la suma con bucle tarda más al recorrer todos los elementos. Por lo tanto, para valores grandes de 'n', la fórmula de Gauss es exponencialmente más eficiente.
"""

# Ejercicio 3: Búsqueda de un elemento en una lista desordenada
def buscar_elemento(lista, objetivo):
    """
    Busca un elemento en una lista desordenada.
    Determina el peor caso y la complejidad temporal de este algoritmo.
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
    # Complejidad temporal en notación Big-O: O(n)
    # Justificación: En el peor caso, el algoritmo debe examinar cada elemento de la lista
    # para determinar si el objetivo está presente, lo que lleva a un tiempo de ejecución
    # que crece linealmente con el tamaño de la lista 'n'. [cite: 3]

# Ejercicio 4: Encontrar el número máximo en una lista
def encontrar_maximo(lista):
    """
    Encuentra el número máximo en una lista.
    Determina el orden de complejidad de este algoritmo.
    """
    # 1 operación de asignación
    maximo = lista[0]
    # El bucle for itera sobre cada 'elemento' en la 'lista'.
    # Si la lista tiene n elementos, el bucle se ejecuta n-1 veces (ya que el primer elemento se inicializa).
    # O bien, si consideramos el recorrido completo, se ejecuta n veces si la lista tiene n elementos.
    for elemento in lista:
        # Dentro del bucle, hay 1 operación de comparación 'elemento > maximo'.
        # Si la condición es verdadera, hay 1 operación de asignación 'maximo = elemento'.
        if elemento > maximo:
            maximo = elemento
    # 1 operación de retorno
    return maximo
    # T(n) = 1 (inicialización) + n (iteraciones) * (1 a 2 operaciones por iteración) + 1 (retorno)
    # T(n) = 1 + n * k + 1, donde k es una constante.
    # Orden de complejidad en notación Big-O: O(n)
    # Justificación: El algoritmo debe recorrer todos los elementos de la lista una vez
    # para encontrar el valor máximo, lo que resulta en un tiempo de ejecución
    # que crece linealmente con el tamaño de la lista 'n'. [cite: 8]

# Ejercicio 5: Ordenamiento por selección
def ordenamiento_seleccion(lista):
    """
    Implementa el algoritmo de ordenamiento por selección.
    Determina la complejidad temporal y explica su comportamiento en el peor caso.
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
    # Complejidad temporal en notación Big-O: O(n^2)
    # Comportamiento en el peor caso:
    # El algoritmo de ordenamiento por selección siempre realiza la misma cantidad de comparaciones y
    # aproximadamente la misma cantidad de intercambios, independientemente del orden inicial de la lista.
    # Esto significa que su peor caso y su caso promedio tienen la misma complejidad temporal: O(n^2).
    # Las comparaciones (el factor dominante) siempre son $n*(n-1)/2$.

# --- PRUEBAS Y RESULTADOS ---

print("--- Ejercicio 1: Suma de los primeros n números (bucle) ---")
n_ej1 = 100000
start_time = time.time()
resultado_ej1 = suma_numeros(n_ej1)
end_time = time.time()
print(f"Suma de los primeros {n_ej1} números (bucle): {resultado_ej1}")
print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
print(f"Orden de complejidad T(n): 2n + 2")
print(f"Orden de complejidad O(n): O(n)\n")


print("--- Ejercicio 2: Suma de los primeros n números (fórmula) ---")
n_ej2 = 100000
start_time = time.time()
resultado_ej2 = suma_numeros_formula(n_ej2)
end_time = time.time()
print(f"Suma de los primeros {n_ej2} números (fórmula): {resultado_ej2}")
print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
print(f"Orden de complejidad T(n): 3")
print(f"Orden de complejidad O(n): O(1)\n")

print("--- Comparación Ejercicio 1 y 2 ---")
print("La solución con la fórmula (Ejercicio 2) es más eficiente (O(1)) que la solución con bucle (Ejercicio 1) (O(n)).")
print("Para valores grandes de n, la diferencia en tiempo de ejecución será muy significativa.")
print("La suma gaussiana es mucho más rápida porque realiza una única operación matemática, mientras que la suma con bucle tarda más al recorrer todos los elementos. [cite: 3]")
print("-" * 40 + "\n")


print("--- Ejercicio 3: Búsqueda de un elemento en una lista desordenada ---")
lista_ej3_existente = list(range(100000))
lista_ej3_no_existente = list(range(100000))

# Peor caso: elemento no encontrado o al final
objetivo_ej3_peor = 100001
start_time = time.time()
encontrado_ej3_peor = buscar_elemento(lista_ej3_no_existente, objetivo_ej3_peor)
end_time = time.time()
print(f"Búsqueda (peor caso - no encontrado): {encontrado_ej3_peor}")
print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
print(f"Peor caso y complejidad temporal: O(n)\n")
print("-" * 40 + "\n")

print("--- Ejercicio 4: Encontrar el número máximo en una lista ---")
lista_ej4 = [random.randint(0, 1000000) for _ in range(100000)]
start_time = time.time()
maximo_ej4 = encontrar_maximo(lista_ej4)
end_time = time.time()
print(f"Número máximo encontrado: {maximo_ej4}")
print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
print(f"Orden de complejidad: O(n)\n")
print("-" * 40 + "\n")

print("--- Ejercicio 5: Ordenamiento por selección ---")
# Para n grandes, el ordenamiento por selección puede ser muy lento (O(n^2)).
# Usaremos un tamaño de lista más pequeño para la demostración práctica.
import random
lista_ej5 = [random.randint(0, 1000) for _ in range(500)] # Reducimos el tamaño para la prueba
# print(f"Lista original (parcial): {lista_ej5[:10]}...") # Imprime solo los primeros 10 elementos para no saturar

start_time = time.time()
lista_ordenada_ej5 = ordenamiento_seleccion(lista_ej5.copy()) # .copy() para no modificar la original
end_time = time.time()
# print(f"Lista ordenada (parcial): {lista_ordenada_ej5[:10]}...") # Imprime solo los primeros 10 elementos
print(f"Tamaño de la lista para ordenamiento por selección: {len(lista_ej5)}")
print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
print(f"Complejidad temporal: O(n^2)")
print("Comportamiento en el peor caso: El ordenamiento por selección siempre realiza aproximadamente n^2/2 comparaciones e n intercambios, independientemente del estado inicial de la lista. Su peor caso es igual a su caso promedio.")
print("-" * 40 + "\n")