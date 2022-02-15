print('Argumentos')

exp2019 = [3274, 1325, 2254, 534, 6954, 7784, 8414, 7784, 425, 6555]

def agregar(lista):
  exportaciones = int(input('Ingresa las exportaciones realizadas: '))
  lista.append(exportaciones)
  lista.sort(reverse= True)
  print(lista)

agregar(exp2019)
print('Otro ejemplo')
agregar([50,1545,22,22,444,55,222,44])


#Otro ejemplo
paises = [
  {'pais': 'Mexico', 'fecha': 2019, 'exp': (4930, 2045, 4836)},
  {'pais': 'Canada', 'fecha': 2019, 'exp': (4782, 6984, 47059, 7365)},
  {'pais': 'Brasil', 'fecha': 2018, 'exp': (85704, 74632)},
  {'pais': 'China', 'fecha': 2019, 'exp': (4730, 4856, 6934,12820)},
  {'pais': 'Japon', 'fecha': 2018, 'exp': (19314, 4183, 4580, 4750)}
]

""""
def promedio_exp(pais_a_calcular, fecha_para_calcular):
  if pais_a_calcular['fecha'] == fecha_para_calcular:
    nombre = pais_a_calcular['pais']
    exportaciones = pais_a_calcular['exp']
    promedio = sum(exportaciones)/ len(exportaciones)
    print(f'Exportaciones promedio en {nombre}: {promedio}')

"""
#Argumentos por nombre

""""
for pais in paises:
  promedio_exp(pais,2018)
"""
""""
for pais in paises:
  promedio_exp(fecha_para_calcular = 2019, pais_a_calcular = pais)
"""

#Parametros por defecto

def promedio_exp(pais_a_calcular = paises[0], fecha_para_calcular = 2019):
  if pais_a_calcular['fecha'] == fecha_para_calcular:
    nombre = pais_a_calcular['pais']
    exportaciones = pais_a_calcular['exp']
    promedio = sum(exportaciones)/ len(exportaciones)
    print(f'Exportaciones promedio en {nombre}: {promedio}')


for pais in paises:
  promedio_exp()