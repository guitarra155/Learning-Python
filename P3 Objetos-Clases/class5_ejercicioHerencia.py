class Usuario:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

    def Saludo(self):
        print('Hola mi nombre es ->', self.name, self.lastName)

class Admin(Usuario):
    def superSaludo(self):
        print('Hola me llamo es ->', self.name,' y soy el administrador')

# class Gato:
    # def __init__(self,name, onomatopeya):
        # self.name = name
        # self.onomatopeya = onomatopeya
    
    # def Saludo(self):
        # print('Hola soy un gato y mi sonido es el ->', self.onomatopeya)

# class Perro:
    # def __init__(self,name, onomatopeya):
        # self.name = name
        # self.onomatopeya = onomatopeya
    
    # def Saludo(self):
        # print('Hola soy un perro y mi sonido es el ->', self.onomatopeya)

# el perro y el gato tienen muchas cosas en comun  podemos usar herenecia 

class Animal:
    def __init__(self,name, onomatopeya):
        self.name = name
        self.onomatopeya = onomatopeya
    def Saludo(self):
        print('Hola soy un',self.tipo,'y mi sonido es el ->', self.onomatopeya)

class Gato(Animal):
    tipo = 'gato'

class Perro(Animal):
    tipo = 'perro'

class Canario(Animal):
    tipo = 'canario'

gato = Gato('Fluffy', 'maulido')
gato.Saludo()

perro = Perro('Zuco','ladrido')
perro.Saludo()

canario = Canario('piolin','Silvido')
canario.Saludo()

