# las tuplas son casi lo mismo que las lista
# pero en este caso los valores que se encutren adentro no se pueden cambiar 

tupla = ('hola','mundo','somos','tupla')
print(tupla)
print(tupla.count('hola'))# cuantas veces se repite 
print(tupla.index('somos'))#nos regresa el valor de donde se enuentra el elemento 
print(tupla[0])
print(tupla[2])

# no se puede usar append ya que las tuplas 
# no son modificacles 
# si queremos modificar la tupla lo que tenemos que hacer 
# es convertirla en una lista 

listaDeTupla = list(tupla)
listaDeTupla.append('chanchito nuevo')
print(listaDeTupla)


rango = range(6)
print(rango)

# este tipo de dato rango nos ayudará a trabajar cuando 
# empecemos a usar iteraciones 