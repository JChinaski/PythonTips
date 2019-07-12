import os

def read_file(file):
    #Lee un archivo de texto y devuelve una lista con sus lineas

    lista = []
    with open(file) as procfile:
      for line in procfile:
        lista.append(line.strip())
    return lista

l=[]
l=read_file('C:/Git/TipsPython/Renombrar_Archivos/name_con_punto.txt')
#print(l)
i= 0
#for i in l:
#    print(i)
print("FIN")

result = {}  # Declaramos el diccionario
# ruta_app = os.getcwd()
# ruta_app = "C:/DERCO/PASAR_A_PDF/data/Parte_2/PDF_PARTE_2" #"C:/Users/jacunah/Documents/GCP/Resumen"
ruta_app = 'C:/Git/TipsPython/Renombrar_Archivos/destino/'
print(ruta_app)

for dirName, subdirList, fileList in os.walk(ruta_app):
    filenames = []  # Declaramos la lista en la que se almacenarán los nombres de archivo.
    for fname in fileList:
        filenames.append(fname)  # Añadimos el nombre de archivo a la lista
    result[dirName] = filenames  # y por último seteamos el diccionario (como clave está el directorio y como valor los archivos.

Listarch = []

for dir, fileList in result.items():
    print('Directorio encontrado:' + dir)
    for fname in fileList:
        #print(fname)
        Listarch.append(fname)


l_new_name = []
l_new_name = read_file('C:/Git/TipsPython/Renombrar_Archivos/name_sin_punto.txt')

for a in Listarch:
    print('Listarch'+ ' ' + a)
    for i in l:
        ##print(a)
        ##print(i)
        if a == i:
            print("Y")
            #origen = 'C:/Git/TipsPython/Renombrar_Archivos/c1/' + a
            origen = ruta_app + a
            destino = 'C:/Git/TipsPython/Renombrar_Archivos/destino_2/' + a
            if os.path.exists(origen):
                with open(origen, 'rb') as forigen:
                    with open(destino, 'wb') as fdestino:
                        shutil.copyfileobj(forigen, fdestino)
                        #shutil.copy("antiguo-nombre.txt", "nuevo-nombre.txt")
                        print("Archivo copiado")
        else:
            print("N")

c= 0
for name_ori in l:
    print(name_ori)
    print(l_new_name[c])
    origen = 'C:/Git/TipsPython/Renombrar_Archivos/destino_2/' + name_ori
    destino = 'C:/Git/TipsPython/Renombrar_Archivos/destino3/' + l_new_name[c]
    print(origen)
    print(destino)
    c = c + 1
    if os.path.exists(origen):
        with open(origen, 'rb') as forigen:
            with open(destino, 'wb') as fdestino:
                shutil.copyfileobj(forigen, fdestino)
                #shutil.copy(forigen, fdestino)
                print("Archivo copiado")




"""

-----------------------
import shutil, os

def menu():
   print("----------- Calculadora -----------")
   print("1. Listar archivo txt")
   print("2. Resta")
   print("3. Multiplicacion")
   print("4. Division")
   print("5. Salir")
   print("-----------------------------------")

def submenu():
   print("----------- Calculadora -----------")
   print("1. Listar archivo")
   print("2. Mostrar archivo")
   print("3. Volver al menu Principal")
   print("-----------------------------------")


def default():
   return "Opcion Invalida"

def switch(case):
    if case ==1:
        submenu()
        opc = int(input("Seleccione una opcion del submenu: "))
        Lista1 = subswitch(opc)
        return Lista1

    if case == 2:
        return print("dos")

def subswitch(case):
    if case ==1:
        print("uno")
        return read_file()
    if case == 2:
        return print("dos")

def inicia():
    print("sads")


def read_file():
    # Lee un archivo de texto y devuelve una lista con sus lineas
    file = input("Ingrese la Ruta del archivo: ")
    #C:\Git\TipsPython\Renombrar_Archivos\ARCHIVOS_ORIGEN\ARCHIVO_PARA_LISTAR.txt
    print(file)
    lista = []
    with open(file) as procfile:
        for line in procfile:
            lista.append(line.strip())
    print(lista)
    return lista


if __name__ == "__main__":
    print("ESTE CODIGO COPIA ARCHIVOS DE UNA CARPETA ORIGEN A UNA DE DESTINO")
    mn=True
    while (mn == True):
        menu()
        case = int(input("Seleccione una opcion: "))
        if case == 5:
            mn=False
        if case == 1:
            switch(case)

    print(L)
"""