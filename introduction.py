"""
print("My first code in Repl")

#Class Variables
#Declaring Variables

edad = 23  #name->edad, value->23
altura = 1.7
institucion = "Emtech"  #name->institucion, value->Emtech

nombre_amigo = "Juan Diego"
nombre_amigo1= "Diana"

#Print Variables
print(edad)
print(altura)
print(institucion)
print(nombre_amigo)
print(nombre_amigo1)

#Print the value directly
print("Diana Aviles")
"""

""""
#Class Numbers

suma = 6 + 5
resta = 6 + 5
multiplicacion = 6 * 5
division = 6 / 5

print (suma)
print (resta)
print (multiplicacion)
print (division)

operaciones_matematicas = 6 + 3 - 1 * 3 / 2
print(operaciones_matematicas)

#in division there is always a decimal part
division_flotante = 15 / 3
print(division_flotante)

#Convert to int
division_entera = 15 // 3
print(division_entera) #In python there is no rounding 

division_entera1 = 29 // 3
print(division_entera1) #print 9 to 9.666

"""

"""->
#Class Textos

mi_cadena = "Hola mundo"
mi_cadena2 = 'Hola mundo'

print(mi_cadena)

cadena_con_comillas = 'Diana dijo: "Hola mundo"'
print(cadena_con_comillas)

#Other form to strings with quotation marks
cadena_con_comillas2 = "Diana dijo: \"Hola mundo 2\""
print(cadena_con_comillas2)

#Multilinea
->"""


#multilinea = """Hola, bienvenida

#A tu curso de python
#"""


"""
print(multilinea)

#Unión de cadenas
union_cadenas = multilinea + cadena_con_comillas
print(union_cadenas)

#Convert to string
age = 23
number_string = str(age)
print("Tu edad es: " + number_string)
"""

""""
#Class Index and Slicing
saludo = "Hola"
print(saludo[0])
print(saludo[2])

#Negative Index
print(saludo[-1])

#Slicing
palabra = "Python"
print(palabra[0:3])
print(palabra[2:4])

#Longitud de una cadena
cadena_larga = "Mi nombre es Diana Aviles"
print(len(cadena_larga))
"""
""""
#List
productos = ["Cereal", "Leche", "Jugo"]
numeros = [1, 2, 3]
cosas = ["Diana", 1, 1.6, "Aviles e"]

print(productos + cosas)
print(productos[1]+ " " + cosas[3])

#Imprimir la cantidad de productos
print(len(productos))

#Listas dentro de otras listas
husbandos = [["Inuyasha", 50], ["Eren",34], ["Sasuke", 16] ]
print(husbandos)
print(husbandos[1][1])

#Agregar a la lista
productos.append("Arroz")
print(productos)

husbandos.append(["Shoto",16])
print(husbandos)

#Eliminar de la lista
husbandos.remove(["Inuyasha",50])
print(husbandos)
"""

"""
#Input Function
lista_productos = ["Agua"]

producto_cliente = input("Ingresa un producto: ")

lista_productos.append(producto_cliente)

print("El producto que se agrego es:  "+ producto_cliente )
print(lista_productos)


valor = int(input("Ingresa un número: "))
print( valor * 7 )

valor_float = float(input("Ingresa un número flotante: "))
print( valor_float * 7 )

""""