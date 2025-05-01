#Definir funciones

def segundos_a_horas(segundos):
    hora = round(segundos / 3600)   #3600 segundos equivalen a una hora.
    if segundos < 3600:
         print("La cantidad de segundos ingresados no llegan a completar una hora..")
         return hora 
    return hora

#Programa principal

segundos = int(input("Ingrese la cantidad de segundos que desee: "))

print(f"La equivalencia de segundos ingresados en horas es: {segundos_a_horas(segundos)} hora/s")