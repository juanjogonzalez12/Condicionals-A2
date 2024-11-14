#Programa fet per Juan José González Rosas, alumne de DAM 1B.
#14/11/2024
print("Escriu dos números per determinar quin és major dels dos.")
print("Primer número:")
primerNum = input()
#Demana el primer número.
print("Segon número:")
segonNum = input()
#Demana el segon número.
if primerNum == segonNum:
    print("Els dos números són iguals.")
#Són iguals?
elif primerNum > segonNum:
    print(f"El primer {primerNum} és més gran que el segon {segonNum}.")
#Primera sortida en càs de que el primer número marcat sigui més gran que el segon.
else:
    print(f"El segon {segonNum} és més gran que el primer {primerNum}.")
#Segona sortida en càs de que la primera sortida no hagi sigut exitosa.