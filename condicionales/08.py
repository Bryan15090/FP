import os 
os.system("cls")

pnota=int(input("Primera nota: "))
snota=int(input("Segunda nota: "))
tnota=int(input("Tercera nota: "))

mensualidad=20

m1=mensualidad+5 if pnota>=13 else mensualidad
m2=mensualidad+5 if snota>=13 else mensualidad
m3=mensualidad+5 if tnota>=13 else mensualidad
print("Monto de mensualidad:",m1+m2+m3)
