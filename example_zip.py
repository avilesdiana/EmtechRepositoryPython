print("Ejemplo ZIP")

paises = ('México', "Canadá", 'China', "Japón")
importaciones = (430, 560, 310, 695)
exportaciones = (1932, 3540, 4800, 530)

agrupacion = zip(paises, importaciones, exportaciones)

print(agrupacion)
#Lista
print(list(agrupacion))

#Tupla
print(tuple(agrupacion))

#Conjuntos
print(set(agrupacion))

#Diccionario
print(dict(zip(paises, exportaciones)))

#Separar elementos
print("Sepracion")
print(list(zip(*paises)))


#combinar colecciones
for pais, exportacion in zip(paises, exportaciones):
  print(pais, exportacion)
