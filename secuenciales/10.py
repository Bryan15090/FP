import os 
os.system("cls")

N= int(input("Numero de 4 cifras : "))

N4 = N % 10
N3 = ( N % 100 ) // 10
N2 = ( N % 1000) // 100
N1 = ( N - ( N % 1000)) // 1000

print("Numero al revez: ",str(N4)+str(N3)+str(N2)+str(N1))