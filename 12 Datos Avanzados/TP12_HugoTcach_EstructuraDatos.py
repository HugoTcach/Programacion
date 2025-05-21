import collections

# --------------------------------------------------------------------------------------
# Actividad 1 y 2: Clase Nodo y sus métodos
# --------------------------------------------------------------------------------------

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []
        self.padre = None # Inicialmente, ningún nodo tiene padre

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)
        nodo_hijo.padre = self # Establece el padre del nodo hijo

    def buscar_camino(self, destino_valor):
        """
        Método provisto en el notebook (se asume su existencia para la actividad 1).
        Realiza una búsqueda en profundidad (DFS) para encontrar un camino.
        """
        cola = collections.deque([(self, [self.valor])])

        while cola:
            (nodo_actual, camino) = cola.popleft()

            if nodo_actual.valor == destino_valor:
                return camino

            for hijo in nodo_actual.hijos:
                cola.append((hijo, camino + [hijo.valor]))
        return None

    def calcular_longitud_de_camino(self, destino_valor):
        """
        Calcula la longitud del camino desde el nodo actual hasta el nodo destino.
        Retorna la longitud del camino (número de nodos) o None si no se encuentra. [cite: 5]
        """
        camino_encontrado = self.buscar_camino(destino_valor)
        if camino_encontrado:
            return len(camino_encontrado) # La longitud es el número de nodos en el camino [cite: 5]
        return None [cite: 6]

    def obtener_hijos(self):
        """
        Imprime por pantalla si el nodo tiene hijos y, en caso de tener, cuáles nodos son. [cite: 7]
        """
        if self.hijos:
            nombres_hijos = [hijo.valor for hijo in self.hijos]
            print(f"El nodo '{self.valor}' tiene hijos: {nombres_hijos}")
        else:
            print(f"El nodo '{self.valor}' no tiene hijos.")

    def obtener_padre(self):
        """
        Imprime por pantalla si el nodo tiene padre y, en caso de tener, cuál nodo es. [cite: 8]
        """
        if self.padre:
            print(f"El nodo '{self.valor}' tiene como padre a: '{self.padre.valor}'")
        else:
            print(f"El nodo '{self.valor}' no tiene padre (es la raíz o un nodo sin conexión ascendente).")

    def obtener_tipo(self):
        """
        Imprime por pantalla si el nodo es raíz, rama u hoja.
        Utiliza los métodos obtener_hijos y obtener_padre (implícitamente a través de sus atributos).
        """
        if self.padre is None and not self.hijos:
            print(f"El nodo '{self.valor}' es una hoja y también la raíz (un árbol de un solo nodo).")
        elif self.padre is None:
            print(f"El nodo '{self.valor}' es la raíz.")
        elif not self.hijos:
            print(f"El nodo '{self.valor}' es una hoja.")
        else:
            print(f"El nodo '{self.valor}' es una rama.")

# --------------------------------------------------------------------------------------
# Actividad 3: Clase ArbolBusquedaBinario y método buscar_nodo
# --------------------------------------------------------------------------------------

class ArbolBusquedaBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.hijos_izquierdo is None:
                nodo_actual.hijos_izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.hijos_izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.hijos_derecho is None:
                nodo_actual.hijos_derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo_actual.hijos_derecho, valor)
        # Si el valor ya existe, no hacemos nada (se puede modificar para manejar duplicados)

    def buscar_nodo(self, valor_a_buscar):
        """
        Busca un nodo con el valor_a_buscar en el árbol binario. [cite: 10]
        Retorna True si lo contiene, False en caso contrario. [cite: 10]
        """
        return self._buscar_nodo_recursivo(self.raiz, valor_a_buscar)

    def _buscar_nodo_recursivo(self, nodo_actual, valor_a_buscar):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == valor_a_buscar:
            return True
        elif valor_a_buscar < nodo_actual.valor:
            return self._buscar_nodo_recursivo(nodo_actual.hijos_izquierdo, valor_a_buscar)
        else:
            return self._buscar_nodo_recursivo(nodo_actual.hijos_derecho, valor_a_buscar)

# Se modifica la clase Nodo para que soporte la estructura de un Árbol Binario de Búsqueda
# para la Actividad 3, dado que el enunciado menciona "basándose en la clase ArbolBusquedaBinario
# provista en el notebook", la cual usualmente tiene hijos izquierdo y derecho.
class NodoABB:
    def __init__(self, valor):
        self.valor = valor
        self.hijos_izquierdo = None
        self.hijos_derecho = None

class ArbolBusquedaBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoABB(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.hijos_izquierdo is None:
                nodo_actual.hijos_izquierdo = NodoABB(valor)
            else:
                self._insertar_recursivo(nodo_actual.hijos_izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.hijos_derecho is None:
                nodo_actual.hijos_derecho = NodoABB(valor)
            else:
                self._insertar_recursivo(nodo_actual.hijos_derecho, valor)
        # Si el valor ya existe, no hacemos nada

    def buscar_nodo(self, valor_a_buscar):
        """
        Busca un nodo con el valor_a_buscar en el árbol binario. [cite: 10]
        Retorna True si lo contiene, False en caso contrario. [cite: 10]
        """
        return self._buscar_nodo_recursivo(self.raiz, valor_a_buscar)

    def _buscar_nodo_recursivo(self, nodo_actual, valor_a_buscar):
        if nodo_actual is None:
            return False
        if nodo_actual.valor == valor_a_buscar:
            return True
        elif valor_a_buscar < nodo_actual.valor:
            return self._buscar_nodo_recursivo(nodo_actual.hijos_izquierdo, valor_a_buscar)
        else:
            return self._buscar_nodo_recursivo(nodo_actual.hijos_derecho, valor_a_buscar)

# --------------------------------------------------------------------------------------
# Actividad 4: Funciones para grafos dirigidos
# --------------------------------------------------------------------------------------

def crear_listas_adyacencia_dirigida(nodos, aristas):
    """
    Toma como input los nodos y aristas de un grafo dirigido y retorna
    las listas de adyacencia de cada nodo. [cite: 11]
    Las aristas se nombran (origen, destino). [cite: 13]
    """
    listas_adyacencia = {nodo: [] for nodo in nodos}
    for origen, destino in aristas:
        if origen in listas_adyacencia:
            listas_adyacencia[origen].append(destino)
        else:
            print(f"Advertencia: El nodo de origen '{origen}' de la arista ({origen}, {destino}) no está en la lista de nodos provista.")
    return listas_adyacencia

def crear_matriz_adyacencia_dirigida(nodos, aristas):
    """
    Toma como input los nodos y aristas de un grafo dirigido y retorna
    la matriz de adyacencia del grafo. [cite: 12]
    Las aristas se nombran (origen, destino). [cite: 13]
    """
    num_nodos = len(nodos)
    # Crear un mapeo de nodo a índice para la matriz
    nodo_a_indice = {nodo: i for i, nodo in enumerate(nodos)}
    
    # Inicializar la matriz con ceros
    matriz_adyacencia = [[0] * num_nodos for _ in range(num_nodos)]

    for origen, destino in aristas:
        if origen in nodo_a_indice and destino in nodo_a_indice:
            fila = nodo_a_indice[origen]
            columna = nodo_a_indice[destino]
            matriz_adyacencia[fila][columna] = 1
        else:
            print(f"Advertencia: La arista ({origen}, {destino}) contiene nodos no definidos.")
            
    return matriz_adyacencia

# --------------------------------------------------------------------------------------
# Actividad 5: Prueba de funciones con el grafo dado
# --------------------------------------------------------------------------------------

print("--- Actividad 5: Prueba de funciones de grafos ---")

# Definir los nodos y aristas del grafo dado [cite: 14]
nodos_grafo = ['A', 'B', 'C']
aristas_grafo = [('A', 'B'), ('A', 'C')] # Asumiendo las aristas son dirigidas como se muestra en la imagen [cite: 14]

print("\nGrafo para pruebas:")
print(f"Nodos: {nodos_grafo}")
print(f"Aristas (Origen, Destino): {aristas_grafo}")

# 5.1 Probar crear_listas_adyacencia_dirigida
print("\nListas de Adyacencia Dirigida:")
listas_adya = crear_listas_adyacencia_dirigida(nodos_grafo, aristas_grafo)
for nodo, adyacentes in listas_adya.items():
    print(f"{nodo}: {adyacentes}")

# 5.2 Probar crear_matriz_adyacencia_dirigida
print("\nMatriz de Adyacencia Dirigida:")
matriz_adya = crear_matriz_adyacencia_dirigida(nodos_grafo, aristas_grafo)
# Imprimir encabezado de columnas
print("  " + " ".join(nodos_grafo))
for i, fila in enumerate(matriz_adya):
    print(f"{nodos_grafo[i]} {' '.join(map(str, fila))}")

print("\n--- Demostración de Actividades 1 y 2 (Árboles) ---")

# Creamos un árbol de ejemplo
nodo_a = Nodo("A")
nodo_b = Nodo("B")
nodo_c = Nodo("C")
nodo_d = Nodo("D")
nodo_e = Nodo("E")

nodo_a.agregar_hijo(nodo_b)
nodo_a.agregar_hijo(nodo_c)
nodo_b.agregar_hijo(nodo_d)
nodo_c.agregar_hijo(nodo_e)

print(f"\nLongitud del camino de A a D: {nodo_a.calcular_longitud_de_camino('D')}")
print(f"Longitud del camino de B a E (no existe en este árbol): {nodo_b.calcular_longitud_de_camino('E')}")

nodo_a.obtener_hijos()
nodo_b.obtener_hijos()
nodo_e.obtener_hijos()

nodo_a.obtener_padre()
nodo_d.obtener_padre()
nodo_e.obtener_padre()

nodo_a.obtener_tipo()
nodo_b.obtener_tipo()
nodo_d.obtener_tipo()
print("\n--- Demostración de Actividad 3 (Árbol Binario de Búsqueda) ---")

# Creamos un Árbol Binario de Búsqueda de ejemplo
abb = ArbolBusquedaBinario()
abb.insertar(50)
abb.insertar(30)
abb.insertar(70)
abb.insertar(20)
abb.insertar(40)
abb.insertar(60)
abb.insertar(80)

print(f"¿El árbol contiene el valor 40? {abb.buscar_nodo(40)}")
print(f"¿El árbol contiene el valor 90? {abb.buscar_nodo(90)}")
print(f"¿El árbol contiene el valor 50? {abb.buscar_nodo(50)}")
print(f"¿El árbol contiene el valor 10? {abb.buscar_nodo(10)}")