
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
multilinea = """Hola, bienvenida

A tu curso de python
"""

print(multilinea)

#Unión de cadenas
union_cadenas = multilinea + cadena_con_comillas
print(union_cadenas)

#Convert to string
age = 23
number_string = str(age)
print("Tu edad es: " + number_string)