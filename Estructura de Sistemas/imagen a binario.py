with open("ahmed musin.png", "rb") as f:
	bytes_data= f.read()

L = []
for byte in bytes_data:
	L.append(f"{byte:08b}")

len(L)
L[0]
L[:7]

s = "".join(L)

with open("ahmed musin.txt", "w") as f:
	f.write(s)

##with open("ahmed musin.txt", "s") as f:
##	f.write(s)


##with open("ahmed musin.txt", "r") as f:
##	seq = f.read()

##L=[]


#for i in range(0, len(seq), 8):
#	L.append(int(seq[i:i+8],2))

#L[100:]

#with open("ahmed musin.txt", "mb") as f:
#	f.write(bytes(L))




