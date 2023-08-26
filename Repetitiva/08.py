import os
os.system("cls")

n = int(input("base: "))
m = int(input("exponente: "))

resultado = 1
i = 0

while i < m:
  resultado *= n
  i += 1

print("resultado:", resultado)