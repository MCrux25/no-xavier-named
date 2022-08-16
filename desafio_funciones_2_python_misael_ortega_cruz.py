# -*- coding: utf-8 -*-
"""DESAFIO_FUNCIONES_2_Python_Misael_Ortega_Cruz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tDTFhRjkgNXhu8GZTjq2xxwoWx48SqmL

**EJERCICIO 1 //**

CONSIGNA:

Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura.


🖐 Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.
"""

b = 0
h = 0
def area_rectangulo (b,h):
  b = int(input("Ingrese la base del rectángulo del cual desea calcular el área: \n"))
  h = int(input("Ingrese la base del rectángulo del cual desea calcular el área: \n"))
  area = (f"El área del rectangulo es {b*h}")
  return area 

area_rectangulo (b,h)

"""**EJERCICIO 2 //**

CONSIGNA:

 Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio.

🖐 Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math.

"""

import math

r = 0

def area_circulo (r):
  r = int(input("Ingrese el radio del círculo del cual desea calcular el área: \n"))
  area = (f"El área del círculo es {(r**2)*(math.pi)}")
  return area 

area_circulo (r)

"""**EJERCICIO 3 //**

CONSIGNA:

Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

1 - Si el primer número es mayor que el segundo, debe devolver 1.

2 - Si el primer número es menor que el segundo, debe devolver -1.

3 - Si ambos números son iguales, debe devolver un 0.

Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

"""

def relacion(n1,n2):
  if n1 > n2:
    resultado = 1
    return resultado
  elif n1 < n2:
    resultado = -1
    return resultado
  elif n1 == n2:
    resultado = 0
    return resultado

print (relacion (5,10))

print (relacion (10,5))

print (relacion (5,5))

"""**EJERCICIO 4 //**

CONSIGNA:

Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:

🖐 Ayuda: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

**Comprueba el punto intermedio entre -12 y 24**


"""

def intermedio (na,nb):
  puntomedio = (na + nb)/2
  return puntomedio
print (intermedio (-12,24))

"""**EJERCICIO 5 //**

CONSIGNA:

Realizá una función llamada recortar() que reciba tres parámetros.

El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior.

La función tendrá que cumplir lo siguiente:

1 - Devolver el límite inferior si el número es menor que éste.

2 - Devolver el límite superior si el número es mayor que éste.

3 - Devolver el número sin cambios si no se supera ningún límite.

Comprueba el resultado de recortar 15 entre los límites 0 y 10

"""

def recortar(n,lmin,lmax):
  if n < lmin:    
    return lmin
  elif n > lmax:
    return lmax
  elif n > lmin and n < lmax:
    return n

print (recortar (15,0,10))

"""**EJERCICIO 6 //**

CONSIGNA:

Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas.


La primera con los números pares, y la segunda con los números impares:

🖐 Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()



```
Por ejemplo:
pares, impares = separar([6,5,2,1,7])
print(pares)   # valdría [2, 6]
print(impares)  # valdría [1, 5, 7]

```



"""

pares = []
impares = []
numeros = []
def separar (numeros):
  print (f'Los números a separar son:{numeros}')
  for i in numeros:
    if (i % 2) == 0:
      pares.append(i)
      pares.sort()

    elif (i % 2) != 0:
      impares.append(i)
      impares.sort()
      
  print (f'Los números pares son:{pares}')
  print (f'Los números impares son:{impares}')

print (separar ([6,5,2,1,7]))