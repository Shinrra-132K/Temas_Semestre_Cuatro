with open("secuencia.txt", "r") as f:
    binario = f.read()

nombre = ""

for i in range(0, 56, 8):
    byte = binario[i:i+8]
    decimal = int(byte, 2)
    nombre = nombre + chr(decimal)

with open("nombre.txt", "w") as f:
    f.write(nombre)

print(nombre)