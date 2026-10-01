from itertools import product
for tupla in product(*[(c.upper(), c.lower())for c in "Juan"]):
	cadena = "".join(tupla)
	print(cadena)