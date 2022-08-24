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
            from playsound import playsound
            if self.personality == "amigable":    
                print (f"Miaw {sum}")
                playsound (r'Personal\programa_gatx\recursos\amigable.mp3')
            elif self.personality == "verguerx":
                print (f"Iggggg {sum}")    
                playsound (r'Personal\programa_gatx\recursos\verguera.mp3')
            elif self.personality == "solitarix":
                print (f"Meaw {sum}")    
                playsound (r'Personal\programa_gatx\recursos\solitario.mp3')
            elif self.personality == "jugueton(a)":
                print (f"M i a u {sum}")    
                playsound (r'Personal\programa_gatx\recursos\jugueton.mp3')
            elif self.personality == "mamon(a)":
                print (f"Miau con desprecio {sum}")    
                playsound (r'Personal\programa_gatx\recursos\mamon.mp3')

    def camina(self, pasos):
        from PIL import Image
        if self.sex == "macho":            
            print(f"Caminando {pasos} pasos")            
            m = Image.open(r'Personal\programa_gatx\recursos\macho.jpg')
            m.show()
        elif self.sex == "hembra":
            print(f"Caminando {pasos} pasos")            
            h = Image.open(r'Personal\programa_gatx\recursos\hembra.jpg')
            h.show()
        elif self.sex == "te vale":
            print(f"Caminando {pasos} pasos")            
            alv = Image.open(r'Personal\programa_gatx\recursos\alv.jpg')
            alv = alv.convert('L')
            alv.show()
        
    
    def ronronea(self,ronroneo):
        sum = 0
        i= 1        
        while i <= ronroneo:
            sum = sum + 1
            i = i + 1
            print (f"Prrr {sum}")            
            from playsound import playsound
            playsound (r"Personal\programa_gatx\recursos\gato_ronroneo.mp3")

    def dormir(self):
        import time, msvcrt   
        t0 = time.time()
        t0 = int(t0)
        print("DURMIENDO...")
        msvcrt.getch()
        t1 = time.time()
        t1 = int(t1)
        print(f"Dormiste por {t1-t0} segundos")