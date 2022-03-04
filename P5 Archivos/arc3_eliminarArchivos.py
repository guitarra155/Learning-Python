import os
if os.path.exists('chanchito.txt'):
    os.remove('chanchito.txt')
else:
    print('el archivo no existe')

# os.rmdir('nombre de carpéta o directorio')# elimia carpetas/directorios