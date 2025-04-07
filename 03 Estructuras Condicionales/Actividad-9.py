#Le pide al usuario que ingrese la magnitus del terremoto.
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print('"Muy leve" (imperceptible)')
elif magnitud >= 3 and magnitud < 4:
    print('"Leve" (Ligeramente perceptible)')
elif magnitud >= 4 and magnitud < 5:
    print('"Moderado" (Sentido por personas,pero generalmete no causa daños)')
elif magnitud >= 5 and magnitud < 6:
    print('"Fuerte"(Puede causar daños en estructuras debiles)')
elif magnitud >= 6 and magnitud < 7:
    print('"Muy fuerte"(Puede causar daños significativos)')
elif magnitud >= 7 :
    print('"Extremo"(Puede causar grandes daños a gran escala)')
