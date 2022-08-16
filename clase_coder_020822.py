###Escribir en archivos

####ejemlpo 1 de creación y escritura de archivos
#           Direccion                , tipo de accion
# file = open("./recursos/usuarios.txt","w") #w: write, r: read, a:append
#        #open abre el archivo o lo crea en el directorio caso de que no exista 
# file.write("Primera linea\n")
# file.write("Segunda linea\n")
# file.close()
###progama para preguntar el nombre de mascota
import os
os.system("cls")
print ("""Hola, este programa servirá para hacer una base de datos
en la que nos dirás el nombre de tu mascota""")
continuar = "SI"
while (continuar.upper() == "SI"):
    nombre = input("¿Cómo te llamas?\n")
    mascota = input('¿Cómo se llama tu mascota?\n')
    color = input ('¿De qué color es tu mascota?\n')
    continuar = input("¿Desea registrar otra mascota Escriba SI o NO\n")
    nomymasc ={"NOMBRE":nombre,"MASCOTA":mascota,"COLOR":color}
    if (continuar.upper() == "SI"):
        nomymasc.update()
    archivo = open("./recursos/mascotas.txt","a")
    archivo.write(nomymasc["NOMBRE"]+":"+nomymasc["MASCOTA"]+nomymasc["COLOR"]+"\n")
    archivo.close()
print (nomymasc)