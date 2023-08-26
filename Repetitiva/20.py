import os
os.system("cls")

lista=[]

cant= int(input("¿Cuantos numeros desea ingresar? "))
i=1

while i <= cant:
    n=int(input(f"{i} Ingrese numero: "))
    lista.append(n)
    i+=1

print("numero mayor ",max(lista))
print("numero menor ",min(lista))
    
