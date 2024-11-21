#Programa fet per Juan José González Rosas, alumne de DAM 1B.
#21/11/2024
print("Esbrina el número secret pista(és troba entre els números: 100 i 400.)")
num = 0
while (num < 100 or num > 400):
    num = int(input())

    print("Incorrecte.")
    if (num < 100 or num > 400):
        print("Incorrecte.")
    elif (num == 150):
        print("Ho has esbrinat.")