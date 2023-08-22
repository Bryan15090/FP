import os
os.system("cls")

numero=int(input("Numero Asignado: "))

estado_civil=numero//1000
edad= (numero%1000)//10
genero = numero%10

if estado_civil ==1:
    estado_civil_str="Soltero"
if estado_civil ==2:
    estado_civil_str="Casado"
if estado_civil ==3:
    estado_civil_str="Divorciado"
if estado_civil ==4:
    estado_civil_str="Viudo"

if genero==1:
    genero_str="Masculino"
if genero==2:
    genero_str="Femenino"

print("Estado_civil:",estado_civil_str) 
print("Edad:",edad)
print("Genero:",genero_str)
