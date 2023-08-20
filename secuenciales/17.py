import os
os.system("cls")

donacion=int(input("Donacion: "))

salud=donacion*0.25
comedor=donacion*0.35
escuela=donacion*0.25
asilo=donacion-salud-comedor-escuela

print("Asignacion centro de Salud: ",salud)
print("Asignacion comedor infantil: ",comedor)
print("Asignacion escuela infantil: ",escuela)
print("Asignacion asilo de ancianos: ",asilo)