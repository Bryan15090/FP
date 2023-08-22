import os
os.system("cls")

a=int(input("Primer numero:"))
b=int(input("Segundo numero: "))
c=int(input("Tercer numero: "))
if a < b < c:
    print("Numeros ingresados fueron en orden Ascendente")
if a > b > c:
    print("Numeros ingresados fueron en orden Decendente")
else:
    print("Numeros ingresados fueron en orden Desorden")
    