from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    sesgo = "Sesgo positivo"
elif media == mediana == moda:
    sesgo = "Sin sesgo"
else:
    sesgo = "Sesgo negativo"

print(f"{sesgo}")