#incio variables y solicito un numero al usuario positivo
n = int(input("Introduce un número entero positivo: "))
if n >= 0:
    #sumo todos los numeros entre el 0 y el numero ofrecido
    suma = sum(range(n + 1))
    print(f"La suma de los números entre 0 y {n} es: {suma}")
else:
    #solicito si el usuario no ingreso un numero positivo
    print("Por favor, ingresa un número entero positivo.")
