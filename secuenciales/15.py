import os
os.system("cls")

soles=int(input("ingrese el importe en soles : "))

dolares=int(input("ingrese el importe en dolares : "))

SolesaDolares=soles / 3

total=SolesaDolares+ dolares

pDolares = SolesaDolares*100/total
pSoles = dolares*100/total


print(f"Capital Total: {total} Dolares")
print(f"porcentaje de soles : {pSoles:.2f}% ")
print(f"porcentaje de dolares : {pDolares:.2f}%")