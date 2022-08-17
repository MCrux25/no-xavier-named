####controladores de flujo
## While, se basa en repertir un bloque de código a partir de evaluar una condición lógica, siempre que ésta sea True.
## Si no se determina la condición en la que sería False, esta repetición seguirá ejecutandose en un bucle infinito.
#Ejemplo 1 (ejecuta un bucle en el que se le resta 1 a la variable num, hasta que deje de ser mayor a 0)
# num = 5

# while num > 0:
#     print (f'{num}')
# ##Esto señala que se le restará 1 a num cada que se ejecute el bucle de while
#     num -= 1
# print ("terminó el conteo")
##while-else sirve para ejecutar una cadena de código cuando el bucle while tenga una condición False o haya terminado y no haya sido forzado a salir
##mediante un break (frena el bucle while en el momento en que se cumpla la condición if,
#aunque en realidad rompe el ciclo en cualquier momento en que se señale),
#else añade la condición False (cuando se deja de cumplir chance <= 3).
# chance = 1
# while chance <= 3:
#     txt = input ("Escribe SI")
#     if txt == "SI":
#         print ("Ok, lo conseguiste en el intento", chance) break
#         chance += 1
#     else: print ("Has agotado tus tres intentos")
##Desafio genérico. (el ciclo while se repetirá hasta que se ingrese el cero, y se mostrará la suma de los números ingresados)
# numero = int(input("ingresa un número: \n"))
# suma = 0
# while numero != 0:
#     suma += numero
#     #suma = suma + numero
#     numero = int(input("ingresa un número: \n"))
# else:
#     print (f'la suma de los números que ingresaste es {suma}')
###instrucciones en el bucle (break continue, pass), para señalar condiciones externas que influyan en el ciclo
##(frena el bucle while en el momento en que se cumpla la condición externa,
##aunque en realidad rompe el ciclo en cualquier momento en que se señale)
##continue (cuando n vale dos imprimirá "contunuamos..." y seguirá ejecutando el ciclo while hasta que n < 10 y ahí imprimirá "n vale , n"),
# si se hubiera sado un break, hubiera terminado el ciclo cuando n == 2.
# n = 0
# while n < 10:
#     n += 1
#     if (n == 2):
#         print ("continuamos con la siguiente iteración")
#         continue
#     print ("n vale ", n)
##pass (deja pasar la condición dada y sigue ejecutando el ciclo hasta que se cumpla la condición dada al while)
# n = 0
# while n < 10:
#     n += 1
#     if (n == 2):
#         print ("continuamos con la siguiente iteración")
#         pass
#     print ("n vale ", n)
###for (hace iteraciones conociendo el número de repeticiones que se tienen), se utiliza para
###recorrer los elementos de un objeto iterable (lista, tupla, etc.)
##ejemplo
# lista = [0,1,2,3,4]

# for num in lista:
#     print("soy un valor de la lista y valgo", num)
#     num *= 5
#     print("soy un valor de la lista y valgo", num)

##ejemplo modifica valores de una lista, los multiplica por 5, ya que numeros [indice] *= 5 modifica el valor de la lista
# numeros en el index que valga indice
# indice = 0
# numeros = [0,1,2,3]
# for numero in numeros:
#     numeros [indice] *= 5
#     indice += 1
# print (numeros)
###enumerate sirve para enumerar los valores iterables en un ciclo for
# lista = [66, 15,154]
# #----
# for indice, numero in enumerate (lista):
#     print (f'indice:  {indice}')
#     print (f'numero: {numero}\n\n')

#     print (f'-------> {lista[indice]}\n\n---------')
### range (indica el valor iterable (index) hasta el que se ejecutará el ciclo for), recordar slicing
##ejemplo 1 (imprimierá los valores en la lista numero [generada localmente para el ciclo for] hasta el index 10)
# for numero  in range (10):
#     print (numero)
###desafios
#crear un bucle que sume los pares del 0 al 100
# sum = 0
# for numero in range (0,101,2):
#     sum += numero
#     print (sum)
#imprimir por pantalla los números del 1 al 10 al revés
# for numero in range (10,0,-1):
#     print (numero)
# perdirle al usuario que ingrese un numero y devolver los dígitos del número
numero = input ("numero: ")
n = 0
for item in numero:
    n = len(numero)
print (f'el {numero} tiene {n} digitos')