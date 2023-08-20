import os 
os.system("cls")

cantidad = int(input("Cantidad de dinero en soles: "))

billetes_200 = cantidad // 200
cantidad = cantidad % 200

billetes_100 = cantidad // 100
cantidad = cantidad % 100

billetes_50 = cantidad // 50
cantidad = cantidad % 50

billetes_20 = cantidad // 20
cantidad = cantidad % 20

billetes_10 = cantidad // 10
cantidad = cantidad % 10

monedas_5 = cantidad // 5
cantidad = cantidad % 5

monedas_2 = cantidad // 2
cantidad = cantidad % 2

monedas_1 = cantidad

print("Billetes de 200:", billetes_200)
print("Billetes de 100:", billetes_100)
print("Billetes de 50:", billetes_50)
print("Billetes de 20:", billetes_20)
print("Billetes de 10:", billetes_10)
print("Monedas de 5:", monedas_5)
print("Monedas de 2:", monedas_2)
print("Monedas de 1:", monedas_1)
