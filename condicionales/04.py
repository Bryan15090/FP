import os 
os.system("cls")

a=int(input("ingrese nota N°1: "))
b=int(input("ingrese nota N°2: "))
c=int(input("ingrese nota N°3: "))

pfinal=a+b+c
pfinal10=a+b+c+2

if c>=10 : print("Promedio final:",pfinal10//3)
if c<10 : print("Promedio final:",pfinal//3)
