import os
os.system("cls")

monto_vendido=int(input("Monto Vendido: "))

sueldo=500
comision=monto_vendido*0.09
sueldo_bruto=sueldo+comision

descuento=sueldo_bruto*0.11
sueldo_neto=sueldo_bruto-descuento

print("Comision: ",comision)
print("Sueldo Bruto: ",sueldo_bruto)
print("Descuento: ",descuento)
print("Sueldo Neto: ",sueldo_neto)
