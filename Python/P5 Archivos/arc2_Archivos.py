c = open('chanchito.txt','a')
# 'w' basicamente modifica todo el archivo-borrando y reescribiendo 
# 'a' agrega un asola linea 
c.write('\ngregamos un alnueva linea a nuestro archivo')
c.close()

x = open('chanchito.txt','r')
print(x.read())
x.close()