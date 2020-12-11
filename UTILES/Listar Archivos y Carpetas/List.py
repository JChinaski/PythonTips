import os
from os import scandir, getcwd  # ls_arch
from os.path import abspath  #
from os import listdir  # ls_arch_carp

ruta_app = os.getcwd()  # obtener ruta actual
#print(type (ruta_app)) #STR string

print(" ")
print("La Ruta Actual es :\n" , ruta_app)


#6 Lista todos los archivos de la ruta, subcarpetas y archivos dentro de estas subcarpetas y los guarda en un TXT dentro de la misma ruta

rootDir = '.'
result = {}  # Declaramos el diccionario
#ruta_app = os.getcwd()
#ruta_app = "C:/Users/nombre_usuario/Documents/carpeta_py/Listar Archivos y Carpetas" # SE PUEDE ESPECIFICAR UNA RUTA

print(ruta_app)

mi_path = ruta_app +"/Resultado_Lista_de_ArchivosyCarpeta.txt" #donde se aloja txt
f = open(mi_path, 'a+', encoding='utf-8')

#for dirName, subdirList, fileList in os.walk(rootDir):
for dirName, subdirList, fileList in os.walk(ruta_app):
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




"""

# 1.- Listar archivos dentro de la ruta especificada ( no mustra las carpetas contenida en la ruta)
def ls_arch(ruta):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]  # lista solo archivos de la ruta


lista_arch = ls_arch(ruta_app)
print(lista_arch)


# 2.-Lista la ruta de los archivos dentro de la ruta especificada
def ls_arch_ruta(ruta):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]  # lista solo archivos de la ruta


lista_arch = ls_arch_ruta(ruta_app)
print(lista_arch)


# 3.- Lista archivos y carpetas de la ruta especificada
def ls_arch_carp(ruta):
    return listdir(ruta)  # lista archivos y carpetas de la ruta


lista_arch_carp = ls_arch_carp(ruta_app)
print(lista_arch_carp)

# 4.- Imprime una lista de todo lo contenido en la ruta y en carpetas dentro de la ruta
from os import walk, getcwd


def ls_arch_carp_sub(ruta):
    listaarchivos = []
    for (_, _, archivos) in walk(ruta):
        print(archivos)
        listaarchivos.extend(archivos)
    return listaarchivos


lista_arch_carp_sub = ls_arch_carp_sub(ruta_app)
print(lista_arch_carp_sub)


# 5.- Imprime Archivos, subcarpetas y archivos dentro de estas subcarpetas

import os
rootDir = '.'
result = {}  # Declaramos el diccionario

for dirName, subdirList, fileList in os.walk(rootDir):
    #print(dirName)
    #print(subdirList)
    #print(fileList)
    filenames = []  # Declaramos la lista en la que se almacenarán los nombres de archivo.
    for fname in fileList:
        filenames.append(fname)  # Añadimos el nombre de archivo a la lista
    result[dirName] = filenames  # y por último seteamos el diccionario (como clave está el directorio y como valor los archivos.

for dir, fileList in result.items():
    print('Directorio encontrado:' + dir)
    for fname in fileList:
        print('\t' + fname)


#6


"""