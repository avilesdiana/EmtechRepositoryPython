#Class while
"""
carrito_compras = ['Tablet', 'Smartwatch']
ver_carrito = input('¿Desea ver su carrito de compras? (si/no)')
n_veces = 0

while ver_carrito == 'si' and n_veces < 7:
  print(carrito_compras)
  n_veces += 1
  print(n_veces)

print('Fin del bucle while')
"""


# other example
carrito_compras = []
agregar_carrito = input('¿Desea agregar un producto a  su carrito de compras? (si/no)')

while agregar_carrito == 'si':
  nuevo_producto = input('Ingresa el nuevo producto: ')
  carrito_compras.append(nuevo_producto)
  agregar_carrito = input('Deseas agregar otro producto: (si/no): ')

print(carrito_compras)




