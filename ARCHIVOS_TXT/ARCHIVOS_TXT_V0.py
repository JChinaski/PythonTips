

"""

# Abre un archivo especifico y lo muestra
f = open ('holamundo.txt','r')
mensaje = f.read()
print(mensaje)
f.close()



#Abre un archivo especifico y remplaza todo por algo en especifico
f = open ('holamundo.txt','w') # W: crea o remplaza
f.write("hola puto y jodido mundo mundo") # si se le quita esta linea crea un archivo sin nada
f.close()

#crea un archivo y escribe con un salto de linea
file = open("/ruta/filename.txt", "w")
file.write("Primera línea" + os.linesep)
file.write("Segunda línea")
file.close()



#crea y escribe un excel - Depende librerias 
import pandas as pd
from pandas import ExcelWriter
df = pd.DataFrame({'Id': [1, 3, 2, 4],
                   'Nombre': ['Juan', 'Poto', 'María', 'Pablo'],
                   'Apellido': ['Méndez', 'López', 'Tito', 'Hernández']})
df = df[['Id', 'Nombre', 'Apellido']]
writer = ExcelWriter('ejemplo.xlsx')
df.to_excel(writer, 'Hoja de datos', index=False)
writer.save()



"""

#UTILES
#https://uniwebsidad.com/libros/python/capitulo-6/metodos-de-formato
#http://decodigo.com/python
#pip install pandas

#pip install XlsxWriter