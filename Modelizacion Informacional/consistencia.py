p = False
q = True
def disyun(p,q):
	return p or q

def nop(p):
	return not p

def condicion(p,q):
	return not p or q

print(disyun(p,q), nop(p), condicion(p,q))	

