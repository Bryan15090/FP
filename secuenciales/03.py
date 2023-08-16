import os 
os.system("cls")

kilometros=int(input("Ingrese los kilometros recorridos: "))
pies=float(input("Ingrese los pies recorridos: "))
millas=int(input("Ingrese las millas recorridas: "))

metrosk=kilometros*1000
yardask=1093*kilometros

metrosp=pies/3.2808
yardasp=pies*0.333333

metrosm=millas/1609
yardasm=1760*millas
print(f"total de metros recorridos: {metrosk+metrosp+metrosm:.2f}")
print(f"total de yardas recorridas: {yardask+yardasp+yardasm:.2f}")