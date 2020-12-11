"""
#ARCHIVOS
#MANEJO DE LECTURA Y ESCRITURA DE ARCHIVOS

a=open("C:\Git\TipsPython\Pruebas\Doc\ANEXOS.txt", "r") # w :write - r: read

#leer  = a.read() #LEE TODO EL ARCHIVO

leer  = a.readline()
print(leer)
leer2  = a.readline()
print(leer2)

#ESCRITURA

b = open("C:\Git\TipsPython\Pruebas\Doc\ArchivoEscritura.txt", "w") #esto abre el archivo y remplaza todo lo que hay dentro

b.write("Uno \nDos \nTres")

b.close()

#CSV #https://thepythonguru.com/python-how-to-read-and-write-csv-files/
#import pandas
#df = pandas.read_csv("C:\Git\TipsPython\Pruebas\Doc\ej_csv.csv" , encoding='latin-1' )
#print(df)

import csv

with open("C:\Git\TipsPython\Pruebas\Doc\ej_csv.csv", newline='') as Archivo:
    reader = csv.reader(Archivo)
    for linea in reader:
        print(linea)


#leer un CSV

import csv

with open("C:\Git\TipsPython\Pruebas\Doc\ej_csv.csv") as File:
    reader = csv.reader(File, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        print(row)

#import csv

#with open("C:\Git\TipsPython\Pruebas\Doc\ej_csv.csv") as csvfile:
#    readCSV = csv.reader(csvfile, delimiter=',')
#    for row in readCSV:
#        print(row)
#        print(row[0])
#        print(row[0],row[1],row[2],)

#http://docs.python.org.ar/tutorial/

#json

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)
print(y["age"])
print(y["city"])

"""
