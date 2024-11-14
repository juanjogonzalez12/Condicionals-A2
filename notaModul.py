#Programa fet per Juan José González Rosas, alumne de DAM 1B.
#14/11/2024
nota = 6.25
#nota del mòdul.
if nota <= 0:
    print("Nota no vàlida.")
elif nota < 5:
    print("Suspès.")
elif nota <= 6.5:
    print("Aprovat.")
elif nota <= 8:
    print("Notable.")
elif nota > 8:
    print("Excel·lent.")
elif nota > 10:
    print("Nota no vàlida.")