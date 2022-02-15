print("Conjuntos")
#No se puede ordenar y no se duplican valores
conjunto_paises = ['Mexico', 'Francia', 'Colombia', 'Argentina', 'UK']
numeros = [1,1,1,1,2,2,2,3,4,5,6,7,7,8]
print(len(numeros))

#Creando Conjuntos
conjunto_numeros = set(numeros)
print(conjunto_numeros)
print(len(conjunto_numeros))

#Otra forma de crear
conjunto_exportaciones = {1,2,3,4,5,6,6,1,1}
print(conjunto_exportaciones)


#Agregar
conjunto_numeros.add(56)
print(conjunto_numeros)

#Eliminar
conjunto_numeros.pop()
print(conjunto_numeros)

conjunto_numeros.remove(56)
print(conjunto_numeros)

#Métodos
#Diferencia
top_num = {1,2,56,78,89,887}
diferencia = conjunto_numeros.difference(top_num)
print(diferencia)

#Intersección
interseccion = conjunto_numeros.intersection(top_num)
print(interseccion)

#Union
union = conjunto_numeros.union(top_num)
print(union)