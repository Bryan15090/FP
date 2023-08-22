import os
os.system("cls")

sueldo_basico=600

monto_vendido=int(input("Monto vendido: "))
comision=monto_vendido*0.15
sueldo_bruto=sueldo_basico+comision

if monto_vendido >=1800:
    descuento=sueldo_bruto*0.1
else:
    descuento=0.05

sueldo_neto=sueldo_bruto-descuento

if monto_vendido >=1000:
    polos=3
else:
    polos=1

print("Sueldo bruto:", sueldo_bruto)
print("Descuento:", descuento)
print("Sueldo neto:", sueldo_neto)
print("Número de polos obsequiados:", polos)
