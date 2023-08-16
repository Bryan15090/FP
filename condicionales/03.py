import os 
os.system("cls")

a=int(input("Ingrese el angulo:"))

if a==0      : print("el angulo se clasifica como nulo")
if 0<a<90     : print("el angulo se clasifica como agudo")
if a==90     : print("el angulo se clasifica como recto")
if 90<a<180  : print("el angulo se clasifica como obtuso") 
if a==180    : print("el angulo se clasifica como llano")
if 180<a<360 : print("el angulo se clasifica como concavo")
if a==360    : print("el angulo se clasifica como completo")



