##Tipo de datos boleanos, operadores lógicos cuyos únicos valores pueden ser Verdadero o Falso   (boolean)
#                                                                                1        0     (binario) 
# == igual a 
capArg = "Buenos Aires"
respuesta = input ("¿Cuál es la capital de Argentina?\n") 
print (capArg == respuesta)
# != distinto de
print (capArg != respuesta)

## > mayor que, < menor que, >= mayor que o igual, <= menor que o igual
num1 = int(input("Vamos a jugar, dame dos números. \n Número 1: \n"))
num2 = int(input("Número 2: \n"))
print (num1 > num2)
print (num1 < num2)
print (num1 >= num2)
print (num1 <= num2)

## operaciones lógicas
#not (negación), and "y" (todo lo que se señale debe ser verdadero), or "o" 
print (not 1 == 1)
print ( 2 > 1 and 5 > 2)
print ( 2 > 1 or 1 > 2)
nombre1 = input("Cuál es tu nombre? \n")
edad1 = int(input("¿Cuál es su edad?\n"))
lista = [
    nombre1 == "Juan", nombre1 != "****", edad1 > 10 and edad1 <30,
    len (nombre1) >= 3 and len (nombre1) < 10,
    edad1 * 4 > 40
]
print (lista [0])
print (lista [1])
print (lista [2])
print (lista [3])

##Operadores de asignación
# = valor a asignar a la variable
a = 10
# += valor a sumar a la variable
a += 15
# -= valor a restar a la variable
a -= 4
# *= valor a multiplicar a la variable
a *= 2
# /= valor con el que se dividira a la variable
a /= 3
# %= residuo de dividir la variable ente el valor  
a %= 7
# **= valor al que se potenciará la variable
a **= 2