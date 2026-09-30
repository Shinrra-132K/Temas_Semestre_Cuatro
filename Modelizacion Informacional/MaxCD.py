def mcd_iterativo(a, b):
    while b != 0:
    	modulo = a%b
    	a = b
    	b = modulo
    return a
    #Este tambien sirve
    #valor = 0;
    #for i in range(1,b):
   # 	if a%i == 0 and b%i == 0:
   # 		valor = i
   # return valor

print(mcd_iterativo(84, 30))


def MCD(a,b):
	if b != 0:
		return MCD(b,a%b)
	if b == 0:
		return a

print(MCD(84,30))

#Ta mal
def sumatoria(n):
	if n == 0:
		return 0
	return 2*(n*((-1)**n))
	
print(sumatoria(5))				
