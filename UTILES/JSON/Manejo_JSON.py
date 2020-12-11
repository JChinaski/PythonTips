import json

#CREAR y Guardar JSON con python 

data = {}
data['clients'] = []
data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 3,
    'amount': 7.17})
data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 32,
    'amount': [1.90, 5.50]})
data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 33,
    'amount': 1.11})

# MOSTRAR 1 JSON
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)

#LEER 2 JSON con python

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
print(data)

# AABRIR JSON POR PARAMETRO DE RUTA

def cargar_datos(ruta):
    with open(ruta) as contenido:
        datos = json.load(contenido)
        print(datos)

if __name__ == '__main__':
    #print("Ingrese la ruta del archivo:")
    #ruta = input()
    ruta = "C:/Users/Chino_Chinaski/Documents/Programacion/Python/PythonTips/UTILES/JSON/data_file.json"

    cargar_datos(ruta)


#LEER JSON 3 con python
json_data_file = open("data_file.json", "r").read() # r for reading the file
json_data = json.loads(json_data_file)
print (json_data)


"""
# OTRA FORMA DE ABRIR Y MOSTRAR JSON
import json

#Abre JSON
with open('states.json') as f:
  data = json.load(f)
  print(data)

# Mostras JSON
for state in data['states']:
  print(state)
  print(state['name'])
  print(state['name'],state['abbreviation'])

"""




# VER TAMBIEN
#https://www.youtube.com/watch?v=9N6a-VLBa2I 
#https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-JSON