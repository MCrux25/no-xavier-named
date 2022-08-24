import os
os.system("cls")
from gato import gatx
print ("Bienvenido a este programa, con él podrá ser un gatx")
name = input("¿Cómo te gustaría llamarte?\n")
os.system("cls")
sex = input("""¿Te gustaría ser gato o gata?
m = macho
h = hembra
alv= te vale\n""")
os.system("cls")
if sex == "m":
    sex = "macho"
elif sex == "h":
    sex = "hembra"
elif sex == "alv":
    sex = "te vale"
type = input("""Qué tipo de gatx te gustaría ser?
a: atigradx
b: negrx
c: egipcix (sin pela, como cholo)
d: siamés
e: electrico\n""")
os.system("cls")
if type == "a":
    type = "atigradx"
elif type == "b":
    type = "negrx"
elif type == "b":
    type = "negrx"
elif type == "c":
    type = "egipcix"
elif type == "d":
    type = "siamés"
elif type == "e":
    type = "electrico"
personality = input("""¿Qué personalidad te gustaría tener?
1: Verguerx
2: Amigable
3: Solitarix
4: Jugueton(a)
5: Mamon(a)\n""")
os.system("cls")
if personality == "1":
    personality = "verguerx"
elif personality == "2":
    personality = "amigable"
elif personality == "3":
    personality = "solitarix"
elif personality == "4":
    personality = "jugueton(a)"
elif personality == "5":
    personality = "mamon(a)"

gatx1 = gatx(name,sex,type,personality)

options = 0

while options >= 0 and options <= 5:
    options = int(input(f'''¿{name}, qué deseas hacer?
1: Maullar
2: Caminar
3: ronronear
4: dormir
5: salir
'''))
    if options == 1: 
        maullidos = int(input(f'¿{name} cuántos maullidos quieres hacer?\nIntroduzca un número entero:\n'))
        gatx1.maulla(maullidos)
        os.system("cls")
    elif options == 2:
        pasos = int(input(f'¿{name} cuántos pasos quieres dar?\nIntroduzca un número entero:\n'))
        gatx1.camina(pasos)
        os.system("cls")
    elif options == 3:
        ronroneos = int(input(f'¿{name} cuántos ronroneos quieres hacer?\nIntroduzca un número entero:\n'))
        gatx1.ronronea(ronroneos)
        os.system("cls")
    elif options == 4:
        print(gatx1.dormir()) #no puede dormir
        os.system("cls")
    elif options == 5:
        print ('Saliendo')
        os.system("cls")
        break
    elif options > 5: #problema de lógica
        print ('Opción inválida')


# 

# def mostrar_menu(opciones):
#     print(f'¿Qué te gustaría hacer {name}?')
#     for clave in sorted(opciones):
#         print(f' {clave}) {opciones[clave][0]}')


# def leer_opcion(opciones):
#     while (a := input('Opción: ')) not in opciones:
#         print('Opción incorrecta, vuelva a intentarlo.')
#     return a


# def ejecutar_opcion (opcion, opciones):
#     opciones[opcion][1]()


# def generar_menu (opciones, opcion_salida):
#     opcion = None
#     while opcion != opcion_salida:
#         mostrar_menu(opciones)
#         opcion = leer_opcion(opciones)
#         ejecutar_opcion(opcion, opciones)
#         print()

# def menu_principal():
#     opciones = {
#         '1': ('Maullar', gatx1.maulla),
#         '2': ('Caminar', gatx1.camina),
#         '3': ('ronronear', gatx1.ronronea),
#         '4': ('dormir', gatx1.dormir),
#         '5': ('Salir', salir)
#     }
    
#     generar_menu(opciones, '5')

# def salir ():
#     print ('Saliendo')

# menu_principal()