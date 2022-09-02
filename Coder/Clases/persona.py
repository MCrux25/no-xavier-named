class Persona:
    def __init__(self, id=None, nombre=None, apellido=None, edad=None, sexo=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

    def setPersona(self):
        with open('Coder/recursos/persona.txt', 'a') as persona:
            persona.write(f'{self.id}|{self.nombre}|{self.apellido}|{self.edad}|{self.sexo}|\n')
            persona.close()
        return True

    def getPersona(self, id):
        with open('Coder/recursos/persona.txt', 'r') as personas:
            for persona in personas:
                detalles = persona.split('|')
                if id == detalles[0]:
                    personas.close()
                    return detalles
            else:
                personas.close()
                return False
