# 3: Data una lista di numeri,
# # a) Usando un singolo ciclo, crea due liste: una con i numeri pari e una con i numeri dispari.
# # b) Stampa le due liste ottenute.

numeri = [5, 12, 7, 4, 21, 8, 3, 18, 10]

numeri_pari = []
numeri_dispari = []

for num in numeri:
    if num % 2 == 0:
        numeri_pari.append(num)
    else:
        numeri_dispari.append(num)

print(f"Pari:    {numeri_pari}")
print(f"Dispari: {numeri_dispari}")