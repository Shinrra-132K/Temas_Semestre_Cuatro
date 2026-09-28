CLAVE_XOR = 42  

with open("ahmed musin.txt", "r", encoding="utf-8") as f:
    texto = f.read()

texto_en_bytes = texto.encode("utf-8")

bytes_cifrados = bytes([b ^ CLAVE_XOR for b in texto_en_bytes])

with open("ahmed_musin_XOR.txt", "wb") as f:
    f.write(bytes_cifrados)

print("¡Archivo cifrado con éxito como 'ahmed_musin_cifrado.enc'!")
