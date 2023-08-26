n = int(input("altura de rectangulo: "))
ancho = 2 * n

for i in range(n):
    for j in range(ancho):
        print("*", end="")
    print()