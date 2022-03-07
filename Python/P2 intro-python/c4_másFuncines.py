def miFuncion2(argumento = 'Chanchito'):
    print(argumento)

miFuncion2('Batman')
miFuncion2()

def miFuncionLista(lista):
    for elemento in lista:
        print(elemento)

miFuncionLista(['Chanchito','Feliz'])

def concatenaNombres(lista):
    i = ''
    for elemento in lista:
        i = i + ' ' + elemento + ' '
    return i
        

nombres = concatenaNombres(['Chanchito','Feliz'])

print(nombres)