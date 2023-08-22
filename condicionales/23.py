import os 
os.system("cls")

nota_matematica=int(input("nota de matematica: "))
nota_fisica=int(input("nota de fisica: "))

propina_matematica= 0
propina_fisica= 0
regalo = (nota_matematica+nota_fisica)/2

if nota_matematica >=17 :
     propina_matematica= 3 
if nota_matematica <17 :
    propina_matematica=1    
if nota_fisica >=15 :
     propina_fisica= 2
if nota_fisica <15 :
     propina_fisica=0.05
if regalo>=16 :
     print("Obsequio un reloj")

propinatotal=propina_matematica+propina_fisica

print("Propina total : ",propinatotal)