import os
from os import scandir, getcwd  # ls_arch
from os.path import abspath  #
from os import listdir  # ls_arch_carp

ruta_app = os.getcwd()  # obtener ruta actual
#print(type (ruta_app)) #STR string
print(ruta_app)


# 5.-

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

#print (fileList)

"""

# 1.-
def ls_arch(ruta):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]  # lista solo archivos de la ruta


lista_arch = ls_arch(ruta_app)
print(lista_arch)


# 2.-
def ls_arch_ruta(ruta):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]  # lista solo archivos de la ruta


lista_arch = ls_arch_ruta(ruta_app)
print(lista_arch)


# 3.-
def ls_arch_carp(ruta):
    return listdir(ruta)  # lista archivos y carpetas de la ruta


lista_arch_carp = ls_arch_carp(ruta_app)
print(lista_arch_carp)

# 4.-
from os import walk, getcwd


def ls_arch_carp_sub(ruta):
    listaarchivos = []
    for (_, _, archivos) in walk(ruta):
        print(archivos)
        listaarchivos.extend(archivos)
    return listaarchivos


lista_arch_carp_sub = ls_arch_carp_sub(ruta_app)
print(lista_arch_carp_sub)
"""