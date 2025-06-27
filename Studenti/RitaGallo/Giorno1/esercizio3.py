numeri = [5, 12, 7, 4, 21, 8, 3, 18, 10]

numeri_pari = []
numeri_dispari =[]

for n in numeri:
    if n % 2 == 0:
        numeri_pari.append(n)

    else:
        numeri_dispari.append(n)

print("i numeri pari sono:", numeri_pari)
print("i numeri dispari sono:", numeri_dispari)
