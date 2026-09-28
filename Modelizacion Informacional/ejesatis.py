from itertools import product

def satisfacibilidad():
	for x in product([True, False], repeat = 3):
		p = x[0]
		q = x[1]
		r = x[2]

		v1 = p or q
		v2 = q or not r
		v3 = r or not p
		v4 = v1 and v2 and v3

		if v4 == True :
			print(f"Es satisfacible con {p=} {q=} {r=}")
			return
	print("Es inconsistente")

satisfacibilidad()			