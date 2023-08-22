import os 
os.system("cls")

numero=int(input("Numero: "))

rpta ="1, "
divisores=2
fin=(numero // 2 if numero % 2 ==0 else numero //3)

for i in range (2, fin + 1 ):
    if numero % i == 0 :
        divisores += 1
        rpta += str (i) + ( ", " if i < fin else "")

rpta += ", " + str(numero)

print( f"Divisores = {rpta}")
print( f"Cantidad de divisores = {divisores}")

# divisor=0
# i=1
# while numero>= i:
#     if numero % i ==0:
#         divisor+=1
#     i+=1
# print("Divisor: ",divisor)

