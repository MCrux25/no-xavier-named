class gatx:
    def __init__(self,name,sex,type,personality):
        print (f'Generando un gatx llamadx {name}, {sex}, de tipo {type}, y con una personalidad {personality}')
        ##atributos de instancia
        self.name = name
        self.sex = sex
        self.type = type
        self.personality = personality
    
    def maulla(self,maullidos):        
        print("Miau "*maullidos)
    
    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")