import os
os.system("cls")

monto_vendido=int(input("Monto total vendido: "))

aumento=monto_vendido*0.10
if monto_vendido >= 5000:
    exceso=(monto_vendido//500)*25

sueldo=aumento+exceso

print("Sueldo del vendedor: ",sueldo)
