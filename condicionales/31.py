import os
os.system("cls")

horas=int(input("Horas trabajadas: "))
categoria=input("Categoria: " )

if categoria == "A":
    sueldo_bruto=horas*21
elif categoria == "B":
    sueldo_bruto=horas*18.50
elif categoria == "C":
    sueldo_bruto=horas*17
elif categoria == "D":
    sueldo_bruto=horas*15.50

if sueldo_bruto>2500 :
    descuento=sueldo_bruto*0.2
else:
    descuento=sueldo_bruto*0.15

sueldo_neto=sueldo_bruto-descuento

print("Sueldo bruto: ", sueldo_bruto)
print("Descuento: ", descuento)
print("Sueldo neto: ", sueldo_neto)