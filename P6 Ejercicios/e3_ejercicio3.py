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

listaMuestra = [10,-10,-145,-56,8,3,9,7,2,0,1,5,9,8,3,-180]
menor(listaMuestra)
