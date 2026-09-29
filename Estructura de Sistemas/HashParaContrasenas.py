#Hacer pip install bcrypt en el cmd
import bcrypt

#Generar el hash
password = b"Contrasena"
hashed =bcrypt.hashpw(password, bcrypt.gensalt()) #la salt le agrega un numero aleatorio a la contrasena para darle seguridad

#Verificar la contrasena
print(bcrypt.checkpw(password, hashed)) #True o False

print(len(hashed))

#Hace que los ataques de fuerza bruta sean mas lentos y mas dificiles
#Incrementa el costo computacional para los hackers