##Tipo de datos boleanos, operadores lógicos cuyos únicos valores pueden ser Verdadero o Falso   (boolean)
#                                                                                1        0     (binario) 
## == igual a 
# capArg = "Buenos Aires"
# respuesta = input ("¿Cuál es la capital de Argentina?\n") 
# print (capArg == respuesta)
## != distinto de
# print (capArg != respuesta)
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

