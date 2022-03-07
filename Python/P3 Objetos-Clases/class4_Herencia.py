class Usuario:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

    def Saludo(self):
        print('Hola mi nombre es ->', self.name, self.lastName)

class Admin(Usuario): #dentro del parantes entregamos la clase del cual se  tiene que basar 
    def superSaludo(self):
        print('Hola me llamo es ->', self.name,' y soy el administrador')


usuario = Usuario('Felipe','Feliz')

usuario.Saludo()
usuario.name = 'Chanchito'
usuario.Saludo()

admin = Admin('Super','Feliz')
admin.Saludo()
admin.superSaludo()

# usuario.superSaludo()