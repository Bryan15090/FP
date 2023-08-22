import os
os.system("cls")

ingreso_mensual=int(input("Ingreso mensual: "))
costo_casa=int(input("Costo de casa: "))

if ingreso_mensual <1250:
    cuota_inicial = costo_casa*0.15
    mensualidad= (costo_casa-cuota_inicial)/120
else :
    cuota_inicial = costo_casa*0.30
    mensualidad= (costo_casa-cuota_inicial)/75

print("Cuota inicial",cuota_inicial)
print("Mensualidad",mensualidad)