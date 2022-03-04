usuarios = ['Chanchito feliz ','felipe','roberto','nicolas']
for usuario in usuarios:
    print(usuario)


nuevoUsuario = 'Chanchito feliz'

for c in nuevoUsuario:
    print(c)


for usuario in usuarios:
    if usuario == 'roberto':
        break
    print(usuario)


for usuario in usuarios:
    if usuario == 'roberto':
        continue
    print(usuario)


# imprimer desde 0 a 5 
for x  in range(6):
    print(x)

# este inicia en 3  y llega a 14
for x  in range(3,15):
    print(x)

# este inicia en 3  y llega a 40 a pasos de 3 
for x  in range(3,40,3):
    print(x)
else: # se ejecuta al terminar el listado de un for en esta caso de un rage 
    print('Hemos Terminado')



usuarios = ['Chanchito feliz ','felipe','roberto','nicolas']

edades = [24,25,26,35]

for usuario in usuarios:
    for edad in edades:
        print(usuario,edad)

# for anidados un for dentro de otro for 

print('FOR DENTRO DE OTRO FOR')


