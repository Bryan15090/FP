import os
os.system("cls")

codigo = int (input("Codigo:"))

bDiv2 = codigo % 2 == 0
bDiv3 = codigo % 3 == 0
bDiv5 = codigo % 5 == 0

if bDiv2 and bDiv3 and bDiv5 : tipo = "Administrativo"
if not bDiv2 and bDiv3 and bDiv5 : tipo = "Directivo"
if bDiv2 and not bDiv3 and not bDiv5 : tipo = "Vendedor"
if not bDiv2 and not bDiv3 and not bDiv5 : tipo = "Seguridad"

print( f"Tipo: {tipo}")