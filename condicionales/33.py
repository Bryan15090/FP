import os
os.system("cls")

puntualidad = int(input("puntaje de puntualidad (1-10): "))
rendimiento = int(input("puntaje de rendimiento (1-10): "))

puntaje_total = puntualidad + rendimiento

if puntaje_total<=11:
    bonificacion=puntaje_total*2.5
elif puntaje_total >11 and puntaje_total <=13:
    bonificacion=puntaje_total*5.0
elif puntaje_total >14 and puntaje_total <=16:
    bonificacion=puntaje_total*7.5
elif puntaje_total >17 and puntaje_total <=19:
    bonificacion=puntaje_total*10.0
else:
    bonificacion=puntaje_total*12.5

    

print("Puntaje de puntualidad:", puntualidad)
print("Puntaje de rendimiento:", rendimiento)
print("Puntaje total:", puntaje_total)
print("Bonificación:", bonificacion)