import os 
os.system("cls")

cuadernos=int(input("Cuadernos adquiridos: "))

if cuadernos<=12:
    lapicero =0
elif cuadernos >12 and cuadernos<=24:
    lapicero =(cuadernos//4)*1
elif cuadernos >24 and cuadernos<=36:
    lapicero =(cuadernos//4)*2
elif  cuadernos >36:
    lapicero =(cuadernos//4)*2 + (cuadernos//6)+(cuadernos//12)

print("Se obsequian",lapicero,"lapiceros")