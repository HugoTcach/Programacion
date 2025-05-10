# Solicitar una frase o palabra al usuario
texto = input("Ingresa una frase o palabra: ")

# Verificar si termina con una vocal (mayúscula o minúscula)
if texto[-1].lower() in "aeiou":
    texto += "!"

# Imprimir el resultado
print(texto)