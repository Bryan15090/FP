import os
os.system("cls")

edad1=int(input("Primera edad: "))
edad2=int(input("Segunda edad: "))
edad3=int(input("Tercera edad: "))

if edad1 >= edad2 and edad1 >= edad3:
    edad_mayor=edad1
elif edad2 >= edad1 and edad2 >= edad3:
    edad_mayor= edad2
else:
    edad_mayor=edad3

if edad1 <= edad2 and edad1 <= edad3:
    edad_menor=edad1
elif edad2 <= edad3 and edad2 <= edad3:
    edad_menor=edad2
else:
    edad_menor=edad3

print("Edad mayor: ",edad_mayor)
print("Edad menor: ",edad_menor)
