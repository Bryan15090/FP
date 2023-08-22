import os
os.system("cls")

unidad_A=25
unidad_B=30

cantidad_A=int(input("Cantidad Unidades Producto(A): "))
cantidad_B=int(input("Cantidad Unidades Producto(B): "))

importe_bruto_A=unidad_A*cantidad_A
importe_bruto_B=unidad_B*cantidad_B

descuento_A=0
descuento_B=0

if cantidad_A >=50:
    descuento_A=importe_bruto_A*0.15
if cantidad_B>=60:
    descuento_B=importe_bruto_B*0.10
total_pagar=importe_bruto_A-descuento_A+importe_bruto_B-descuento_B

print("Importe bruto producto A: ",importe_bruto_A)
print("Importe bruto producto B: ",importe_bruto_B)
print("Descuento producto A: ",descuento_A)
print("Descuento producto B: ",descuento_B)
print("Total a pagar: ",total_pagar)