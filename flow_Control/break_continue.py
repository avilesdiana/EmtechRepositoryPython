#Class Break Continue

#Detener línea de producción  en cuanto lea defectuoso
autos = ['correcto', 'correcto', 'correcto', 'defectuoso', 'correcto','defectuoso', 'correcto']

for estado in autos:
  if estado == 'defectuoso':
    print('AUTO DEFECTUOSO REVISAR, deteniendo linea de producción')
    break

  print('Este auto esta ' + estado)

"""
Este auto esta correcto
Este auto esta correcto
Este auto esta correcto
AUTO DEFECTUOSO REVISAR
"""
print('-------------------------------')
autos1 = ['correcto', 'correcto', 'correcto', 'defectuoso', 'correcto','defectuoso', 'correcto']

for estado1 in autos1:
  if estado1 == 'defectuoso':
    print('AUTO DEFECTUOSO, enviado a revisión')
    continue

  print('Este auto esta ' + estado1)
  print('Enviado para distribución')

"""

Este auto esta correcto
Enviado para distribución
Este auto esta correcto
Enviado para distribución
Este auto esta correcto
Enviado para distribución
AUTO DEFECTUOSO, enviado a revisión
Este auto esta correcto
Enviado para distribución
AUTO DEFECTUOSO, enviado a revisión
Este auto esta correcto
Enviado para distribución

"""

