#Programa fet per Juan José González Rosas, alumne de DAM 1B.
#21/11/2024
nums = [1, 4, 5, 67, 34, 55, 78, 90, 2, 44, 65, 33, 35, 50]
print("Parells: ")
for num in nums:
    if (num % 2 == 1):
        continue

    print(num)
print("\nImparells: ")
for num in nums:
    if (num % 2 == 0):
        continue
    
    print(num)