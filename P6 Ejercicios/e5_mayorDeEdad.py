# escribir una funciòn que indique que el usuario es mayor de edad 
def edad():
    age = int(input('ingrese la edad que registra en estos momentos-> '))
    if age <=18 and age >= 0:
        print('El usuario es un menor de edad ->',age)
    elif age >18 and age >= 0 and age <= 150:
        print('El usuario es un Adulto -> ',age)
    elif age < 0:
        print('El usuario ingreso incorrectamente la edad')


edad()