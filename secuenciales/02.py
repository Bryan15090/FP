import os 
os.system("cls")

metro=int(input("Ingrese la cantidad de metros: "))

centimetro = metro * 100 
pulgada = centimetro//2.54
pies = pulgada//12
yarda = pies//3
print("Valor de centimetros: ",centimetro)
print("Valor de pies: ",pies)
print("Valor de pulgadas: ",pulgada)
print("Valor de yarda: ",yarda)
