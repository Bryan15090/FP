import os
os.system("cls")

sueldo=250
montovendido=int(input("Monto vendido:"))

if montovendido<=5000:
	comision=montovendido*0.05
if montovendido>=5000 and montovendido<=10000:
	comision=montovendido*0.08
if montovendido>=10000 and montovendido <=20000:
	comision=montovendido*0.10
if montovendido>=20000:
	comision=montovendido*0.15
	
sueldo_bruto=sueldo+comision

if sueldo_bruto >= 3500:
	descuento = sueldo_bruto*0.15
else:
	descuento = sueldo_bruto*0.08

sueldo_neto = sueldo_bruto - descuento

print("Sueldo bruto: ", sueldo_bruto)
print("Sueldo neto: ", sueldo_neto)
print("Descuento: ", descuento)
print("Comisión: ", comision)