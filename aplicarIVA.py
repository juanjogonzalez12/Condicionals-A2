#Programa fet per Juan José González Rosas, alumne de DAM 1B.
#14/11/2024
salari = 5000
#Salari d'una persona
if salari < 15000:
    print ("S'aplicarà un IVA del 0%")
    iva = 0
elif salari < 30000:
    print ("S'aplicarà un IVA del 10%")
    iva = 10
elif salari < 60000:
    print ("S'aplicarà un IVA del 21%")
    iva = 21
else:
    print ("S'aplicarà un IVA del 21%")
    iva = 21

IVA = salari * (iva / 100)
print(f"El salari és de {salari} i l'iva és del {iva}%.")
print(f"L'import de l'iva és {IVA}€.")