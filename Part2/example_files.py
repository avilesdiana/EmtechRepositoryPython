print('Manejo de Archivos')

#Abrir

#Si esta en otro directorio tiene que ponerse la resultado
#path=diana/emtech/informacion.txt
#open(path)
#Lo más recomendable es tenerlo en la misma carpeta

path = '/Users/dianalaura/Desktop/Emtech/EmtechRepositoryPython/Part2/informacion.txt'
path2 = '/Users/dianalaura/Desktop/Emtech/EmtechRepositoryPython/Part2/archivo_escritura1.txt'
archivo = open(path,'r')


"""
#Obtener el contenido
contenido = archivo.read()
print(contenido)

#Para mayor contenido
contenido1 = archivo.readline()
print(contenido1)
print(archivo.readline())


#Otra forma para leer
for linea in archivo:
    print(linea)
"""


#Otra forma de leer
lista_contenido = archivo.readlines()
print(lista_contenido)

archivo.close()


#Escribir archivo
escribir_archivo = open(path2,'w')

escribir_archivo.write("Exportaciones realizadas por pais: \n")

"""
for elemento in lista_contenido:
    escribir_archivo.write(elemento)
"""
#Otra forma
escribir_archivo.writelines(lista_contenido)
escribir_archivo.close()

#Agregar
escribir_archivo = open(path2,'a')
nuevo_dato = input("Ingres anueva información: ")
escribir_archivo.write('\n' + nuevo_dato)

escribir_archivo.close()
