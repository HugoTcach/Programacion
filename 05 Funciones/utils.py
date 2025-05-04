def valid_num(mensaje, min = float("-Inf"), max = float("Inf")):
    num = int(input(f"{mensaje}: "))
    while num < min or num > max:
        num = int(input(f"ERROR... {mensaje}"))
    return num

def get_num(mensaje):
    num = input(f"{mensaje}")
    while not es_numero(num):
        num = input(f"ERROR... {mensaje}")
    return num

def es_numero(num):
    try:
        float(num) 
        return True 
    except ValueError:
        return False  

def get_rest(n1, n2):
    return n1 % n2

def es_multiplo(n1, n2):
    return get_rest(n1,n2) == 0

def sucesion_simbolos(simbolo, cant):
    sucesion = ""
    for i in range(cant):
        sucesion += simbolo
    return sucesion

def imprimir_simbolo(simbolo, cant):
    print(sucesion_simbolos(simbolo, cant))