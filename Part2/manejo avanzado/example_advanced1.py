print('Manejo avanzado')

#Importar el csv
import csv

totales = []

#Ruta del archivo csv
path = '/Users/dianalaura/Desktop/Emtech/EmtechRepositoryPython/Part2/manejo avanzado/exportaciones2020.csv'

#Abrir con with
with open(path,'r') as archivo_csv:
    lector = csv.reader(archivo_csv)

    for linea in lector:
      print(linea[2])
      if linea[2] == 'total':
          continue

      totales.append(int(linea[2]))

print(totales)
print('La suma es ',sum(totales))

#Total de exportaciones a más de un país desde méxico
#Diccionarios
exp_mexico = []

with open(path,'r') as archivo_csv:
    lector = csv.DictReader(archivo_csv)

    for linea in lector:
        print(linea)
        if linea['origen'] == 'mexico':
            exp_mexico.append(int(linea['total']))



totales_mexico = sum(exp_mexico)
print(exp_mexico)
print(f'Exportaciones totales de México {totales_mexico}')
