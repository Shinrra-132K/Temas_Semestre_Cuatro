with open("ahmed_musin2.txt", "r", encoding="utf-8") as f:
    texto_bits = f.read().strip()  # Leemos el texto entero y quitamos espacios en los extremos

# 1. Cortamos el texto en bloques de exactamente 8 caracteres
lista_bits = [texto_bits[i:i+8] for i in range(0, len(texto_bits), 8)]

# 2. Convertimos cada bloque de 8 bits a su número entero (byte)
lista_bytes = [int(bit, 2) for bit in lista_bits if len(bit) == 8]

# 3. Guardamos los bytes en el archivo PNG
with open("ahmed_musin3.png", "wb") as f:
    f.write(bytes(lista_bytes))

print(f"¡Imagen reconstruida con éxito! Se procesaron {len(lista_bytes)} bytes en 'ahmed_musin3.png'.")
