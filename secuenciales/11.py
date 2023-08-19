import os
os.system("cls")

n=int(input("1er Numero de tres cifras: " ))
nu=int(input("2do Numero de tres crifras: " ))

n3 = n % 10
n2 = ( n % 100) //10
n1 = ( n - ( n % 100) ) // 100

nu3 = nu % 10
nu2 = ( nu % 100) // 10
nu1 = ( nu - ( n % 100)) // 100
 
print("Numeros: ",n,"y",nu)

print("Numeros Intercambiados: ",str(nu3)+str(n2)+str(nu1),"y",str(n3)+str(nu2)+str(n1))

