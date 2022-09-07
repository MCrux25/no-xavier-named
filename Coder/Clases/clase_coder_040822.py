######################FUNCIONES#####################

import os
os.system("cls")
def saludar(adjetivo):
    print (f'Hola popo {adjetivo}\n')
adjetivo = input("¿cómo te sientes? \n(usa un adjetivo)\n")
saludar(adjetivo)

#apellido = "Cruz"

# def saludar_con_parametros(nombre):
#     print ("Hola {} de la popo".format(nombre))
# ##lo mismo que
#     print (f'Hola {nombre} de la popo')


# nombre = input("Nombre: ")

# saludar_con_parametros(nombre)

# def saludar_con_parametros2(nombre):
#      saludo = f'Hola {nombre} de la popo'
#      return saludo

# nombre = input("Nombre: ")
# saludar = saludar_con_parametros2(nombre)
# print (saludar) 

# ####función Calculadora
# def suma(num1, num2, num3):
#     resultado = num1 + num2 + num3
#     return resultado
# print (suma(8,5,7))
#############función par o impar
# def par_o_impar(numero):
#     if type(numero) == int:
#         if ((numero % 2) == 0):
#             respuesta = f"el número es {numero} es PAR"
#             return respuesta
#         else:
#             respuesta = f"el número es {numero} es IMPAR"
#             return respuesta
#     else:
#         respuesta = f"{numero} no es un número"
#         return respuesta
# numero = (input("ingresa un número: "))
# print (par_o_impar(numero))
######################TRANSACCIÓN###################### complementar
# print ("TRANSACCIÓN")
# print ("O:Operador\nV:Verificador\nA:Autorizador")

# opcion = input ("Seleccione una opcion: ").upper()
# def recuperarUsuario("operador"):
#     with open("./recursos/datausuarios.txt")