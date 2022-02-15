print("Len y Sum")

exp2019 = [3274, 1325, 2254, 534, 6954, 7784, 8414, 7784, 425, 165, 7784, 6555]

nummero_exp = len(exp2019)
print(nummero_exp)

sum_exp = sum(exp2019)
print(sum_exp)

promedio_exp2019 = sum_exp/nummero_exp
print('El promedio de exportaciones realizadas es: ', promedio_exp2019)


#Con diccionarios
exportaciones = {'Enero': 3274, 'Febrero': 13225, 'Marzo': 2254, 'Abril': 534, 'Mayo': 6954, 'Junio': 7784, 'Julio': 8414, 'Agosto': 7784, 'Septiembre': 425, 'Octubre': 165, 'Noviembre': 7784 }


longitud = len(exportaciones)
suma = sum(exportaciones.values())

print(suma / longitud)