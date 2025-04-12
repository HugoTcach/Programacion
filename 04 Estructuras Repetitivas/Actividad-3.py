#Le pide al usuario el ingreso de dos números.
numero_1 = int(input("Ingrese el primer número por favor: "))
numero_2 = int(input("Ongrese el segundo número por favor: "))

#Inicializa la suma en 0
suma = 0
#Ciclo for para iterar sobre los números ingresados EXCLUYENDOLOS.
for x in range(numero_1 + 1, numero_2):
    suma += x   #Suma sus valores.
print(suma)  #Imprime por pantalla el resultado.