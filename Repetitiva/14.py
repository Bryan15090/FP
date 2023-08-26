import os 
os.system("cls")

num = int(input("Número: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "no es un número primo")
            break
    else:
        print(num, "es un número primo")
else:
    print(num, "no es un número primo")