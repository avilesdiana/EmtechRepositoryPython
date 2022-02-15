print('Operaciones con listas')

semestre_1 = [3274, 1325, 254, 533, 6954, 7784]
semestre_2 = [8414, 7784, 425, 165, 7784, 555]

productos_exportacion = ['Computadoras', 'Tablets', 'Teclados','Smart Watch']

#Unión de listas
totales = semestre_1 + semestre_2
print(totales)

#Multiplicación
print(totales*3)

#Modificación último valor
totales[-1] = 6556
print(totales)

totales[9] = 2165
print(totales)


#Métodos

#Count - Contar
print(totales.count(7784))

#Insertar
productos_exportacion.insert(2,'Audifonos')
print(productos_exportacion)

productos_exportacion.insert(0,'Computadoras')
print(productos_exportacion)

#Eliminar
#pop - indica el indice a eliminar
productos_exportacion.pop(1)
print(productos_exportacion)

#Remove, indicar el valor a eliminar
productos_exportacion.remove('Computadoras')
print(productos_exportacion)

#sorted ordenar
totales.sort()
print(totales)

productos_exportacion.sort()
print(productos_exportacion)

productos_exportacion.sort()
productos_exportacion.reverse()
print(productos_exportacion)

#Otra forma
productos_exportacion.sort(reverse = True)
print(productos_exportacion)