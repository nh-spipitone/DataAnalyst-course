# ## Consegna

# Realizza un breve programma Python che rispetti **solo** i seguenti vincoli:

# 1. All’inizio del codice è già presente la lista di interi

#     ```python
#     numeri = [5, 12, 7, 4, 21, 8, 3, 18, 10]
#     ```

# 2. Scorri la lista _una sola volta_ usando un ciclo a tua scelta (`for` **oppure** `while`).

# 3. Durante lo scorrimento, dividi i valori in **due nuove liste**:

#     - `pari` → contiene tutti i numeri pari
#     - `dispari` → contiene tutti i numeri dispari

# 4. Al termine del ciclo stampa le due liste con un output simile a:

#     ```
#     Pari:    [12, 4, 8, 18, 10]
#     Dispari: [5, 7, 21, 3]
#     ```

# > **Limitazioni obbligatorie**
# >
# > -   Non usare funzioni, list comprehension, librerie esterne o altre strutture avanzate.
# > -   Usa soltanto variabili semplici, liste/tuple, cicli `for` o `while` e l’istruzione `if`.

numeri = [5, 12, 7, 4, 21, 8, 3, 18, 10]

pari = []
dispari = []

for num in numeri:
    if num % 2 == 0:
        pari.append(num)
    else:
        dispari.append(num)

print(f'I numeri pari sono: {pari}')
print(f'I numeri dispari sono: {dispari}')