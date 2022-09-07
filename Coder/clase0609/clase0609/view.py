from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Curso

def home(request):
    return HttpResponse ("Hola homie")

def homie(self):
    lista = [1,2,3,4,5,6,7,8,9]
    data = {'name': 'Julia', 'apellido': 'Cruz', 'lista':lista}
    planilla = loader.get_template('homie.html')
    documento = planilla.render(data)
    return HttpResponse(documento)

def cursos(self):
    curso = Curso(nombre='UX/UI',camada='1546')
    curso.save()
    documento = f'Curso: {curso.nombre} camada: {curso.camada}'
    return HttpResponse(documento)

