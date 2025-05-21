# Gestión de Stock de Productos

# Listas paralelas
nombres_productos = []
cantidades_stock = []

# Menú interactivo
def mostrar_menu():
    print("\n🛒 Menú de opciones:")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Salir")

# Agregar nuevo producto
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    nombres_productos.append(nombre)
    cantidades_stock.append(cantidad)
    print("✅ Producto agregado con éxito.")

# Ver productos agotados
def ver_productos_agotados():
    agotados = False
    print("\n📦 Productos agotados:")
    for i in range(len(nombres_productos)):
        if cantidades_stock[i] == 0:
            print("- " + nombres_productos[i])
            agotados = True
    if not agotados:
        print("No hay productos agotados.")

# Actualizar stock
def actualizar_stock():
    producto = input("Ingrese el nombre del producto a actualizar: ")
    encontrado = False
    for i in range(len(nombres_productos)):
        if nombres_productos[i].lower() == producto.lower():
            while True:
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                    if nueva_cantidad < 0:
                        print("La cantidad no puede ser negativa.")
                    else:
                        break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            cantidades_stock[i] = nueva_cantidad
            print("🔄 Stock actualizado.")
            encontrado = True
            break
    if not encontrado:
        print("❌ Producto no encontrado.")

# Mostrar todos los productos
def ver_todos_los_productos():
    if len(nombres_productos) == 0:
        print("No hay productos registrados.")
    else:
        print("\n📋 Listado de productos:")
        for i in range(len(nombres_productos)):
            print(f"- {nombres_productos[i]}: {cantidades_stock[i]} unidades")

# Programa principal
def programa_principal():
    salir = False
    while not salir:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_productos_agotados()
        elif opcion == "3":
            actualizar_stock()
        elif opcion == "4":
            ver_todos_los_productos()
        elif opcion == "5":
            print("👋 Gracias por usar el sistema.")
            salir = True
        else:
            print("⚠ Opción inválida. Intente nuevamente.")

# Ejecutar el programa
programa_principal()
