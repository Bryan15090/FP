import os
os.system("cls")

num = int(input("Ingrese un número de 4 cifras: "))

cifra_mayor = max(str(num))
cifra_menor = min(str(num))

if cifra_mayor == cifra_menor:
    mayor_dos_cifras = int(cifra_mayor * 2)
else:
    mayor_dos_cifras = int(cifra_mayor + cifra_menor)

print("El mayor número posible de dos cifras es:", mayor_dos_cifras)