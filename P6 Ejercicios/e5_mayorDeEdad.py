# escribir una funciòn que indique que el usuario es mayor de edad 
# def edad():
    # age = int(input('ingrese la edad que registra en estos momentos-> '))
    # if age <=18 and age >= 0:
        # print('El usuario es un menor de edad ->',age)
    # elif age >18 and age >= 0 and age <= 150:
        # print('El usuario es un Adulto -> ',age)
    # elif age < 0:
        # print('El usuario ingreso incorrectamente la edad')


# edad()


def mayor(user):
    return user.age > 18


class User():
    def __init__(self, age):
        self.age = age

num1 = int(input('ingrese la edad 1 -> '))
num2 = int(input('ingrese la edad 2 -> '))
usuario = User(num1)
usuario2 = User(num2)

resultado1 = mayor(usuario)
resultado2 = mayor(usuario2)

print(resultado1,resultado2)