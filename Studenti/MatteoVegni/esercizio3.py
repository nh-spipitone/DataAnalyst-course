numeri = [5, 12, 7, 4, 21, 8, 3, 18, 10]

numeri_dispari=[]
numeri_pari = []

for n in numeri:
    if n % 2 == 0:
        numeri_pari.append(n)
    else:
        numeri_dispari.append(n)

print("il numero è pari:", numeri_pari)
print("il numero è dispari:", numeri_dispari)
