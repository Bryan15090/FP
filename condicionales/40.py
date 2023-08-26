import os
os.system("cls")

m1=float(input("Pactica calificada matematica 1: "))
m2=float(input("Pactica calificada matematica 2: "))
m3=float(input("Pactica calificada matematica 3: "))
epm=float(input("Examen Parcial matematica : "))
efm=float(input("Examen Final matematica: "))

promedio_matematica=(m1*0.1)+(m2*0.2)+(m3*0.1)+(epm*0.3)+(efm*0.3)

if promedio_matematica <13:
    print("promedio matematica:",promedio_matematica,"Desaprobado")
else:
    print("promedio matematica:",promedio_matematica,"Aprobado")

f1=float(input("Pactica calificada fisica 1: "))
f2=float(input("Pactica calificada fisica 2: "))
f3=float(input("Pactica calificada fisica 3: "))
epf=float(input("Examen Parcial Fisica: "))
eff=float(input("Examen Final Fisica: "))

promedio_fisica=(f1*0.2)+(f2*0.2)+(f3*0.2)+(epf*0.2)+(eff*0.2)

if promedio_fisica <13:
    print("promedio fisica:",promedio_fisica,"Desaprobado")
else:
    print("promedio fisica:",promedio_fisica,"Aprobado")

q1=float(input("Pactica calificada quimica 1: "))
q2=float(input("Pactica calificada quimica 2: "))
q3=float(input("Pactica calificada quimica 3: "))
epq=float(input("Examen Parcial quimica: "))
efq=float(input("Examen Final quimica: "))

promedio_quimica=(q1*0.1)+(q2*0.3)+(q3*0.1)+(epq*0.25)+(efq*0.25)
