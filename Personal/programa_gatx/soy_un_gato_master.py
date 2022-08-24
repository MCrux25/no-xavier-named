import os
import time
os.system("cls")
from gato import gatx
print ("Bienvenido a este programa, con él podrá ser un gatx")
tiempoin = time.time()
tiempoin = int(tiempoin)
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

while options >= 0:
    options = int(input(f'''¿{name}, qué deseas hacer?
1: Maullar
2: Caminar
3: ronronear
4: dormir
5: salir
'''))
    if options == 1: 
        os.system("cls")
        maullidos = int(input(f'¿{name} cuántos maullidos quieres hacer?\nIntroduzca un número entero:\n'))
        gatx1.maulla(maullidos)
    elif options == 2:
        os.system("cls")
        pasos = int(input(f'¿{name} cuántos pasos quieres dar?\nIntroduzca un número entero:\n'))
        gatx1.camina(pasos)
    elif options == 3:
        os.system("cls")
        ronroneos = int(input(f'¿{name} cuántos ronroneos quieres hacer?\nIntroduzca un número entero:\n'))
        gatx1.ronronea(ronroneos)
    elif options == 4:
        os.system("cls")        
        print(gatx1.dormir())
    elif options == 5:
        os.system("cls")
        tiempofin = time.time()
        tiempofin = int(tiempofin)
        print (f'Fuiste un gato durante {tiempofin-tiempoin} segundos')
        print ('Saliendo...')
        print (f'Adios {name}.')
        break
    elif options > 5:
        print ('Opción inválida')
        