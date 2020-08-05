"""
#INT

#P0TENCIA
POT=7**2
print("RESULTADO DE 7^2:", POT )

#DIVISION ENTERA
RES=7//5
print("RESULTADO DE 7//5:", RES )

#DIVISION
RES=7/5
print("RESULTADO DE 7//5:", RES )

#MODULO O RESTO
RES=7%5
print("RESULTADO DE 7//5:", RES )

#STRING
print("STRING")
#CONCATENAR
RESTR="H"+"HOLA"
print ("CONCATENAR 'H' + 'OLA': ", "H"+"OLA")

#CONCATENAR
RESTR="A"*3
print ("CONCATENAR A*3: ", RESTR)

print("CONCATENAR 'Res: +str(2*2)+str(5)' : "+"Res: "+str(2*2)+str(5))

#DATA
print("INPUT DATA:")
print("descomentar para ver")
##nom= input("Ingrese Nombre: ")
##print("Hola "+ nom)

#IF
print("IF")
llueve=True
temperatura =  int (input("Ingresa T°: "))
if temperatura < 18:
    if llueve == True:
        print("llevar paraguas")
    else:
        print("No lleves paragua")
else:
    print("caluroso")

#WHILE
print("WHILE")
print("Ingrese temp ( menor q 73 )")
temp=int(input())
print("F°   C°")
while temp < 73:
    print(temp, "  ", int((temp-32)*5/9))
    temp = temp + 1


#FOR
print("FOR")
print("Agregar en array cantidad de nombres definido")
cant_nom = int(input("Ingrese la cantidad de nombres:"))
print(cant_nom)
i=0
a = []
for i in range(cant_nom):
    print(i)
    a.append(input("ingrese nombre: "))
    ++i

print("A[] = ",a)
#print(a[1])

print("RECORRER ARRAY")
print("LARGO ARRAY: ", len(a))

i=0
for i in range(len(a)):
    print("A[",i,"]: ", a[i])

#FUNCION
print("FUNCION PARA SABER SI EL NUMERO ES PAR")
def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

numero = int(input("Ingrese Numero para ver si es par: "))
print(es_par(numero))

string = input("Ingrese un string: ")
print("Colocar letras en mayuscula: ",string.upper())
print("Colocar letras en minusculas: ",string.lower())
print("Remplazar letra 'a' por '8': ",string.replace("a","8"))

#LISTA
l =["a","b","c","d","e","f","g","h","i","j",12]

print(type(l))

print("l = ",l)

print(l[2:7])
print(l[2:7:2])
print(l[7:])
print(l[:5:3])
print(l[2:2])
print(l[::-1])

#recorrer lista con un for -in

for elem in l:
    print(elem)

#se pueden cocatenar listas
l2=["hola","mundo", 100]

print(l2)
l3= l + l2
l4= l2*2
print(l3)
print(l4)

#agregar elemento en la lista
l2.append("Juan")
print(l2)
l2.insert(1,"nueva palabra") #agrega elemento en una posicion especifica en este caso en la posicion 1
print(l2)

#elimina y retorna el ultimo elelemto de la lista

popl2= l2.pop()
print(popl2)
print(l2)

#elimina y retorna el elemento de la posicion indicada

remov= l2.remove(0) #no me fuunciono
print(remov)
print(l2)


#FUNCIONES SOBRE LISTAS

#TAMAÑO O CANTIDAD DE ELEMENTOS EN UNA LISTA

list =["a","b","c","d","e","f","g","h","i","j",12]
print(type(list))
print(list)
print("la lista tiene: ", len(list), " elementos")

#BUSCAR ELEMENTOS EN UNA LISTA

print("Esta g en la lista ?", ("g" in list))

#Encontrar la posicion de un elemento ubicado en la lista

print("En que posicion esta 'g' ? : " , list.index("g"))

#Llenar una lista

texto  = input("ingrese una Lista: ")
print("Primero: ", texto[0])
print("No Lista: ", texto)
list2 = []
inicio = 0
for i in range(0,len(texto)):
    if texto[i] == ",":
        list2.append(texto[inicio:i])
        inicio = i + 1
list2.append(texto[inicio:])
print("Lista = ", list2)

#Convertir un string separado por algo en una lista (en este caso separado por puntoycomas)

texto= input("ingrese una lista: ") #Juan;Pedro;3; die go; 32;as
list3 = texto.split(";")
print("lista = ", list3)

#ordenar elementos de una lista
print("lista Original", list3)
list3.sort()
print("lista Ordenada: ", list3)

"""

