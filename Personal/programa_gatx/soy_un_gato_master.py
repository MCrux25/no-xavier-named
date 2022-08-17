import os
os.system("cls")
from gato import gatx
print ("Bienvenido a este programa, con él podrá ser un gatx")
name = input("¿Cómo te gustaría llamarte?:\n")
sex = input("""¿Te gustaría ser gato o gata?
            m = macho
            h = hembra
            alv= te vale\n""")
if sex == "m":
    sex = "macho"
elif sex == "h":
    sex = "hembra"
elif sex == "alv":
    sex = "te vale"
type = input("""Qué tipo de gatx te gustaría ser?
            a: atigradx
            b: negrx
            c: egipcix (sin pela, como cholo
            d: siamés
            e: electrico\n""")
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

maullidos = int(input("¿Cuántas veces quiere maullar?\nIngrese un número entero:\n"))
gatx1.maulla(maullidos)
