import time
#lee el archivo pdf
#l crea la lista del contenido
#byte hace la represnetacion a binario
with open('PEP.pdf','rb') as f:
	binary_data = f.read()
	l = []

	for byte in binary_data:
		binary_representation = f"{byte:08b}"
		l.append(binary_representation)

#aca se crea el archivo de texto para anadirel binario al .text
with open('PEP.text','w') as f:
	seq= "".join(l)
	f.write(seq)

print("Proceso terminado")	

