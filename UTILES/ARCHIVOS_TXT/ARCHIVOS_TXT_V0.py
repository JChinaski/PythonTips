#1 Crear un archivo txt en la ruta actual

import os
ruta_app = os.getcwd()  # obtener ruta actual
#print(type (ruta_app)) #STR string

print(" ")
print("La Ruta Actual es :\n" , ruta_app)

#crea un archivo y escribe con un salto de linea
file = open(ruta_app + "/TXT_CREADO.txt", "w")
file.write("Primera línea" + os.linesep)
file.write("Segunda línea")
file.close()


#2 Abre un archivo especifico y lo muestra

f = open ('TXT_CREADO.txt','r')
mensaje = f.read()
print(mensaje)
f.close()


#3 Abre un archivo especifico y remplaza todo por algo en especifico

f = open ('TXT_CREADO.txt','w') # W: crea o remplaza
f.write("hola mundo mundo :) ") # si se le quita esta linea crea un archivo sin nada
f.close()

