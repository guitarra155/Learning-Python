# escribir una funcion que devuelva el volumen de una esfera por u radio 
import math

def volumen():
    radio = int(input('ingrese el valor del radio '))
    volumen = (4/3)*(math.pi)*(math.pow(radio,3))
    volumen1 = (4/3)*(math.pi)*(radio**3)
    #otra forma de elvar a un apotencia 

    print('El volumen de la esfera es el siguiente -> ',volumen)

volumen()