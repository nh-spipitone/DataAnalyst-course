numbers = [12, 7, 9, 20, 33, 4, 18]
numeri_pari = []
numeri_quadri =[]

for numero in numbers:
    if numero % 2 == 0:
        numeri_pari.append(numero)
    numeri_quadri.append(numero**2)

print("numeri pari", numeri_pari)
print("numeri al quadrato", numeri_quadri)
print("la lunghezza dei numeri pari è:", len(numeri_pari))
print("la lunghezza dei numeri quadrati è:", len(numeri_quadri))
    
