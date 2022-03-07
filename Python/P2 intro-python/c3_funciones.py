# palabra reservada def

def miFuncion():
    print('Mi primera funcion')
    print('se acaba de imprimri mi primera funcion')

# llamo a la funcion 
miFuncion()
# ******************************

def imprimeDato(argumento):
    print('Mi argumento es ->',argumento)

imprimeDato('parametro 1')# las funciones pueden tener los argumentos que nosotros queramos   
# el valor que lle pasamos cuanto es parentecis es un parametro 
# pero cuando hacemos referencia dentro de la funcion se llama argumento 


def imprimeNombres(nombre,apellido):
    print('Nombre completo es  ->', nombre,apellido)



# siempre tenemos que pasar todos los parametros que defiinimos la función 
imprimeNombres('Chanchito','Feliz')


# pasar mas argumentos variables

def imprimeNuevoDato(*nombre):
    print('Nombre completo es  ->', nombre)

imprimeNuevoDato('Chanchito','Feliz','lala','lolo') # el cual se imprime como una tupla 


# formas de accedear a los argumentos de la funcion de

def imprimeNuevoDato1(*nombre):
    print('Nombre completo es  ->', nombre[2])

imprimeNuevoDato1('Chanchito','Feliz','lala','lolo') # el cual se imprime como una tupla 

def nombreCompleto(apellido,nombre):
    print(nombre,apellido)

# si no recuerdo el nombre del argumento o en la posicion en la que se encuentra
# puedo buscarlo mediante el nombre que yo el proporcione 

nombreCompleto(nombre ='Chanchito',apellido ='Feliz')



def nombreCompleto2(**kwargs):# agrupar todos los argumentos de una funcion como que si fuese un diccionario
    print(kwargs['nombre'],kwargs['apellido']) 
# argumanto por llave más o menos 

# puedo acceder a los argumentos utilizando la sintaxis de los diccionarios 
nombreCompleto2(nombre ='Chanchito',apellido ='Feliz')