import os
os.system("cls")

costo_docenas=float(input("Costo por docena: "))
docenas=int(input("Docenas: "))


if docenas >=6:
    descuento=0.15
else:
    descuento=0.10

subtotal=costo_docenas*docenas
monto_descuento=subtotal*descuento
total=subtotal-monto_descuento

if docenas>=30:
    lapiceros=(docenas//3)*2
else:
    lapiceros=0

print("Monto de la compra: ",subtotal)
print("Descuento: ",monto_descuento)
print("Total a pagar: ",total)
print("Obsequio lapiceros: ",lapiceros)