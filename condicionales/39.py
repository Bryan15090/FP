import os
os.system("cls")

bHorasAusencia= float (input("Horas ausencia : ")) <=1.5
bTDefectuoso = int (input("Tornillos Defectuosos :")) <300
bTbuenos = int (input("Tornillos buenos : ")) > 10000

if not bHorasAusencia and not bTDefectuoso and not bTbuenos : grado = 5
elif bHorasAusencia and not bTDefectuoso and not bTbuenos : grado = 7
elif not bHorasAusencia and bTDefectuoso and not bTbuenos : grado = 8
elif not bHorasAusencia and not bTDefectuoso and bTbuenos : grado = 9
elif bHorasAusencia and bTDefectuoso and not bTbuenos : grado = 12
elif bHorasAusencia and not bTDefectuoso and bTbuenos : grado = 13
elif not bHorasAusencia and bTDefectuoso and bTbuenos : grado = 15
elif bHorasAusencia and bTDefectuoso and bTbuenos : grado = 20