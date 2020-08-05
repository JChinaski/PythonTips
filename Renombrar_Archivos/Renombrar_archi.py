
import shutil, os

def read_file(file):
    #Lee un archivo de texto y devuelve una lista con sus lineas

    lista = []
    with open(file) as procfile:
      for line in procfile:
        lista.append(line.strip())
    return lista

if __name__ == "__main__":
    print(' ')
    print("ESTE CODIGO COPIA ARCHIVOS DE UNA CARPETA ORIGEN A UNA DE DESTINO UTILIZANDO UNA LISTA DE ARCHIVOS LISTADOS EN UN TXT")
    print("OBS: Archivos de origen deben estar en una carpeta unica y no en subcarpeta")
    print(' ')
    ruta_origen = input("Ingrese la Ruta de Origen: ")
    ruta_origen = 'C:/Git/TipsPython/Renombrar_Archivos/ARCHIVOS_ORIGEN/'
    ruta_destino = input("(Opcional) Quiere ingresar una ruta de destino ""S/N"" : ")

    if ruta_destino == "n" or ruta_destino == "N":
        ruta_destino  = 'C:/Git/TipsPython/Renombrar_Archivos/ARCHIVOS_DESTINOS/'
    if ruta_destino == "s" or ruta_destino == "S":
        ruta_destino = input("Ingrese ruta de destino: ")

    ruta_txt = input("Ingrese la Ruta del archivo TxT: ")

    print("La ruta del archivo proporcionada es: " + ruta_txt)

    #Se crea una variabre de tipo lista para almacenar los archivos q se listan en el txt
    lista_txt = []
    #lista_txt = read_file(ruta_txt)
    lista_txt = read_file('C:/Git/TipsPython/Renombrar_Archivos/lista_Archivos_txt.txt')

    print(lista_txt)

    result = {}  # Declaramos el diccionario que recorre la ruta origen y almacena las carpetas y archivos encontrados en esa ruta

    for dirName, subdirList, fileList in os.walk(ruta_origen):
        filenames = []  # Declaramos la lista en la que se almacenarán los nombres de archivo.
        for fname in fileList:
            filenames.append(fname)  # Añadimos el nombre de archivo a la lista
        result[
            dirName] = filenames  # y por último seteamos el diccionario (como clave está el directorio y como valor los archivos.

    print("result")
    print(result)

    Listarch = []
    # Lista q guarda los archivos totales encontrados
    for dir, fileList in result.items():
        print('Directorio encontrado:' + dir)
        for fname in fileList:
            # print(fname)
            Listarch.append(fname)

    print(Listarch)

    #Ciclo que hace mach con el archivo de la carpeta origen y archivos listados en TXT. Cuando se produce el mach se copia el archivo a la ruta destino
    for a in Listarch:
        print('Listarch' + ' ' + a)
        for i in lista_txt:
            ##print(a)
            ##print(i)
            if a == i:
                print("MACH")
                # origen = 'C:/Git/TipsPython/Renombrar_Archivos/c1/' + a
                origen = ruta_origen + a
                destino = ruta_destino + a
                if os.path.exists(origen):
                    with open(origen, 'rb') as forigen:
                        with open(destino, 'wb') as fdestino:
                            shutil.copyfileobj(forigen, fdestino)
                            # shutil.copy("antiguo-nombre.txt", "nuevo-nombre.txt")
                            print("Archivo copiado")





#C:/Git/TipsPython/Renombrar_Archivos/name_con_punto.txt

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