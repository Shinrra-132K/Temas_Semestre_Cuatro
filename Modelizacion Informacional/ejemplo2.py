from itertools import product

def consistencia():
	for x in product([True, False], repeat=3):
		p = x[0]
		q = x[1]
		r = x[2]

		v1 = not p or q
		v2 = p == q
		v3 = r
		v4 = not q

		if v1 and v2 and v3 and v4:
			print(f"Es consistente con {p=} {q=}")
			return
	print("Inconsistente")
	
consistencia()			