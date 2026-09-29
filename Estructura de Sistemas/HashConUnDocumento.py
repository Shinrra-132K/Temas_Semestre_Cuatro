import hashlib

with open("ahmed musin.png", "rb") as f:
	data = f.read()
	print(hashlib.new("sha256", data).hexdigest())


with open("ahmed musin.png", "rb") as f:
	d = hashlib.file_digest(f, "sha256")
	print(d.hexdigest())



