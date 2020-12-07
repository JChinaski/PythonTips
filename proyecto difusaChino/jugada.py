import random

class Jugada:


	def __init__(self , lista, cobro = 0):
		self.valores = []
		for item in lista:
			self.valores.append(item)
		self.cobro = cobro

	def set_cobro(self, cobro):
		self.cobro = cobro

	def get_cobro(self):
		return self.cobro

	def generate(self):
		for i in range(0,9):
			self.valores.append(round(random.uniform(0,1),1))

	def imprimir(self):
		print self.valores
		print self.cobro

	def comparar(self, otra_jugada):
		response = True
		if len(self.valores) == len(otra_jugada.valores):
			for i in range(len(self.valores)):
				if self.valores[i] != otra_jugada.valores[i]:
					response = False
		return response
