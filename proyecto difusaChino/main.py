import jugada
import reglas
import csv, operator


def main():

	#leer CSV y convertirlo en una lista de jugadas
	"""
	datos = []
	#leer CSV
	with open('Data.csv', 'r') as archivo:
		lineas = archivo.read().splitlines()
		#lineas.pop(0)
		for l in lineas:
			linea = l.split(" ")
			#print linea
			datos.append(linea)
			#print datos


	print('******************')
	print datos [0]
	print datos [1]
	print datos [2]
	print datos [3]

	"""
	datos = []
	file=open('Data.csv','r')
	data=file.readlines()
	file.close()
	contador=0

	lista_datas = []
	for renglon in data:
	    for palabra in renglon.split(','):
	        contador+=1
	        aux=palabra
	        #lista_datas.append(contaor,aux)
	        #print " ###### "
	        #print aux
	        #print palabra
	        datos.insert(contador,aux)
	        #print '%s) %s'%(str(contador),palabra)
	#print datos
	print"####"
	print datos[0]
	print datos[1]

	#generar una lista de jugadas aleatorias para pruebas de comparacion
	lista_jugadas = []
	#crea un primer elemento con datos controlables para probar match
	#lista_jugadas.append(jugada.Jugada(datos[0],2))
	lista_jugadas.append(jugada.Jugada([datos[0], datos[1], datos[2], datos[3] , datos[4] , datos[5] , datos[6] , datos[7]],2))
	#lista_jugadas.append(jugada.Jugada(datos[0],2))



	#crea 5 jugadas aleatorias y las agrega a la lista
	for i in range(5):
		jugada_i = jugada.Jugada([])
		jugada_i.generate()
		lista_jugadas.append(jugada_i)

	#imprime la lista de jugadas
	for item in lista_jugadas:
		item.imprimir()

	#genera una jugada con datos controlados como entrada al controlador difuso
	a = jugada.Jugada([0.5 , 0.1 , 0.1 , 0.1 , 0.1 , 0.1 , 0.1 , 0.1 , 0.1])
	#a.imprimir()

	#buscar match en lista de jugadas
	match = False
	for item in lista_jugadas:
		if a.comparar(item):
			a.set_cobro(item.get_cobro())
			match = True

	#sino llama al motor de inferencia
	if match:
		a.imprimir()
	else:
		print "ingresando al motor de inferencia"
		cobro = reglas.Reglas(a.valores)
		print cobro.revisar()



	

main()




"""
	#Ingresar Datos de Variables Manualmente
	NewData= []
	for i in range (10):
		if i == 0:
			testVar = raw_input("Intencion de jugar el balon:\n 1.Ninguna 2.Baja 3.Media 4.Alta\n")
			testVar=testVar.lower()
			print testVar
			if testVar == "1" or testVar == "ninguna":
				NewData.insert(i,0)
			if testVar == "2" or testVar == "baja":
				NewData.insert(i,0.3)
			if testVar == "3" or testVar == "media":
				NewData.insert(i,0.1)
			if testVar == "4" or testVar == "alta":
				NewData.insert(i,0.1)
		if i == 1:
			testVar = raw_input("Fuerza de la entrada:\n 1.Baja 2.Media 3.Alta 4.Excesiva\n")
			testVar=testVar.lower()
			print testVar
			if testVar == "1" or testVar == "baja":
				NewData.insert(i,0.1)
			if testVar == "2" or testVar == "media":
				NewData.insert(i,0.1)
			if testVar == "3" or testVar == "alta":
				NewData.insert(i,0.1)
			if testVar == "4" or testVar == "excesiva":
				NewData.insert(i,0.1)
		if i == 2:
			testVar = raw_input("Direccion origen de la entrada:\n 1.Atras 2.Costado 3.Media 4.Alta\n")
			testVar=testVar.lower()
			print testVar
			if testVar == "1" or testVar == "ninguna":
				NewData.insert(i,0.1)
			if testVar == "2" or testVar == "baja":
				NewData.insert(i,0.1)
			if testVar == "3" or testVar == "media":
				NewData.insert(i,0.1)
			if testVar == "4" or testVar == "alta":
				NewData.insert(i,0.1)
		if i == 3:
			testVar = raw_input("Intencion de jugar el balon:\n 1.Ninguna 2.Baja 3.Media 4.Alta\n")
			testVar=testVar.lower()
			print testVar
			if testVar == "1" or testVar == "ninguna":
				NewData.insert(i,0.1)
			if testVar == "2" or testVar == "baja":
				NewData.insert(i,0.1)
			if testVar == "3" or testVar == "media":
				NewData.insert(i,0.1)
			if testVar == "4" or testVar == "alta":
				NewData.insert(i,0.1)
		if i == 0:
			testVar = raw_input("Intencion de jugar el balon:\n 1.Ninguna 2.Baja 3.Media 4.Alta\n")
			testVar=testVar.lower()
			print testVar
			if testVar == "1" or testVar == "ninguna":
				NewData.insert(i,0.1)
			if testVar == "2" or testVar == "baja":
				NewData.insert(i,0.1)
			if testVar == "3" or testVar == "media":
				NewData.insert(i,0.1)
			if testVar == "4" or testVar == "alta":
				NewData.insert(i,0.1)
		if i == 0:
			testVar = raw_input("Intencion de jugar el balon:\n 1.Ninguna 2.Baja 3.Media 4.Alta\n")
			testVar=testVar.lower()
			print testVar
			if testVar == "1" or testVar == "ninguna":
				NewData.insert(i,0.1)
			if testVar == "2" or testVar == "baja":
				NewData.insert(i,0.1)
			if testVar == "3" or testVar == "media":
				NewData.insert(i,0.1)
			if testVar == "4" or testVar == "alta":
				NewData.insert(i,0.1)
		if i == 0:
			testVar = raw_input("Intencion de jugar el balon:\n 1.Ninguna 2.Baja 3.Media 4.Alta\n")
			testVar=testVar.lower()
			print testVar
			if testVar == "1" or testVar == "ninguna":
				NewData.insert(i,0.1)
			if testVar == "2" or testVar == "baja":
				NewData.insert(i,0.1)
			if testVar == "3" or testVar == "media":
				NewData.insert(i,0.1)
			if testVar == "4" or testVar == "alta":
				NewData.insert(i,0.1)
		

	"""