# c = open('chanchito.txt','r')
# open -> permite abrir un archivo si se encuentra en el mismo lugar 
c = open('chanchito.txt') # la r es permiso solo de leer 
# 'a' -> append para agregar texto al archivo 
# 'w' -> si quiero modificar por completo usamos el permiso, tambien lo puede crear 
# 'x' -> si no se encuentra creado entonces crea el archivo 


# print(c.read())# c,read  toca tener cuidado con eso 
# pues si el archivo es muy grande pues podria ser pejudicial para el codigo 

# si quiero leer linea que sea uno por uno 

for x in c:   # para leer cada linea de forma independiente 
    print(x)

# una buena practica es cerrar el archivo usando close()
c.close()