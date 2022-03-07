

print('Tercer Intento')
primero = input('Ingrese primer numero -> ')
try:
    primero = int(primero)
except:
    primero = 'chanchito feliz'

if primero == 'chanchito feliz':
    print('el valor eingresado no es un entero')
    exit()

segundo = input('Ingrese primer numero -> ')
try:
    segundo = int(segundo)
except:
    segundo = 'segundo chanchito feliz'

if segundo  == 'segundo chanchito feliz':
    print('el valor eingresado no es un entero')
    exit()

print(primero + segundo)

simbolo = input('Ingrese la opreacion ->  :')

if simbolo == '+':
    print('Suma ->',primero + segundo)
elif simbolo == '-':
    print('Resta ->',primero - segundo)
elif simbolo == '*':
    print('Multiplicación ->',primero * segundo)
elif simbolo == '/':
    print('Divicion ->',primero / segundo)
else:
    print('El simbolo ingresado no es valido ')