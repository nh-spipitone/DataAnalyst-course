## Consegna

# Realizza un breve programma Python che rispetti **solo** i seguenti vincoli:

# 1. All’inizio del codice è già presente la lista di stringhe

#     ```python
#     nomi = ["Anna", "Marco", "Elena", "Osvaldo", "Luca", "Irene", "Giorgio", "Umberto"]
#     ```

# 2. Scorri la lista _una sola volta_ usando un ciclo a tua scelta (`for` **oppure** `while`).

# 3. Durante lo scorrimento, dividi i valori in **due nuove liste**:

#     - `vocali` → contiene i nomi che iniziano con una vocale (a, e, i, o, u, maiuscole o minuscole) (comando per inizia è .startswith("valore con cui deve iniziare") esempio nome.startswith )
#     - `consonanti` → contiene tutti gli altri nomi

# 4. Al termine del ciclo stampa le due liste con un output simile a:

#     ```
#     Nomi che iniziano con vocale: ['Anna', 'Elena', 'Osvaldo', 'Irene', 'Umberto']
#     Nomi che iniziano con consonante: ['Marco', 'Luca', 'Giorgio']
#     ```

# > **Limitazioni obbligatorie**
# >
# > -   Non usare funzioni, list comprehension, librerie esterne o altre strutture avanzate.
# > -   Usa soltanto variabili semplici, liste/tuple, cicli `for` o `while` e l’istruzione `if`.

# Buon lavoro!

nomi = ["Anna", "Marco", "Elena", "Osvaldo", "Luca", "Irene", "Giorgio", "Umberto"]
vocali = []
consonanti = []

for nome in nomi:

    lista_vocali = ('a', 'e', 'i', 'o', 'u')

    if nome.lower().startswith(lista_vocali):
        vocali.append(nome)
    else:
        consonanti.append(nome)
        

print(f'Nomi che iniziano con vocali: {vocali}')
print(f'Nomi che iniziano con consonanti: {consonanti}')

