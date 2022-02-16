print('Return')

paises = [
  {'pais': 'Mexico', 'fecha': 2019, 'exp': (4930, 2045, 4836)},
  {'pais': 'Canada', 'fecha': 2019, 'exp': (4782, 6984, 47059, 7365)},
  {'pais': 'Brasil', 'fecha': 2018, 'exp': (85704, 74632)},
  {'pais': 'China', 'fecha': 2019, 'exp': (4730, 4856, 6934,12820)},
  {'pais': 'Japon', 'fecha': 2018, 'exp': (19314, 4183, 4580, 4750)}
]


def promedio_exp(pais):
  if len(pais['exp']) == 0:
    return "No hay exportaciones"
  else: 
    return sum(pais['exp'])/ len(pais['exp'])
  

def nombre_pais(pais):
  nombre = pais['pais']
  return nombre

def mostrar_info(pais):
  nombre = nombre_pais(pais)
  promedio = promedio_exp(pais)
  print(f'Exportaciones promedio en {nombre}: {promedio}')


for pais in paises:
  mostrar_info(pais)


#Ejemplo
print(".")
def operacion(numero):
  return numero, numero*2, numero*3

print(operacion(2))

#Ejemplo

valor = 15

def sumar(a,b):
 suma = a + b
 return valor + suma

resultado = sumar(10,5)
print(resultado*2)