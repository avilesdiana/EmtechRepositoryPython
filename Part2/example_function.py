print('Funciones')

def agregar():
  exp2019 = [3274, 1325, 2254, 534, 6954, 7784, 8414, 7784, 425, 6555]
  
  exportaciones = int(input('Ingresa las exportaciones realizadas: '))
  exp2019.append(exportaciones)
  exp2019.sort(reverse= True)
  print(exp2019)

def multiplicar():
  print(6*5)

#Llamado a la funcón
agregar()
multiplicar()