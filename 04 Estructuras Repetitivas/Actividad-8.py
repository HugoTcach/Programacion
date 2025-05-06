#Le dice al usuario lo que va a hacer.
print("Itroduzca 100 números para contar los pares,impares,positivos y negativos! ")

#Inicializa los contadore en 0.
cont_par = 0
cont_impar = 0
cont_negativos = 0
cont_positivos = 0

#Crea un ciclo for para ingresar 10 números,(En el ejercicio dice 100,es cuestion de cambiar el 10 por 100 y ya esta)
for x in range(1, 10+1):
    numeros = int(input(f"Número {x}: "))  #Le pide al usuario que ingrese un número,y le dice en que numero de iteracion esta.
    if numeros >= 0:    #validamos que en número sea mayor a 0(positivo)
        cont_positivos += 1 #Sumamos 1 al contador de positivos.
        if numeros % 2 == 0: #Validamos si el número es par.
            cont_par +=1  #Sumamos 1 al contador de par o impar.
        else:
            cont_impar +=1
            
    else:
        cont_negativos +=1   #Si el número es negativo sumamos 1 al contador de negativos.
        if numeros % 2 == 0:  #Validamos si es par o impar.
            cont_par += 1
        else:
            cont_impar += 1
#Muestra por pantalla los resultados.
print(f"La cantidad de números positivos son: {cont_positivos}")
print(f"La cantidad de números negativos es: {cont_negativos}")
print(f"La cantidad de números pares es: {cont_par}")
print(f"La cantidad de números impares es: {cont_impar}")
    

  