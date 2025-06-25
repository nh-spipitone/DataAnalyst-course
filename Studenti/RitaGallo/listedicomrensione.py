
numbers = [12, 7, 9, 20, 33, 4, 18]

numeri_pari = [] 
numeri_quadri = []
for n in numbers:
    if n % 2 == 0:
        numeri_pari.append(n)
    numeri_quadri.append(n**2)

print(numeri_pari)
print(numeri_quadri)

print("la lunghezza dei numeri pari è:", len(numeri_pari))

print("la lunghezza dei numeri quadrari è:", len(numeri_quadri))