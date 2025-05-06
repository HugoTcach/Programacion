
import random  #Importa random para crear una lista de números aleatorios.
import statistics as st  #Importa statistics para calcular la moda,media y mediana.

#Crea una lista de números aleatoria.
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

#Mediante condicionales calcula la media,moda y mediana para saber si hay sesgo positivo,negativo o si directamente no hay sesgo.
if st.mean(numeros_aleatorios) > st.median(numeros_aleatorios) and st.median(numeros_aleatorios) > st.mode(numeros_aleatorios):
    print("Hay sesgo positivo")
elif st.mean(numeros_aleatorios) < st.median(numeros_aleatorios) and st.median(numeros_aleatorios) < st.mode(numeros_aleatorios):
    print("Hay sesgo negativo")
elif st.mean(numeros_aleatorios) == st.median(numeros_aleatorios) and st.median(numeros_aleatorios) == st.mode(numeros_aleatorios):
    print("Sin sesgo")

 
 