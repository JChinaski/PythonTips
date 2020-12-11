#https://www.mclibre.org/consultar/python/lecciones/python-biblioteca-random.html

from random import randrange, choice, uniform
"""
print(randrange(10))
print(choice(["1", "2", "3","4","5"]))

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "cherry":
    break
"""


#lista = ["1", "2", "3","4","5", "6"]
lista = ["uno", "dos", "tres","cuatro","cinco", "seis"]

print ("tamano" , len(lista))

print (lista[3])
"""
RECORRER LISTA : 

for elemento_lista in lista:
  print ( elemento_lista )

"""

for x in range(26):
  #print(x)
  print("x: ",x, " - ",choice(lista))


for x in range(10):
  #print(x)
  #print("x: ",x, " - ",randrange(10))
  print(randrange(10, 110))
  #print(uniform(5, 8))