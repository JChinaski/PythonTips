import json
"""
#CREAR y Guardar JSON con python 

data = {}
data['clients'] = []
data['clients'].append({
    'first_name': 'Sigrid',
    'last_name': 'Mannock',
    'age': 27,
    'amount': 7.17})
data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31,
    'amount': [1.90, 5.50]})
data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36,
    'amount': 1.11})
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)

#LEER JSON con python

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
print(data)

# AABRIR JSON POR PARAMETRO DE RUTA

def cargar_datos(ruta):
    with open(ruta) as contenido:
        datos = json.load(contenido)
        print(datos)

if __name__ == '__main__':
    print("Ingrese la ruta del archivo:")
    ruta = input()
    cargar_datos(ruta)


#LEER JSON 2 con python
json_data_file = open("data_file.json", "r").read() # r for reading the file
json_data = json.loads(json_data_file)
print (json_data)

"""
