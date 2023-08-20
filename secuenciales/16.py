import os 
os.system("cls")

horas_trabajadas=float(input("Horas Trabajadas: "))
pago_por_hora=float(input("Pago por Hora: "))

sueldo_basico=horas_trabajadas*pago_por_hora
bonificacion=sueldo_basico*0.20
sueldo_bruto=sueldo_basico+bonificacion
descuento=sueldo_bruto*0.10
sueldo_neto=sueldo_bruto-descuento

print("Sueldo basico: ", sueldo_basico)
print("Sueldo bruto: ", sueldo_bruto)
print("Sueldo neto: ", sueldo_neto)