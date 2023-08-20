import os
os.system("cls")

cantidad=int(input("Cantidad: "))
precio_unitario=float(input("Precio Unitario: "))

importe=cantidad*precio_unitario
descuento1=importe*0.15
primer_descuento=importe-descuento1
descuento2=primer_descuento*0.15
pagar=primer_descuento-descuento2

print("Importe de compra: ",importe)
print("Descuento: ",descuento1+descuento2)
print("Importe a pagar",pagar)