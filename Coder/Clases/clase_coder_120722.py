##Ejemplo de usar f' para concatenar##
ingrediente1= "jamón"
ingrediente2 = "queso"
#concatenar con ("texto" + variable + ... + etc)
unidades = int(input("Cuántos sandwiches de " + ingrediente1 + " con " + ingrediente2 + " desea?\n"))
#concatenar con f'
print (f'Salen {unidades} de sandwiches de {ingrediente1} con {ingrediente2}')


##Tuplas##
#definir tuplas, se usan ()
tupla1 = ("pepperoni","anchoas","quesillo")
#imprimir la posición que ocupa el elemento "quesillo" en la tupla, se puede usar en listas
print (tupla1.index("quesillo"))
#imprimir(contar) cuántas veces está el cero en la tupla, se puede usar en lista
print (tupla1.count(0))
#imprimir listado de los últimos 2 valores de la tupla, se usa en listas también, recuerda slicing
print (tupla1[-2:])

##Listas##
#definir lista, se usan []. sirve para tuplas también
lista1 = [unidades,"sandwiches de:",ingrediente1,ingrediente2,["pepperoni","anchoas","quesillo"]]
#añadir valores a lista usando +=
lista1 += ["BBQ","Ranch"]
#añadir valores a lista "aritméticamente"
lista1 = lista1 + ["queso azul","panela"]
#reasignar valores a lista
lista1 [4] = "salami"
print (lista1)
#añadir valores al final de una lista
lista1.append("frito")
print (lista1)
lista1.append(input("¿Será para llevar?\n"))
print (lista1)
#Borrar elementos de una lista, se debe señalar la posición/index del elemento a borrar
lista1.pop(int(input("""Le quitamos algo a tu sandwich?\n 
Recuerda que debes indicar el índice del elemento de la lista que se mostró,
contando de izquierda a derecho y del 0 al n \n """)))
print (f'Tu orden será {lista1}')
#convertir lista a tupla, se puede usar viceversa usando list en lugar de tuple
convertlista_a_tupla = tuple (lista1)
print (convertlista_a_tupla)
