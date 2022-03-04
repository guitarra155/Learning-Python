# escribir un a función que encuentre el elemneto menor de una lista 
def menor(lista):
    aux = 0
    for i in range(len(lista)):
        if lista[i] < lista[i+1]:
            aux = lista[i]
            lista[i] = lista[i+1]


lista = [5,8,-1,-9,45,8,2,-98,-10,4,5,3]

