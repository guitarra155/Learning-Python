# Escribir una funcion que indique si el numero es par o impar 

def parity(data):
    if data % 2 == 0:
        return True
        
    else:
        return False
        

numero = int(input('ingrese el numero a evaluar -> '))
valor = parity(numero)
if valor:
    print('El numero ->',numero,'es PAR')
else:
    print('El numero ->',numero,'es IN-PAR')