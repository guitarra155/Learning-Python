class Usuario:
    def __init__(self, name, lastName):
    # luego indico que hago con ese nombre y con ese apellido
    # self es la referencia del objeto cuando nosotros lo instanciamos 
        self.name = name
        self.lastName = lastName

# lo pruimero que se ejecuta al generar una instancia es
# el metodo init

usuario = Usuario('Felipe','Feliz')
usuario2 = Usuario('Chanchito','Feliz')
print(usuario.name,usuario.lastName,usuario2.name,usuario2.lastName)