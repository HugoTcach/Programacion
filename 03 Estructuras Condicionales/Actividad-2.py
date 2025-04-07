#Le pide al usuario que ingrese el número de su nota.
nota = float(input("Ingrese el número de su nota por favor: "))

# Con la condicional if,le dice si la nota es mayor o igual a 6 :Aprobado.Si no,Desaprobado.
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")