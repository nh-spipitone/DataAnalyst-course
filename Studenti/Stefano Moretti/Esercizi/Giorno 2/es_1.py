numbers = [12, 7, 9, 20, 33, 4, 18]

numeri_pari = []
numeri_quadri = []
for n in numbers:
    if n % 2 == 0:
        numeri_pari.append(n)
    numeri_quadri.append(n ** 2)


numeri_dispari = []
for n in numbers:
    if n % 2 != 0:
        numeri_dispari.append(n)

print(f"I numeri pari sono: {numeri_pari}, quelli dispari sono: {numeri_dispari} e i loro quadrati sono: {numeri_quadri}")

print(f"La lunghezza della lista dei numeri pari è: {len(numeri_pari)}")

