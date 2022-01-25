#Class if

productos_descuento = ['Computadora', 'TV', "Teclado", 'Mouse', 'Cartera', 'Monitor']
sin_stock = ['Cámara', 'Celular', 'Reloj', 'Memoria']

producto = input("Ingresa un producto: ")

""""
if producto == "Computadora" or producto == "computador" : 
  print('Ese producto si esta en descuento')
  print('Aprovecha la oferta')

elif producto =="Teclado":
  print("El teclado si esta en descuento")

else: 
  print("No tiene descuento")

print("Fin de la sentencia IF")
"""

if producto in productos_descuento: 
  print('Ese producto si esta en descuento')
  print('Aprovecha la oferta')

elif producto in sin_stock:
  print("Este producto esta agotado")

else: 
  print("No tiene descuento")

print("Fin de la sentencia IF")

#Example
resultado = False

if resultado:
  print("Correcto")
else:
  print("Incorrecto")

#Incorrecto