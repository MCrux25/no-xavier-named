from django.http import HttpResponse
from django.template import loader


def homie(self):
    data = {'name': 'Julia', 'apellido': 'Cruz', 'zodiac':'piscis'}
    plantilla = loader.get_template('homie.html')
    documento = plantilla.render(data)
    return HttpResponse (documento)
    