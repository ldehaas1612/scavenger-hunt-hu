import hashlib

secret_number = int(hashlib.md5("student@email.nl".lower().encode()).hexdigest(), 16)
not_so_secret_number = "/scavenger_hunt/{}".format(secret_number)
print(hashlib.md5(not_so_secret_number.encode()).hexdigest())
