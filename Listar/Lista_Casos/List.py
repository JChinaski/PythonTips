import os
rootDir = '.'
result = {}  # Declaramos el diccionario
ruta_app = os.getcwd()
print(ruta_app)

mi_path = ruta_app +"/ero.txt" #donde se aloja txt
f = open(mi_path, 'a+', encoding='utf-8')

for dirName, subdirList, fileList in os.walk(rootDir):
    filenames = []  # Declaramos la lista en la que se almacenarán los nombres de archivo.
    for fname in fileList:
        filenames.append(fname)  # Añadimos el nombre de archivo a la lista
    result[dirName] = filenames  # y por último seteamos el diccionario (como clave está el directorio y como valor los archivos.

for dir, fileList in result.items():
    print('Directorio encontrado:' + dir)
    for fname in fileList:
        print('\t' + fname)
        f.write('Directorio encontrado:' + dir + '\t' + fname + '\n')
f.close()