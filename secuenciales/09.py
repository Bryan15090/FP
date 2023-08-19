import os 
os.system("cls")

numero=int(input("Numero de 4 digitos: "))

suma=0
while numero > 0:
    suma = suma+(numero % 10)
    numero=numero//10
print("la suma de los digito es: ",suma)
