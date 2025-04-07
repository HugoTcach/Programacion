#Se solicita al usuario ingresar una frase o palabra
palabra_frase=input("Ingrese una frase o palabra: ")
#Verificamos si termina en vocal
if palabra_frase[-1].lower() in "aeiou":
    #Se agrega signo ! si termina en vocal
    palabra_frase = palabra_frase +"!"
print(palabra_frase)