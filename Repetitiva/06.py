import os
os.system("cls")

num=int(input("Numero: "))
primero=int(input("Desde: "))
ultimo= int(input("Hasta: "))

for i in range (primero,ultimo+1):
    print(f"´{num} x {i} = {num*i}")
    