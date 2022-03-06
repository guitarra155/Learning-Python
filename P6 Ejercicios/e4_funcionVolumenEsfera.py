# escribir una funcion que devuelva el volumen de una esfera por u radio 
import math

def volumen():
    radio = int(input('ingrese el valor del radio '))
    volumen = (4/3)*(math.pi)*(math.pow(radio,3))
    print('El volumen de la esfera es el siguiente -> ',volumen)

volumen()