import os
os.system("cls")

print ("Este programa le permitirá conocer si un año es, ha sido, o será bisiesto. En caso de que lo necesite")

año = int(input("Ingrese el año:\n"))

# while (año.isnumeric()) == true:
def anobis(año):
    if ((año % 4) == 0):
        print (f'El {año} es bisiesto')
        if ((año <100) and (año % 400) == 0):
            print (f'El {año} es bisiesto')
    else:
        print (f'El {año} no es bisiesto')       
# else:
#     print (f'El dato ingresado no es un número, por favor ingresa un número: ')

anobis (año)