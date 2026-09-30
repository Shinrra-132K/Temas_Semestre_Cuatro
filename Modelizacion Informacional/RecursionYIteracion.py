#Iteracion
def factorial(n):
	resp = 1
	for i in range(1,n+1):
		resp = resp*i
	return resp


print(factorial(5))

#Esta horrible la iteracion, mejor recursion :)	


#Recursion
def factor(n):
	if n == 1:
		return 1
	
	return n*factor(n-1)

print(factor(5))

def sumatoria(n):
	if n == 1:
		return 1
	return n+sumatoria(n-1)

print(sumatoria(5))


def potencia(n,p):
	if p == 1:
		return n
	return 	n*potencia(n,p-1)

print(potencia(5,5))	

