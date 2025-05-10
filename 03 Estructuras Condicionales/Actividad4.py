#solicito edad al usuario
edad = int(input("Ingrese su edad: "))
#indico en que categoria de edad esta
if edad < 12:
    print("Niño")
elif edad >= 12 and edad < 18:
    print("Adolecente")
elif edad >= 18 and edad < 30:
    print("Adulto/Joven")
elif edad >= 30:
    print("Adulto")

