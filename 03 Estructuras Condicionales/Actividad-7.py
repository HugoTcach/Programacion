#Le pide al usuario que ingrese una palabra o frase.
texto = input("Ingrese una palabra o frase: ")

texto.strip() #Elimina los espacios al principio y al final.

if texto: #Verifica que el texto no este vacio.
    ultima_letra = texto[-1].lower() #Con esto toma la ultima letra del texto y lo convierte a minuscula(lower()) para evitar inconvenientes.
    #Verifica si la ultima letra es vocal.
    es_vocal = ultima_letra in "aeiou" 
    if es_vocal:
        texto += "!" #Si termina en vocal,le agrega un signo de interrogacion.
        print(texto)
    else:
        print(texto) #Si no termina en vocal,muestra el texto como esta.
else:
    print("El texto no puede estar vacio")