import os
os.system("cls")

peso=float(input("Peso: "))
estatura=float(input("Estatura: "))

imc=peso/(estatura**2)

if imc < 20:
    print(f"IMC {imc:.2f} delgado")
elif imc>20 and imc<25:
    print(f"IMC {imc:.2f} Normal")
elif imc>25 and imc<27:
    print(f"IMC {imc:.2f} Sobrepeso")
else:
    print(f"IMC {imc:.2f} Obesidad")

