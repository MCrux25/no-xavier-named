import persona

Persona = persona.Persona

class Alumno (Persona):
    def __init__(self, numEstudiante= None, id = None, nombre=None, apellido=None, edad=None, sexo=None, comision = None):
        super().__init__(id, nombre, apellido, edad, sexo)
        self.numEstudiante = numEstudiante
        self.comision = comision
    
    def setAlumno (self):
        with open('./recursos/alumno.txt','a') as alumno:
            alumno.write(f'{self.numEstudiante}|{self.id}|{self.comision}|\n')
            alumno.close()
        return True

    def getAlumno(self, numEstudiante):
        with open('./recursos/alumno.txt','r') as alumnos:
            for alumno in alumnos:
                detalles = alumno.split('|')
                if numEstudiante == detalles[0]:                
                    MyPersona = Persona ()
                    dataAlumno = MyPersona.getPersona(detalles[1])
                    return detalles + dataAlumno
            else:
                alumnos.close()
                return False


        pass
