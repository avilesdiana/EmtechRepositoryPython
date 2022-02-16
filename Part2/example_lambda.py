print('Lambda')

""""
def multiplicar(a,b):
  return a * b
"""

#Lambda
multiplicar = lambda a, b: a * b
print(multiplicar(6,5))


#Otro ejemplo
""""
def promedio(secuencia):
  return sum(secuencia) / len(secuencia) 
"""
promedio = lambda secuencia: sum(secuencia) / len(secuencia)

paises = [
  {'pais': 'Mexico', 'fecha': 2019, 'exp': (4930, 2045, 4836)},
  {'pais': 'Canada', 'fecha': 2019, 'exp': (4782, 6984, 47059, 7365)},
  {'pais': 'Brasil', 'fecha': 2018, 'exp': (85704, 74632)},
  {'pais': 'China', 'fecha': 2019, 'exp': (4730, 4856, 6934,12820)},
  {'pais': 'Japon', 'fecha': 2018, 'exp': (19314, 4183, 4580, 4750)}
]

for pais in paises:
  print(promedio(pais['exp']))