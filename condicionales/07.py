import os
os.system("cls")

num1=int(input("Primer numero: "))
num2=int(input("Segundo numero: "))
num3=int(input("Tercer numero: "))

if num1 >= num2 and num1 <=num3:
    intermedio=num1
elif num2>= num1 and num2 <=num3:
    intermedio=num2
else:
    intermedio=num3

print("El numero intermedio es:",intermedio)
