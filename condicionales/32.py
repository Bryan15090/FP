import os
os.system("cls")

categoria=input("categoria: ")
promedio=float(input("promedio: "))

if categoria == "A" : pension = 550
elif categoria == "B" : pension = 500
elif categoria == "C" : pension = 450
elif categoria == "D" : pension = 400

if promedio <= 14 : descuento = 0
elif promedio >= 14 and promedio <16 : descuento = 0.10
elif promedio >= 16 and promedio <18 : descuento = 0.12
elif promedio >= 16 and promedio <20 : descuento = 0.15

print (f"Pension = S/ {pension:.2f}")
print (f"Descuento = S/ {(descuento * pension):.2f} - {( descuento * 100):.2f}" )
print (f"Nueva pension = S/ {(pension * ( 1- descuento)):.2f}")

