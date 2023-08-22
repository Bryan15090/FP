import os
os.system("cls")

monto_compra=int(input("Monto de compra: "))

if monto_compra >= 5000:
    prestamo=monto_compra*0.3
else:
    prestamo=monto_compra*0.2
 
interes=prestamo*0.1
pago=monto_compra-interes-prestamo

print("Pago de la empresa: ", pago)
