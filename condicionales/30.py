import os
os.system ("cls")

cuota =int(input("Cuota : "))
dia = int(input("Dia de pago: "))

if dia <=10 :
     descuento = cuota* 0.02
     if descuento < 5 : descuento = 5 
     descuento*= -1
elif dia >20 :
     descuento = 0.03 * cuota
     if descuento < 10 : descuento = 10
else :
     descuento = 0

print(f"Cuota a pagar = S/ {cuota + descuento:.2f}")
print(f"descuento     = S/ {(descuento):.2f}")
