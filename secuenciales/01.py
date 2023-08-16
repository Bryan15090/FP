import os 
os.system("cls")

varones = int(input("Varones: "))
mujeres = int(input("Mujeres: "))

total = varones+ mujeres
pVarones = varones*100/total
pMujeres = mujeres*100/total

print(f"% Varones : {pVarones:.2f}%")
print(f"% Mujeres : {pMujeres:.2f}%")
print()

