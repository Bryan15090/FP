import os
os.system("cls")

hora=int(input("Ingrese la hora:"))

if 0 > hora  or hora >23:
    print("hora invalida")
else:
    if hora== 0:
        print("12 am")
    elif hora < 12:
        print(str(hora)+" am")
    elif hora ==12:
        print("12 pm") 
    else:
        print(str(hora-12)+" pm")



