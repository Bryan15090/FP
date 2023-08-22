import os
os.system("cls")

numero_tarjeta=int(input("Numero de Tarjeta: "))
monto_compra=float(input("Monto de compra: "))

if numero_tarjeta % 2 == 0 and numero_tarjeta >= 100:
    descuento=monto_compra*0.15
else:
    descuento=monto_compra*0.05

print("Número de tarjeta:", numero_tarjeta)
print("Monto de la compra:", monto_compra)
print("Descuento:", descuento)
