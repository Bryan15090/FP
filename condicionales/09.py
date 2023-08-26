import os
os.system("cls")

codigo=int(input("codigo(101,102,103,104): "))
cantidad=int(input("Cantidad:"))

if codigo == 101:
    precio_unitario=17
    if cantidad <=10:
        descuento=0.05
    elif cantidad >10 and cantidad <=20 :
        descuento=0.08
    elif cantidad >20 and cantidad <=30 :
        descuento=0.10
    elif cantidad >30 :
        descuento=0.13

if codigo == 102:
    precio_unitario=25
    if cantidad <=10:
        descuento=0.05
    elif cantidad >10 and cantidad <=20 :
        descuento=0.08
    elif cantidad >20 and cantidad <=30 :
        descuento=0.10
    elif cantidad >30 :
        descuento=0.13

if codigo == 103:
    precio_unitario=16
    if cantidad <=10:
        descuento=0.05
    elif cantidad >10 and cantidad <=20 :
        descuento=0.08
    elif cantidad >20 and cantidad <=30 :
        descuento=0.10
    elif cantidad >30 :
        descuento=0.13

if codigo == 104:
    precio_unitario=27
    if cantidad <=10:
        descuento=0.05
    elif cantidad >10 and cantidad <=20 :
        descuento=0.08
    elif cantidad >20 and cantidad <=30 :
        descuento=0.10
    elif cantidad >30 :
        descuento=0.13   

importe_compra=precio_unitario*cantidad 
descuento_total=importe_compra*descuento   
total_pagar=importe_compra-descuento_total

print("importe de compra: ",importe_compra)
print("Descuento: ",descuento_total)
print("Total a pagar: ",total_pagar)