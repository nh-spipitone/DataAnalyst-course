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

"""------------------------------------------------------------------------------"""

# 7. **Inserimento controllato (`while`)**
#     - Continua a chiedere all’utente un numero finché non digita `0`.
#     - Alla fine mostra la somma e la media dei numeri inseriti (escludendo lo 0).
somma = 0
n = 0
while True:
    i = int(input("Ins un numero e 0 per uscire: "))
    if i == 0:
        break
    somma += i
    n +=1
if n != 0:
    print(f"La somma dei numeri è: {somma}\nLa media dei numeri è: {somma/n}")

"""------------------------------------------------------------------------------"""


## Livello 3 – Insiemi di dati più ricchi

"""------------------------------------------------------------------------------"""

# 8. **Analisi di dizionario**
spesa = {"mele": 3.2, "pane": 1.0, "latte": 1.5}
articolo = input("Articolo: ")
prezzo = float(input("Prezzo: "))
spesa.update({articolo:prezzo})
print(spesa)
max = 0
chiave = ""
tot = 0
for i in spesa:
    if spesa[i] > max:
        max = spesa[i]
        chiave = i
    tot += spesa[i]
spesa.pop(chiave)
print(f"Il prezzo totale è: {tot}, l'articolo più costoso è: {chiave}\n",spesa)

"""------------------------------------------------------------------------------"""

# 10. **Rubrica telefonica**
#     -   Implementa un semplice menu testuale con queste opzioni:
#         1. Aggiungi contatto (`nome` → `numero`)
#         2. Cerca numero per nome
#         3. Elenca tutti i contatti ordinati alfabeticamente
#         4. Elimina un contatto
#         5. Esci
#     -   Usa un **dizionario** per archiviare i dati, i **set** per verificare duplicati di nomi, cicli `while` per mantenere il programma attivo, e una serie di condizioni `if` per gestire il menu.

rubrica = {}
while True:
    scelta = int(input("MENU:\n1)Aggiungi contatto\n2)Cerca numero per nome\n3)Elenco contatti\n4)Elimina un contatto\n5)Esci\nIns. numero azione: "))
    if scelta == 1:
        print("Aggiungi Contatto.")
        nome = input("Nome: ").strip().capitalize()
        if nome in rubrica:
            print("Nome già salvato")
        else:
            numero = int(input("Numero: "))
            rubrica[nome] = numero
        
    elif scelta == 2:
        nome = input("Cerca Numero.\nNome: ").strip().capitalize()
        if nome in rubrica:
            print(rubrica.get(nome))

    elif scelta == 3:
        listaOrdinata = list(rubrica)
        listaOrdinata.sort()
        print(f"I numeri in rubrica sono:\n{listaOrdinata}")

    elif scelta == 4:
        nome = input("Elimina Numero.\nNome: ").strip().capitalize()
        if nome in rubrica:
            print(rubrica.pop(nome))

    elif scelta == 5:
        print("Sei uscito!")
        break
    else:
        print("Inserisci un numero valido!")