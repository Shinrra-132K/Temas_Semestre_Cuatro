from itertools import product

def consistencia():
	for x in product([True, False], repeat = 2):
		p = x[0]
		q = x[1]

		v1 = p or q
		v2 = not p
		v3 = not p or q

		if v1 and v2 and v3:
			print(f"Es consistente con {p=} {q=}")
			return
	print("Es inconsistente")

consistencia()			