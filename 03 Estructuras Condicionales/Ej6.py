import random
import statistics
#Se genera una lista de 50 numeros aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
#Calculamos moda, mediana y media
moda = statistics.multimode(numeros_aleatorios)
moda_valor= moda[0]
mediana = statistics.median(numeros_aleatorios)
media = statistics.mean(numeros_aleatorios)
#Se muestran los valores 
print(f"Lista:{numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
#Sesgo
if media > mediana > moda_valor:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda_valor:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda_valor:
    print("Sin sesgo")
else:
    print("El sesgo no se puede determinar")
