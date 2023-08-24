import os
os.system("cls")

horas_trabajadas=int(input("Horas trabajadas: "))
pago_hora=int(input("Pago por horaria: "))

if horas_trabajadas<48:
    sueldo_bruto=pago_hora*horas_trabajadas
else:
    sueldo_bruto=(48 * pago_hora) + ((horas_trabajadas - 48)* pago_hora * 1.2)

if sueldo_bruto>1500:
    descuento=sueldo_bruto*0.11
else:
    descuento=0

pago_total=sueldo_bruto-descuento

print("Horas trabajadas: ",horas_trabajadas)
print("Pago por hora: ",pago_hora)
print("Sueldo bruto: ",sueldo_bruto)
print("Descuento: ",descuento)
print("Total a pagar: ",pago_total)
