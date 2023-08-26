import os
os.system("cls")

count = 0
n1=int(input("Numero de 3 cifras: "))

for num in range(n1):
    if str(num) == str(num)[::-1]:
        count += 1

print(count)