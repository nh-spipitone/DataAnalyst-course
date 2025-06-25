"""ESERCIZIO 1: GESTIONE MAGAZZINO

Obiettivo: Imparare a modificare una lista in modo sicuro, controllando prima se un elemento esiste.

1. Crea una lista chiamata `prodotti` che contenga le seguenti stringhe: "tastiera", "mouse", "monitor", "cuffie".
2. Stampa la lista iniziale.
3. Definisci una variabile `prodotto_da_rimuovere` e assegnale il valore "mouse".
4. Scrivi una condizione `if` per controllare se `prodotto_da_rimuovere` è presente nella lista `prodotti`.
5. Se è presente, rimuovilo dalla lista e stampa un messaggio di conferma (es. "Il prodotto 'mouse' è stato rimosso.").
6. Se non è presente, stampa un messaggio di avviso (es. "Il prodotto 'mouse' non era in magazzino.").
7. Alla fine, stampa la lista aggiornata.
8. Ripeti i passaggi da 3 a 7, ma questa volta prova a rimuovere il prodotto "webcam" (che non è presente nella lista) per verificare che il tuo codice gestisca correttamente anche questo caso."""

prodotti = ["tastiera", "mouse", "monitor", "cuffie"]
print(prodotti)
prodotto_da_rimuovere = "webcam"
if prodotto_da_rimuovere in prodotti:
    prodotti.remove(prodotto_da_rimuovere)
    print(f"Il prodotto '{prodotto_da_rimuovere}' è stato rimosso.")
else:
    print(f"Il prodotto '{prodotto_da_rimuovere}' non era in magazzino.")
print(prodotti)

"""ESERCIZIO 2: CARTA D'IDENTITÀ VIRTUALE

Obiettivo: Lavorare con i dati fissi di una tupla e usare una condizione per interpretarli.

1. Crea una tupla chiamata `utente` che contenga 3 elementi: un nome (stringa), un cognome (stringa) e un'età (numero). Esempio: ("Maria", "Rossi", 25).
2. Estrai i valori dalla tupla in tre variabili separate: `nome`, `cognome`, `eta`.
3. Scrivi una condizione `if` per controllare se il valore della variabile `eta` è maggiore o uguale a 18.
4. Se l'età è maggiore o uguale a 18, stampa un messaggio come: "Maria Rossi è maggiorenne."
5. Altrimenti, stampa un messaggio come: "Maria Rossi è minorenne."""

utente = ("Maria","Rossi",25)
nome = utente[0]
cognome = utente[1]
eta = utente[2]
if eta >= 18:
    print("Maria Rossi è maggiorenne.")
else:
    print("Maria Rossi è minorenne.")
