from io import open

"""
archivo1 = open('archivo.txt', 'a')
archivo1.write('\n saludo IDGS801')
archivo1.close()"""

archivo1 = open('archivo.txt', 'r')
"""print(archivo1.read())
archivo1.seek(1)
print(archivo1.read())
archivo1.close()"""

#print(archivo1.readlines())

for datos in archivo1.readlines():
    print(datos.rstrip())

archivo1.close()