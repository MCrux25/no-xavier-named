from django.http import HttpResponse
from django.template import Template, Context

def saludo (request):
    return HttpResponse("Hola mundo")

def segundavista (request):
    return HttpResponse('<div style="background-color: blue; width: 100%; height: 100%; position: absolute; color: white; border : 0px; margin: 0px">Hola equipo coder</div>'
)

def minombre (self,nombre):
    documentotexto = f'Mi nombre es {nombre}'
    return HttpResponse(documentotexto)

def template(self):
    mihtml = open(r'C:\Users\Misaldazo\Documents\Coder\Coder\django1\django1\templates\index.html')
    planilla = Template(mihtml.read())
    mihtml.close()
    micontexto = Context()
    documento = planilla.render(micontexto)
    return HttpResponse(documento)
