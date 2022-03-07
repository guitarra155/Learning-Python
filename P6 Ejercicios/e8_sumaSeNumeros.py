lista = []

print('ingrese los numeros y para terminar escriba "bast"')
while True:
    valor = input(' Ingrese el valor -> ')
    if valor.lower() == 'basta':
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print('Dato Ivalido')
            exit()

resultado = 0
for x  in lista:
    resultado += x

print('El resultado es -> : ',resultado)
