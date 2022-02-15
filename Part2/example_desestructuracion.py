print("Desestructuración o desempaquetados")

#Tupla
exportaciones = 850, 920
mexico, canada = exportaciones
print(mexico, canada)

china, japon = 1810, 1516
print(china)
print(japon)

#Lista
columbia, chile, brasil = [520, 630, 450]

#Lista con tupla
paises = [('Mexico', 850), ('Canada', 920), ('China', 1940)]


""""
for pais in paises:
  nombre = pais[0]
  total = pais[1]
  print(f'{nombre} realizó {total} exportaciones en 2019')
"""

#Otra forma
for nombre,total in paises:
  print(f'{nombre} realizó {total} exportaciones en 2019')