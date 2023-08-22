import os
os.system("cls")

hijos=int(input("Hijos del empleado: "))
sueldo=int(input("sueldo del empleado: "))

if hijos >=1 :
    bonificacion=sueldo*0.125 + 40*hijos
else:
    bonificacion=sueldo*0.10

sueldo_neto=sueldo+bonificacion

print("Bonificacion: ",bonificacion)
print("Sueldo neto: ",sueldo_neto)
