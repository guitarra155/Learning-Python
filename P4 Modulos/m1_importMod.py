import modulos as xs
from  camelcase import CamelCase
# import mod1 as otroNombreModulo
# este es el caso en donde se usa todo el modulo
# print(otroNombreModulo.pets)
# otroNombreModulo.saludo('Guitarra Jhon')

# pero existren casos en el cual ese no es el caso 
# y solo deseamos usar una parte del modulo entoces se usa 
print(xs.pets)
xs.saludo('Guitarra Jhon')

c = CamelCase()
s = 'Esta oración necesita CamelCase!'
camelcased = c.hump(s)
# podemos usar distintos modulos 
# y aprender a usar el saber com
# 
# como istala pip
# https://recursospython.com/guias-y-manuales/instalacion-y-utilizacion-de-pip-en-windows-linux-y-os-x/
# 
# pagina para encontrar otros paquetes de
# https://pypi.org/ose intala y toda la cosa 

# como istala pip
# https://recursospython.com/guias-y-manuales/instalacion-y-utilizacion-de-pip-en-windows-linux-y-os-x/

# pagina para encontrar otros paquetes de pip
# https://pypi.org/

print(camelcased)