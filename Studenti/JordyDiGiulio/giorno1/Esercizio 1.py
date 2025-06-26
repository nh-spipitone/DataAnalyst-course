# Lista di numeri da elaborare
numbers = [12, 7, 9, 20, 33, 4, 18]

# Inizializzazione di due liste vuote
numeri_pari = []  # Conterrà i numeri pari
numeri_quadri = []  # Conterrà i quadrati di tutti i numeri

# Ciclo per elaborare ogni numero nella lista
for n in numbers:
    # Verifica se il numero è pari (resto della divisione per 2 è 0)
    if n % 2 == 0:
        numeri_pari.append(n)  # Aggiunge il numero pari alla lista

    # Calcola e aggiunge il quadrato del numero (per tutti i numeri)
    numeri_quadri.append(n**2)

# Stampa i risultati
print(numeri_pari)  # Stampa la lista dei numeri pari
print(numeri_quadri)  # Stampa la lista dei quadrati

# Stampa le lunghezze delle liste
print("La lunghezza dei numeri pari è: ", len(numeri_pari))
print("La lunghezza dei numeri quadrati è: ", len(numeri_quadri))
