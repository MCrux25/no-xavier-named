import os
from playsound import playsound
from PIL import Image
import time, msvcrt

class gatx:
    def __init__(self,name,sex,type,personality):
        print (f'Generando un gatx llamadx {name}, {sex}, de tipo {type}, y con una personalidad {personality}')
        ##atributos de instancia
        self.name = name
        self.sex = sex
        self.type = type
        self.personality = personality
 
    
    def maulla(self,maullidos):
        
        sum = 0
        i= 1
        #maullidos = int(maullidos)
        while i <= maullidos:
            sum = sum + 1
            i = i + 1            
            if self.personality == "amigable":    
                print (f"Miaw {sum}")
                playsound ('recursos/sonidos/amigable.mp3')
            elif self.personality == "verguerx":
                print (f"Iggggg {sum}")    
                playsound ('recursos/sonidos/verguera.mp3')
            elif self.personality == "solitarix":
                print (f"Meaw {sum}")    
                playsound ('recursos\sonidos\solitario.mp3')
            elif self.personality == "jugueton(a)":
                print (f"M i a u {sum}")    
                playsound ('recursos\sonidos\jugueton.mp3')
            elif self.personality == "mamon(a)":
                print (f"Miau con desprecio {sum}")    
                playsound ('recursos\sonidos\mamon.mp3')

    def camina(self, pasos):
        if self.sex == "macho":            
            print(f"Caminando {pasos} pasos")            
            m = Image.open("recursos\imagenes\macho.jpg")
            m.show()
        elif self.sex == "hembra":
            print(f"Caminando {pasos} pasos")            
            h = Image.open("recursos\imagenes\hembra.jpg")
            h.show()
        elif self.sex == "te vale":
            print(f"Caminando {pasos} pasos")            
            alv = Image.open("recursos/imagenes/alv.jpg")
            alv = alv.convert('L')
            alv.show()
        
    
    def ronronea(self,ronroneo):
        sum = 0
        i= 1        
        while i <= ronroneo:
            sum = sum + 1
            i = i + 1
            print (f"Prrr {sum}")            
            playsound ('recursos\sonidos\gato_ronroneo.mp3')

    def dormir(self):
        t0 = time.time()
        t0 = int(t0)
        print("DURMIENDO...")
        msvcrt.getch()
        t1 = time.time()
        t1 = int(t1)
        print(f"Dormiste por {t1-t0} segundos")