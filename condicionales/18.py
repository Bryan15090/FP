import os
os.system("cls")

donacion_anual=float(input("Donacion Anual: "))

if donacion_anual>=10000:
    centro_salud=donacion_anual*0.30
    comedor_niños=donacion_anual*0.50
    invertir=donacion_anual-centro_salud-comedor_niños
else:
    centro_salud=donacion_anual*0.25
    comedor_niños=donacion_anual*0.60
    invertir=donacion_anual-centro_salud-comedor_niños

print("Monto Centro de salud: ",centro_salud)
print("Monto comedor de niños: ",comedor_niños)
print("Invertir en bolsa: ",invertir)