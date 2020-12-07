import os

def list_files(dir):
    r = []
    for root, dirs, files in os.walk(dir):
     for name in files:
      r.append(os.path.join(root, name))
    return r

ruta_app = os.getcwd()
print (list_files(ruta_app))

mi_path = ruta_app +"/Resultado_txt.txt" #donde se aloja txt
f = open(mi_path, 'a+')

for i in list_files:
    f.write(mi_path + ' | ' +i + '\n')

f.close()


"""
import os
ruta_app = os.getcwd()

for base, dirs, files in os.walk(ruta_app):
  print (os.getcwd())
  print (files)


"""



"""
import os

ruta_app = os.getcwd() #OBTIENE LA RUTA ACTUAL
print (ruta_app)
contenido = os.listdir(ruta_app ) #GUARDA EN UNA LISTA LOS NOMBRES DE TODOS LOS ARCHIVOS EN ESA RUTA
print(contenido)

mi_path = ruta_app +"/fichero.txt" #donde se aloja txt
f = open(mi_path, 'a+')

for i in contenido:
    f.write(mi_path + ' | ' +i + '\n')

f.close()
"""