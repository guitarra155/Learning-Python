
lista = [1,1,1] 
lista2 = lista.copy()
lista.append(100)# para poder agregar más datos 
print(lista,lista2.count(1))

# lista2.count(2)  me indica cuantas veces se repite 
# el valos que se enuentra adentro de count en la lista

lista.clear()
# para limpiar la lista 
print(lista)


# contar la ciantidad de elementos dentro de una lista 

print(len(lista2),len(lista))

# tambien se lo puede escribir de la siguiente manera la

largolista = len(lista)
largolista2 = len(lista2)

print(largolista,largolista2)

#****************************************************************

# acceder a los datos de una lista

lista = ['Hola','mundo','chanchito feliz']

print(lista[2])

#*******************************

lista.pop()  # elimina ultimo elemento de la lista
print('elemnto de lista eliminado ', lista)
lista.remove('Hola')
print('elemnto de lista eliminado por seleccion ', lista)

#****************************************************************

lista = ['Hola','mundo','chanchito feliz']
lista.reverse()
print(lista)
#  si quiero hacer uso del metodo de sort 
# ya que pordenar solo funciona en el mismo tuipo de dato 
lista.append('chanchito triste')
lista.sort()
print(lista)


lista3 = [10,15,49,5,2,4,8,6,7,9,11]
lista3.sort()
print(lista3)



