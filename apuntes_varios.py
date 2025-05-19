

# Operaciones con números

# Conversión
    # entero_a_decimal = float(123)
    # decimal_a_entero = int(22.5)
    # entero_a_complejo = complex(35)

    # print(entero_a_decimal) #Imprime: 123.0
    # print(decimal_a_entero) #Imprime: 22
    # print(entero_a_complejo) #Imprime: (35+0j)

## Aleatorios
    # import random
    # num_aleatorio = random.randint(5, 10) #Genera un número aleatorio entre 5 y 10
    # # print(num_aleatorio) #Imprime el número aleatorio generado

## Strings

    # nombre = "Gino"
    # edad = 41
    # print(f"Mi nombre es {nombre} y tengo {edad} años de edad.")
    # print("Tengo {} años de edad y mi nombre es {}".format(edad, nombre)) # Imprime: Tengo 29 años de edad y mi nombre es Marcelo
    # print("Mi nombre es %s y tengo %d años de edad." % (nombre, edad)) # Imprime: Mi nombre es Marcelo y tengo 29 años de edad.


## LISTAS

# frozen = ["Elsa", "Anna", "Olaf"]
# frozen.pop() #Sintaxis: nombre_lista.funcion()

# print(frozen) #Imprime: ['Elsa', 'Anna']


# PRACTICA 

# 1. Imprime "Hola, mundo"
# print( "Hola, Mundo" )

# # 2. Imprime "Hola, Valeria" con el nombre en una variable
# nombre = "Valeria"
# print( "Hola, {}".  format(nombre) )  # con una coma
# print( "Hola+ {}".  format(nombre) ) # con un +

# # # 3. Imprimir "Hola 156!" con el número en una variable
# numero = 156
# print( "Hola, {}!".  format(numero) ) # con una coma
# print( "Hola+ {}!".  format(numero) ) # con un + -- este debería arrojar un error!, corrígelo con conversión

# # # 4. Imprimir "Me encanta comer tacos y arepas" con las comidas en variables
# comida1 = "tacos"
# comida2 = "arepas"
# print( "Me encanta comer {} y {}" . format(comida1, comida2) ) # con .format()
# print( f"Me encanta comer {comida1} y {comida2}" ) # con una cadena f
# num1 = '5'
# num2 = 4

# print(num1 + num2)
# print( int(num1) + num2)
# print( str(num1) + str(num2) )
# print(num1 + str(num2) )


# nombre = Miyagi



# string1 = 'Hola' + 'Python'

# string2 = Hola + Python

# string3 = ‘Hola’ . ‘Python’


lista_prueba = [2, 4, 6, 7, 10]


print(lista_prueba[2])