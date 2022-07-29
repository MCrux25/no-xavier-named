############METODOS DE COLECCIONES##############
###CADENAS
# ####.lower
# cadena1 = "ID NOMBRE APELLIDO EDAD"
# print (cadena1.lower())
# ### .upper
# cadena2 = cadena1.upper()
# print (cadena2)
# ### .split
# cadena3 = cadena2.split()
# print (cadena3)
# ###replace
# cadena4 = "Hola, soy diego y vivo en Plutón, donde hace calor"
# cadena4 = cadena4.replace("diego","Misael",1)
# cadena4 = cadena4.replace("Plutón","Marte",1)
# cadena4 = cadena4.replace("calor","llueve",1)
# print (cadena4)
####LISTAS
####.clear ()    .extend()     .insert()
####.sort()   .reverse()

###Ejerciio, redistribuir cadena
# texto = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castinglione&dos pues -le corrigió Troop&strawberry menea la cabeza como disgustado... -agrega el comentarista"
# lineas = texto.split("&")
# print (lineas)

# for i, linea in enumerate(lineas):
#     lineas[i] = linea.capitalize()
#     if i == 0:
#         lineas[i] = lineas[i] + "..."
#     else:
#         lineas[i] = f"- {lineas[i]}."

# for fila in lineas:
#     print (fila) 
################SETS
# set1 = {1,2,3}
# ##.copy
# set2 = set1.copy()
# print (set2)
# ###.isdisjoint
# set3 = {3,4,5}
# print (set1.isdisjoint(set2))
# ###.issubset
# set4 = {5,6,7}
# print (set3.issubset(set4))
# ###.issuperset
# set2 = {1,2}
# print (set1.issuperset(set2))
# ####.union
# set5 = (set1.union(set2))
# print (set5)
# ###.difference
# set6 = (set3.difference(set4))
# print (set6)
######Desafio
lista0 = [29,-5,-12,17,5,24,5,12,23,16,12,5,-12,17]
##Paso 1 borrar elementos duplicados
##solución a
set1 = set(lista0)
lista1 = list(set1)
print (lista1)
##solución b (de muchas)
lista1b = list(set(lista0))
print (lista1b)
##Paso 2 ordenar de mayor a menor
lista1b.sort(reverse = True)
print (lista1b)
###Paso 3 eliminar todos los impares
##esta respuesta va recorrer los índices de la lista y
##cuando encuentre un impar va a eliminarlo, pero lo
##recorre los índices, por lo que se se encuentra otro
##impar inmediatamente no lo va a evaluar porque ese
##va a ocupar el índice del elemento que se eliminó 
for indice, item in enumerate(lista1b):
    print (f'{item} ! {item%2}')
    if ((item%2) == 1):
        lista1b.pop(indice)
print (lista1b)
