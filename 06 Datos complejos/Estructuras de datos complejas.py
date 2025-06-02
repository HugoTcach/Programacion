# Punto 1: Añadir frutas al diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Punto 2: Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Punto 3: Lista con solo las frutas
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

# Punto 4: Agenda telefónica
agenda = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    telefono = input(f"Ingrese el número de {nombre}: ")
    agenda[nombre] = telefono

buscar = input("Ingrese el nombre del contacto a buscar: ")
if buscar in agenda:
    print(f"El número de {buscar} es {agenda[buscar]}")
else:
    print(f"No se encontró el contacto {buscar}")

# Punto 5: Análisis de frase
frase = input("Ingrese una frase: ")
palabras = frase.lower().split()
palabras_unicas = set(palabras)
conteo_palabras = {}

for palabra in palabras:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Frecuencia de palabras:", conteo_palabras)

# Punto 6: Promedio de alumnos
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingrese nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {alumno}: {promedio:.2f}")

# Punto 7: Sets de estudiantes
parcial1 = set(input("Ingrese los nombres de estudiantes que aprobaron Parcial 1 (separados por coma): ").split(','))
parcial2 = set(input("Ingrese los nombres de estudiantes que aprobaron Parcial 2 (separados por coma): ").split(','))

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los parciales:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)

# Punto 8: Stock de productos
stock = {}
producto = input("Ingrese el nombre del producto a consultar/agregar: ")
if producto in stock:
    agregar = int(input("Ingrese la cantidad a agregar: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto no encontrado. Ingrese stock inicial: "))
    stock[producto] = nuevo_stock

print(f"Stock actual de {producto}: {stock[producto]}")

# Punto 9: Agenda de eventos
agenda_eventos = {}
dia = input("Ingrese el día del evento (ej: lunes): ")
hora = input("Ingrese la hora del evento (ej: 14:00): ")
evento = input("Ingrese la descripción del evento: ")
agenda_eventos[(dia, hora)] = evento

consulta_dia = input("Consultar - Ingrese día: ")
consulta_hora = input("Consultar - Ingrese hora: ")
actividad = agenda_eventos.get((consulta_dia, consulta_hora), "No hay actividad registrada.")
print("Actividad:", actividad)

# Punto 10: Invertir diccionario país-capital
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo'
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario invertido (capital -> país):", capitales_paises)
