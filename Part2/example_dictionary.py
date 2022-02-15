print("Diccionarios")

lista_exportaciones = [3274, 1325, 2254, 534, 6954, 7784, 8414, 7784, 425, 165, 7784]

exportaciones = {'Enero': 3274, 'Febrero': 1325, 'Marzo': 2254, 'Abril':534, 'Mayo': 6954, 'Junio': 7784, 'Julio': 8414, 'Agosto': 7784, 'Septiembre':425, 'Octubre': 165, 'Noviembre': 7784 } 

#Operaciones

#Buscar
print(exportaciones['Marzo'])

#Insertar
exportaciones['Diciembre'] = 6555
print(exportaciones)

#Eliminar
del(exportaciones['Enero'])
print(exportaciones)

#Si se repite, se actualiza el valor

#Diccionario con listas
exportaciones[2018] = [520, 630, 120]
print(exportaciones)

#Diccionario dentro de otro diccionario
exportaciones[2019] = {'Enero': 3, 'Febrero': 1, 'Marzo': 2}
print(exportaciones)

print('Estructura Avanzada')
#Estructuras avanzadas
exp2019 = {'Enero': 31, 'Febrero': 12, 'Marzo': 23}
exp2018 = {'Enero': 39, 'Febrero': 14, 'Marzo': 27}
exp2017 = {'Enero': 34, 'Febrero': 13, 'Marzo': 29}
exp2016 = {'Enero': 33, 'Febrero': 15, 'Marzo': 236}


exportaciones_totales = [
  {'Enero': 31, 'Febrero': 12, 'Marzo': 23},
  {'Enero': 39, 'Febrero': 14, 'Marzo': 27},
  {'Enero': 34, 'Febrero': 13, 'Marzo': 29},
  {'Enero': 33, 'Febrero': 15, 'Marzo': 236}
]


#Otra forma
""""
exportaciones_totales.append(exp2019)
exportaciones_totales.append(exp2018)
exportaciones_totales.append(exp2017)
exportaciones_totales.append(exp2016)
"""
print(exportaciones_totales)
print("______")
print(exportaciones_totales[0])
print(exportaciones_totales[1]['Marzo'])

#Función dict
datos = [('Enero', 50), ('Febrero', 4534), ('Marzo', 3535)]

datos_meses = dict(datos)
print(datos_meses)