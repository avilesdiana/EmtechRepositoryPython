print("Manejo de csv")

#importar modulo csv
import csv

"""
#Abrir archivo
archivo_csv = open('exportaciones2020.csv','r')
archivo_csv.close()
"""

path = '/Users/dianalaura/Desktop/Emtech/EmtechRepositoryPython/Part2/archivos csv/exportaciones2020.csv'

#Controlar procedimientos con with()
with open(path, 'r') as archivo_csv:
    #lector = csv.reader(archivo_csv, delimiter = ';')
    #Lee por línea, creando un objeto por cada uno de ellas
     
    #con diccionarios
    lector = csv.DictReader(archivo_csv)

    for linea in lector:
        print(linea)


info = [
    ('Mexico', 'cars'),
    ('Canda', 'petroleum'),
    ('United States', 'planes'),
    ('China', 'electronic'),
    ('South Korea', 'computers'),
    ('Germany', 'cars') 
]


with open(path, 'w') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(info)

#Con diccionarios
paises = [
  {'pais': 'Mexico', 'fecha': 2019, 'exp': (4930, 2045, 4836)},
  {'pais': 'Canada', 'fecha': 2019, 'exp': (4782, 6984, 47059, 7365)},
  {'pais': 'Brasil', 'fecha': 2018, 'exp': (85704, 74632)},
  {'pais': 'China', 'fecha': 2019, 'exp': (4730, 4856, 6934,12820)},
  {'pais': 'Japon', 'fecha': 2018, 'exp': (19314, 4183, 4580, 4750)}
]

path2 = '/Users/dianalaura/Desktop/Emtech/EmtechRepositoryPython/Part2/archivos csv/dict_exp.csv'
with open(path2, 'w') as archivo_dict:
    campos = ['fecha', 'pais', 'exp']
    escritor = csv.DictWriter(archivo_dict, fieldnames = campos)
    escritor.writeheader()
    escritor.writerows(paises)