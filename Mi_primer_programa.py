nombre1 = input ("Bienvenido al programa para calcular tu nota final, ¿Cuál es tu nombre?")
print ("Bienvenido " + nombre1)
print ("""Por favor, ingresa la nota de tu primera evaluación 
recuerda que ésta vale el "40 %" de tu calificación
""")
nota1 = int(input ("Primera evaluación= ")) * 0.4
print ("La nota que ingresaste equivale al " + str(nota1) + " %" + " de tu calificación")
print ("""Por favor, ingresa la nota de tu segunda evaluación 
recuerda que ésta vale el "60 %" de tu calificación
""")
nota2 = int(input ("Segunda evaluación= ")) * 0.6
print ("La nota que ingresaste equivale al " + str(nota2) + " %" + " de tu calificación")
notafinal= nota1 + nota2
print ("Tu nota final es= " + str(notafinal))
print ("Muchas gracias por tu esfuerzo.")