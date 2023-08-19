import os 
os.system("cls")

altura=int(input("Altura de cilindro : "))
radio=int(input("Radio de cilindro : "))

areatotal = 2*3.1416*radio*(radio+altura)
Volumen = 3.1416*radio*radio*altura

print(f"Area: {areatotal:.2f}")
print(f"Volumen: {Volumen:.2f}")

