import os
os.system("cls")

print ("Este programa le permitirá conocer si un año es, ha sido, o será bisiesto. En caso de que lo necesite")


año =  0
def anobis(año):
    while True:
        año = input("Ingrese el año:\n")
        if año.isnumeric():
            añob = int(año)
            if añob%4 == 0 and añob%100 != 0:
                print (f'{añob} es bisiesto')
                break
            elif añob%4 == 0 and añob%100 == 0 and añob%400 == 0:
                print (f'{añob} es bisiesto')
                break
            else:
                print (f'{añob} no es bisiesto')
                break           
        else:
            print (f'El dato ingresado no es un número, por favor ingresa un número')
        
anobis (año)