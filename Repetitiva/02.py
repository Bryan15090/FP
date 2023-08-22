import os 
os.system("cls")

multiplicando=int(input("Multiplicando: "))
multiplicador=int(input("Multiplicador: "))

# producto=0
# while multiplicador>0:
#     producto+= multiplicando
#     multiplicador-=1

producto=0
for x in range(multiplicador) :
    producto+= multiplicando

print( f"Producto : {producto}" )