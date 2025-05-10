# Dada la lista "compras", cuyos elementos representan los productos comprados por diferentes clientes:
# a)Agregar "jugo"a la lista del tercer cliente usando append.
# b)Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c)eliminar "pan" de la lista del primer cliente
# d)imprimir la lista resultante por pantalla

compras = [["pan", "Leche"], ["arroz", "fideos", "Salsa"],["agua"]]

# compras_cliente1 = compras[1]
# compras_cliente1.remove("pan")
compras.remove("pan")
compras_cliente2 = compras[2]
compras_cliente2[1] = "tallarines"
compras_cliente3 = compras[3]
compras_cliente3.append("jugo")

compras = compras_cliente1 + compras_cliente2 + compras_cliente3

print(compras)