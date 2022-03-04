# son similares a la lista 
# pero con la diferencia que en lugsar de acceder a los elementos de un diccionario
# vamos a utlizar strings y no numeros como se lo hace 
# en las lista 

diccionario = {
    "nombre": "chanchito feliz",
    "raza": "Persa",
    "Edad":5
}
print(diccionario)

# quiero acceder a un valor del diccionario 
print(diccionario['nombre'])
print(diccionario['raza'])

# tambien se puede utilizar un metodo para acceder a los valores 
print(diccionario.get('nombre'))

#  si me gustaria cambiar el nombre para
diccionario['nombre']='Fluffy'
print('más los datos cambiados es:-> ',diccionario)

print('el tamaño o la cantidad de elementos que contiene es:',len(diccionario))

# vamos agregar valor en el diccionario

diccionario['ronronea']= 'Si'
print(diccionario)
diccionario.pop('ronronea')
print(diccionario)
diccionario['ronronea']= 'Si'
print(diccionario)

# otra forma de eliminar 
diccionario.popitem() # elimina el ultimo valor agrado sea el que sea
print(diccionario)
diccionario['ronronea']= 'No'
print(diccionario)
print('otra forma es usar la palabra reservada del')
del diccionario['ronronea']
print(diccionario)

# generamos copia de diccionario 

copaigatito = diccionario.copy()
diccionario['ronronea']= 'No'
del diccionario['ronronea']
print(copaigatito,diccionario)
diccionario.clear()
# de esa manera elimino todo lo que esta en ese diccionario 
print('diccoinario limpio',diccionario)
print('diccionario copiado',copaigatito)

# otra forma para generar copias de undiccionario

diccionario = dict(copaigatito)

print('usando metodo dic para copiar ',diccionario)


#***************************************************************************
for i in range(5):
    print('.')

# coleccion de mas diccionarios 


gatitos = {
    "Fluffy":{
        "nombre": "Fluffy",
        "edad": 4
    },
    "Manba":{
        "nombre":"black Mamba",
        "edad": 12
    }
}

print('la coleccion de diccionarios es : ')
print(gatitos)
print(gatitos["Fluffy"])

print('otra forma que tenemos de almacenar datos es mediante variables ')

fluffy = {
    "nombre": "Fluffy",
    "edad": 4
}
manba = {
    "nombre":"black Mamba",
    "edad": 12
}

gatitos = {
    "Fluffy":fluffy,
    "Manba":manba
}
print('la coleccion almacenada mediante varibles',gatitos)


#***************************************************************************
for i in range(5):
    print('.')

# otra forma para poder crear diccionarios es mediante
# el contructor dict
# puede existir más formas de crear diccionarios

perritos = dict(nombre="Chanchito Feliz",edad = 5)
print(perritos)