class Usuario:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

    def Saludo(self):
        print('Hola mi nombre es ->', self.name, self.lastName)
# lo pruimero que se ejecuta al generar una instancia es
# el metodo init

usuario = Usuario('Felipe','Feliz')
usuario2 = Usuario('Chanchito','Feliz')

usuario.Saludo()
usuario2.Saludo()

# pruedo cambiar las propiedades de las instacias de los objetos para

usuario.name = 'Chanchito'
usuario.Saludo()

del usuario.name  # eliminar una propiedad de objeto 

del usuario2     # elimina toda la instacia de usuario 
