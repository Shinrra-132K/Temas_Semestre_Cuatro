CLAVE_XOR = 42  

with open("ahmed_musin_XOR.txt", "rb") as f:
    datos_cifrados = f.read()

datos_descifrados = bytes([b ^ CLAVE_XOR for b in datos_cifrados])

texto_original = datos_descifrados.decode("utf-8")

with open("ahmed_musin2.txt", "w", encoding="utf-8") as f:
    f.write(texto_original)

print("¡Archivo descifrado con éxito como 'ahmed_musin2.txt'!")
