import os
os.system("cls")

sexo=input("Sexo(F/M): ")
edad=int(input("Edad: "))

if sexo == "F":
    if edad<=23:
        categoria="FA"
    else:
        categoria="FB"
elif sexo == "M":
    if edad <=25:
        categoria="MA"
    else:
        categoria="MB"

print("Categoria: ",categoria)