# escribir un a función que encuentre el elemneto menor de una lista 
def menor(lista):
    menor = 0
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[j] <= lista[i]:
                menor = lista[j]
                lista[i] = lista[j]
                lista[j] = menor
    print(menor)

listaMuestra = [-10,1,3,5,4,6,8,5,2,10]
menor(listaMuestra)
