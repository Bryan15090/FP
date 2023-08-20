import os
os.system("cls")

juan=float(input("Cantidad de dinero que aporta Juan en dolares : "))
rosa=float(input("Cantidad de dinero que aporta Rosa en dolares : "))
daniel=float(input("Cantidad de dinero que aporta Daniel en soles : "))

dolar_daniel= daniel/3.00
total_dolares=juan+rosa+dolar_daniel

p_juan=juan*100/total_dolares
p_rosa=rosa*100/total_dolares
p_daniel=dolar_daniel*100/total_dolares

print("Capital total en dolares es: ", total_dolares)
print(f"Juan aporta el: {p_juan:.2f} % del capital")
print(f"Rosa aporta el: {p_rosa:.2f} % del capital")
print(f"Daniel aporta el: {p_daniel:.2f} % del capital")