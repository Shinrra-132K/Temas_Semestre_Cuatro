from itertools import product

def satisfacibilidad():
	for x in product([True, False], repeat = 3):
		p = x[0]
		q = x[1]
		r = x[2]

		v1 = p and q

		if v1 == True:
			print(f"Es satisfacible con {p=} {q=}")
			return
	print("Es inconsistente")

satisfacibilidad()			