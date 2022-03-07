# escribir una funcion que reciba nombre y apellido y los vaya agregando a un archivo 
def addNmeAndLastName(name,lastName):
    c = open('NombreCompleto.txt','a')
    c.write('\n'+name + ' ' + lastName)
    c.close()

addNmeAndLastName(input('ingrese el nombre -> '),input('ingrese el Apellido -> '))