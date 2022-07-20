##flujo continuo
#nombre = input ("Ingresar nombre: ")
#edad = int(input("Cuando nació: "))
##if (ejecuta una secuencia de cógido sólo si se cumple una condición dada)
###cuando se escriba de esta manera, el programa va a probar que cumpla cada una de las condiciones
# if (edad >= 18):                                ###if solitario
#     print ("¡Es mayor de edad!")
# if (edad >= 12):                                ###if solitario
#     print ("¡Es un adolescente!")
# if (edad >= 1):                                 ###if else (familia)
#     print ("¡Es un niño!")
# ##else sino (cumple lo que sucede si no se cumple la condición previa (if))
# else:                                           ###if else (familia)
#     print ("¡Es menor de edad!") 
# #todo lo que está fuera de la indentación ya no se contempla dentro de la condicionales
# print (edad)
#if not
#if not (edad>18):
#    print ("¡Es mayor de edad!")
###ejemplo if elif
# if (edad >= 18):
#     print ("¡Es mayor de edad!")
# elif (edad >=12):
#     print ("Eres un adolescente")
# elif edad >= 1:
#     print ("Eres un mocoso")
# else:
#     print ("Eres un bebé superdotado")
###Ejercicio genérico, preguntar al usuario su edad
# edad = int(input("Buenos días, ¿Cuál es su edad"\n))
# if (edad >= 18):
#      print ("¡Es mayor de edad!")
# else:
#     print ("No es mayor de edad")
###Ejercicio condicionales anidadas
nombre = input ("Ingresar nombre:\n ")
fandom = input ("¿Eres fan de marvel o de capcom? '(contesta con M para marvel y C para capcom)'\n")
inicial = nombre [0]

if fandom == "M" or fandom == "C":
    if inicial > "M" or inicial < "C" :
        grupo = "A"
    else:
        grupo = "B"
else:
    grupo = "B"
print (f'{nombre} perteneces al grupo {grupo}')