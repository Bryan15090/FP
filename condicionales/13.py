import os
os.system("cls")

num=int(input("Numero de tres digitos: "))

n3 = num % 10
n2 = (num %100) //10
n1 = num//100

if (n1 == n2 - 1 == n3 -2) or  (n1==n2+1==n3+2):
    print("Los numeros son consecutivos")
else:
    print("Los numero no son consecutivos")
