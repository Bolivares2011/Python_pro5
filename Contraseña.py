import random

simbolos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


print(" ")
print(" ")
longitud = int(input("¿Cuál es la longitud de tu contraseña? : "))


contrasena = ""


for i in range(longitud):
    contrasena += random.choice(simbolos)


print(f"Tu contraseña generada es: {contrasena}")
