import hashlib

data = "HELLO"
bdata = bytes(data, "utf-8")
h1 = hashlib.new("md5", bdata).hexdigest()
h2 = hashlib.new("sha256", bdata).hexdigest()
h3 = hashlib.new("sha512", bdata).hexdigest()

print(h1)
print(h2)
print(h3)

##Es una funcion buena:)
##Caracteristicas:
##Siempre que yo ejecute esto me dara el mismo valor
##velocidad
##resistente a colision
## dificil de invertir
##Efecto avalancha

