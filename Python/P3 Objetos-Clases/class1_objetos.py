class Usuario:
    # los metodos que puede tener una clase 
    nombre = 'Faleipe'
    apellido = 'Feliz'
    # puedo agregar todas las propiedades que yo quiera 

# cuando queramos generar una instancia de un usuario 

usuario = Usuario()
usuario2 = Usuario()
print(usuario)
print(usuario.nombre)
print(usuario.apellido)
print(usuario.nombre,usuario2.nombre)