factorial = 1
numero = int(input("Numero a calcular el factorial:"))

for i in range(numero):
    print (factorial,"*",numero)
    factorial=factorial*numero
    numero=numero - 1

print("El factorial del numero es: ",(factorial))
