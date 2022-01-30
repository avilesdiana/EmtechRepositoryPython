
#List
productos = ["Cereal", "Leche", "Jugo"]
numeros = [1, 2, 3]
cosas = ["Diana", 1, 1.6, "Aviles e"]

print(productos + cosas)
print(productos[1]+ " " + cosas[3])

#Imprimir la cantidad de productos
print(len(productos))

#Listas dentro de otras listas
husbandos = [["Inuyasha", 50], ["Eren",34], ["Sasuke", 16] ]
print(husbandos)
print(husbandos[1][1])

#Agregar a la lista
productos.append("Arroz")
print(productos)

husbandos.append(["Shoto",16])
print(husbandos)

#Eliminar de la lista
husbandos.remove(["Inuyasha",50])
print(husbandos)
