with open('PEP.text','r') as f:
	seq = f.read()
	l = []

	for i in range(0,len(seq),8):
		l.append(int(seq[i:i+8],2))

with open('PEP2.pdf','wb') as g:
	g.write(bytes(l))

print("Proceso terminado")	
