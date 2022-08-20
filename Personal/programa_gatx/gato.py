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
            print (f"Miau {sum}")
            from playsound import playsound
            playsound (r".\Personal\programa_gatx\maullido_bebe.mp3")

    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")
    
    def ronronea(self,ronroneo):
        sum = 0
        i= 1
        #ronroneo = int(ronroneo)
        while i <= ronroneo:
            sum = sum + 1
            i = i + 1
            print (f"Prrr {sum}")
            from playsound import playsound
            playsound (r".\Personal\programa_gatx\gato_ronroneo.mp3")

    def dormir(self):
        print(f"Durmiendo...")
