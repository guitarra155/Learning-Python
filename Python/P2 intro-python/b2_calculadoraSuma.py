primero = input('Ingrese primer numero -> ')
segundo = input('Ingrese segundo numero-> ')
# tenemos que transformar los datos que se ingresa de la
# para este caso tenemos que tranformarlos a numeros
primerNumero = int(primero)
segundoNumero = int(segundo)
print(primerNumero + segundoNumero)


print('Segundo Intento')
primero = input('Ingrese primer numero -> ')
try:
    primero = int(primero)
    # intenta transformar a numero en lapero en caso que no logre transformar aun numero en
    # se ejutará lo que este adentro de segundoescept
except:
    primero = 'chanchito feliz'


segundo = input('Ingrese primer numero -> ')
try:
    segundo = int(segundo)
    # intenta transformar a numero en lapero en caso que no logre transformar aun numero en
    # se ejutará lo que este adentro de segundoescept
except:
    segundo = 'segundo chanchito feliz'

if primero == 'chanchito feliz' or segundo == 'segundo chanchito feliz':
    print('se ingreso mal un dato intente solamente numeros')
else:
    print(primero+segundo)


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