# encoding=utf-8

# Obtener el dígito verificador del RUT en Python.
#
# La función recibe el RUT como un entero (sin punto),
# y entrega el dígito verificador como un entero.
# Si el resultado es 10, el RUT es "raya k".

from itertools import cycle

def digito_verificador(rut):
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    if ((-s) % 11) == 10:
    	return "K"
    else:
    	return (-s) % 11

	
print('RUT 1: 7.750.754')
r='7750754'
print ("Digito Verificado:", digito_verificador (r))
print(" ")
print('RUT 1: 13.628.669')
r='13628669'
print ("Digito Verificado:", digito_verificador (r))

