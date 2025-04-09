magnitud = float(input("Ingrese la magnitud del terremoto. Ej: 2.9 : "))

if magnitud >= 7:
    resultado = '"Extremo" (puede causar graves daños a gran escala).'
elif magnitud >= 6:
    resultado = '"Muy Fuerte" (puede causar daños significativos).'
elif magnitud >= 5:
    resultado = '"Fuerte" (puede causar daños en estructuras débiles).'
elif magnitud >= 4:
    resultado = '"Moderado" (sentido por personas, pero generalmente no causa daños).'
elif magnitud >= 3:
    resultado = '"Leve" (ligeramente perceptible).'
else:
    resultado = '"Muy leve" (imperceptible).'

print(f"La magnitud ingresada es: {resultado}")