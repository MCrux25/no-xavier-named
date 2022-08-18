class gatx:
    def __init__(self,name,sex,type,personality):
        print (f'Generando un gatx llamadx {name}, {sex}, de tipo {type}, y con una personalidad {personality}')
        ##atributos de instancia
        self.name = name
        self.sex = sex
        self.type = type
        self.personality = personality
 
    def maulla(self,maullidos):        
        #for i in maullidos:
        print ("Miau "*maullidos)
            
        from pydub import AudioSegment
        from pydub.playback import play
        n = maullidos
        audio = AudioSegment.from_mp3(r'C:\Users\MisaelOrtegaCruz\Documents\Personal\no-xavier-named\Personal\programa_gatx\maullido_bebe.mp3') #your audio file
        play(audio * n)  #Play audio 2 times
            
            #from playsound import playsound
            #playsound (r'C:\Users\MisaelOrtegaCruz\Documents\Personal\no-xavier-named\Personal\programa_gatx\maullido_bebe.mp3')

    
    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")