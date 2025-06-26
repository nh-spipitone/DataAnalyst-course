# Esercizi Python – ispirati al Power Point

# Livello 1 – Fondamentali

"""------------------------------------------------------------------------------"""

# 1. **Temperature in lista**
#     - Crea una lista con le temperature massime della settimana.
#     - Stampa la media, la temperatura più alta e quella più bassa.
#     - Ordina la lista in ordine decrescente e mostrala.
temp = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
somma = 0
for i in temp:
    somma += i
temp.sort(reverse=True)
print(f"la media è: {somma/len(temp)}\n{temp}")

"""------------------------------------------------------------------------------"""

# 2. **Tuple immutabili**
#     - Trasforma la lista del punto 1 in una tupla.
#     - Prova ad assegnare un nuovo valore al primo elemento: che errore ottieni? Spiega perché.
tempTupla = tuple(temp)
try:
    tempTupla[0] = 1
except:
    print("Se vedi questo messaggio è perché il try ha dato un errore in console. La tupla non è modificabile")

"""------------------------------------------------------------------------------"""

# 3. **Set per eliminare duplicati**
#     - Data la lista `numeri = [3, 5, 3, 7, 5, 9, 3]`, usa un set per rimuovere i duplicati.
#     - Confronta la lunghezza prima e dopo la trasformazione.
numeri = [3, 5, 3, 7, 5, 9, 3]
setNumeri = list(set(numeri))
print(f"{numeri}\n{setNumeri}")

"""------------------------------------------------------------------------------"""

# 4. **Quiz sui tipi**
#     - Scrivi una funzione `tipo_collezione(obj)` che ritorni la stringa `"lista"`, `"tupla"`, `"set"` o `"dizionario"` in base al tipo dell’oggetto passato.
def tipo_collezione(oggetto):
    print(type(oggetto))
tipo_collezione(tempTupla)

"""------------------------------------------------------------------------------"""

## Livello 2 – Controllo di flusso

"""------------------------------------------------------------------------------"""

# 5. **Categorie di voto (if / elif / else)**
#     - Chiedi all’utente un voto (0-100).
#     - Stampa “Insufficiente” (<60), “Sufficiente” (60-69), “Buono” (70-79), “Ottimo” (80-89), “Eccellente” (90-100).
voto = 0
while voto>100 or voto<=0:
    voto = int(input("Ins voto tra 1-100: "))
if voto >= 90:
    print("Eccellente")
elif voto >= 80:
    print("Ottimo")
elif voto >= 70:
    print("Buono")
elif voto >= 60:
    print("Sufficiente")
else:
    print("Insufficiente")

"""------------------------------------------------------------------------------"""

# 6. **Tabelline con `for` e `range`**
#     - Usa un ciclo `for` per stampare la tabellina del 7 da 1 a 10.
#     - Estendi l’esercizio per stampare le tabelline da 1 a 10 in un formato a griglia.
for i in range(11):
    print(f"Tabellina del numero {i}:")
    for i2 in range(11):
        print(f"-   {i}X{i2}={i*i2}")