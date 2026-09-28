# Crear archivo de texto
with open("secuencia.txt", "w") as f:
    f.write("Hora de clase\n")
    f.write("Preguntas?\n")


# Leer archivo de texto
with open("secuencia.txt", "r") as f:
    for x in f:
        print(x)


# Crear un archivo con la representación binaria
# de los caracteres del nombre

nombre = "Joaquin"

with open("secuencia.txt", "w") as f:
    for c in nombre:
        binario = bin(ord(c))[2:].zfill(8)
        f.write(binario)