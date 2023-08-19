import os 
os.system("cls")

nota1=int(input("nota N°1: "))
nota2=int(input("nota N°2: "))
nota3=int(input("nota N°3: "))

pfinal=nota1+nota2+nota3
pfinal10=nota1+nota2+nota3+2

if nota3>=10 : print("Promedio final:",pfinal10//3)
if nota3<10 : print("Promedio final:",pfinal//3)
