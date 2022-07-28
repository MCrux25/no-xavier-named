# ###SET (conjuntos)
# ##diferencias entre lista, tupla y set
# lista = [1,1,2,3,4,5]
# tupla = (1,1,2,3,4,5)

# print (lista,"\n",tupla)
# ##OJO
# miset = {1,1,2,3,4,5}

# print (miset)
# ## set vacío, set puede alamacenar datos de cualquier tipo
# ## no puedes almacenar datos mutables: listas, diccionarios, SÍ tuplas
# variable1 = "Popo"
# ## el set ordena los datos de forma irdenada
# Set1 = set ((15,2,4,5,"hola mundo",variable1))
# print (Set1)
# miset = {1,1,2,3,4,5}
# ## .add permite agregar nuevos ítems al set
# miset.add(10)
# ## también puedes realizar operaciones aritméticas al ítem
# miset.add(5*48)
# ## .update permite agregar varios elementos al set
# lista1 = ["el jamón es lo máximo",6,7,9,"prro"]
# miset.update(lista1)
# print (miset)
# print (len(miset))
# ## .discard y .remove, sirven para quitar elementos del set
# miset.discard("jamón")
# ## brinca error porque el ítem no está en el set
# #miset.remove("jamón")
# ## in para saber si un ítem está en un set
# if "jamón" in miset:
#     print ("Si existe jamón dentro del set")
# else: 
#     print ("No existe jamón dentro del set")
# ## .clear limpiar elementos del set
# miset.clear()
# print (miset)
# ## .pop para eliminar elementos del set, sin embargo, no se puede 
# ##  indexar como en las listas
# miset = {"misael",1,2,4,5,3,"apato"}
# while miset:
#     print ("Se está borrando: ",miset.pop())

### DICCIONARIOS
## coleccion no ordenada, con claves para identificar los elementos
## (tipo indexado), la clave puede ser cualquier objeto no mutable
## pero los valores podrían ser mutables o inmutables

midict = {"yellow":"amarillo","brown":"café","azul":"blue","popo":"comes"}
print (midict["yellow"])
##se pueden asignar valores a las claves con el input
midict["comes"] = input("comes\n")
##se pueden hacer operaciones en asignación
midict["comes"] *= 2
print (midict["comes"]) 
## .update actualiza un diccionario añadiendo los pares clave-valor
midict.update (shit = "caca")
## del eliminar valores
del midict["popo"]
## .pop permite eliminar elementos específicos, usando la clave 
## como index
midict.pop("yellow")
print (midict)

##Caso de uso de la vida Real sets
#Imaginemos que vamos a una convencion internacional de programadores
#Y queremos saber que paises nos visitaron
#Senso donde el usuario escribe
seguir = "SI"
mySetPais = set()
myListaPais = []

while (seguir.upper() == "SI"):
    pais = input("Pais: ")
    seguir = input("Desea seguir??? Escriba SI o NO\n")
    mySetPais.add(pais.upper())
    myListaPais.append(pais)
### recuerda que el set no tiene valores repetidos y set sí,
### ojo con el conteo
print(f"Asistieron {len(mySetPais)} paises a la convecion")
print(f"Asistieron {len(myListaPais)} paises a la convecion")
print("################### SET ############################")
for indice, pais in enumerate(mySetPais):
    print(f"{indice+1}.- {pais}")
###recuerda que el set no tiene valores repetidos y set sí
print("\n################## LISTA ###########################")
for indice, pais in enumerate(myListaPais):
    print(f"{indice+1}.- {pais}")

#Caso de uso de la vida Real dic
#Imaginemos que vamos a la misma convencion internacional de programadores
#Y queremos saber datos de quienes nos visitaron
#Senso donde el usuario escribe
mas = "SI"
ListaPersonas = []
#persona = {}

while (mas == "SI"):
    #persona.clear()
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    pais = input("Pais: ")
    edad = int(input("Edad: "))
    ####intentar poner condicional para que sólo acepte strings que
    #### tengan la estructura ""@"".com
    correo = input("Correo: ")
    #persona.update({"nombre": nombre, "apellido":apellido,"pais":pais,"edad":edad,"correo":correo})
    ListaPersonas.append({"nombre": nombre, "apellido":apellido,"pais":pais,"edad":edad,"correo":correo})
    print(ListaPersonas)
    mas = input("Otro usuario (SI o NO): ").upper() #lower

for persona in ListaPersonas:
    print(persona)

buscar = input("Buscar persona por nombre: ")

for persona in ListaPersonas:
    if (persona["nombre"].upper() == buscar.upper()):
        print("Persona encontrada!!!")
        print(persona)
        break
else:
    print("Persona no encontrada!!!")
