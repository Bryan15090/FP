import os 
os.system("cls")

r=int(input("Radio de cilindro: "))
h=int(input("Altura de cilindro: "))

AreaBase=3.1416*r**2
AreaLateral= 2*3.1416*r*h
AreaTotal=2*AreaBase*AreaLateral

print(f"Area Base: {AreaBase:.2f}")
print(f"Area Lateral: {AreaLateral:.2f}")
print(f"Area Total: {AreaTotal:.2f}")