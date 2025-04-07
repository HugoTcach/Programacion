#Le pide al usuario que ingrese su nombre.
nombre = input("Ingrese su nombre: ")
#Verifica que el texto no este vacio.
if nombre:
    #Le pide al usuario que ingrese las opciones 1, 2 o 3.
    opcion = input("Elija la opcion que desee: 1, 2 o 3: \nOpcion 1: Si desea su nombre en mayúscula.\nOpcion 2: Si desea su nombre en minúscula.\nOpcion 3: Si desea su nombre con la primera letra en mayúscula.\nIngrese su opcion: ")
    if opcion == "1":
        nombre_mayuscula = nombre.upper()#Opcion 1: muestra nombre en mayúscula.
        print(nombre_mayuscula)
    elif opcion == "2":
        nombre_minuscula = nombre.lower()#Opcion 2: muestra nombre en minúscula.
        print(nombre_minuscula)
    elif opcion == "3":
        #En esta opcion podemos usar la funcion capitalize o la funcion title depende lo que queramos,aca nos servian las 2!
        primera_letra_mayúscula = nombre.capitalize()#Opcion 3: muestra nombre con la primera letra en mayúscula.
        print(primera_letra_mayúscula)
    else:
        print("Opcion inexistente")
else:
    print("ERROR! texto vacio.")