# Esercizi Python – ispirati al Power Point

## Livello 1 – Fondamentali

1. **Temperature in lista**

    - Crea una lista con le temperature massime della settimana.
    - Stampa la media, la temperatura più alta e quella più bassa.
    - Ordina la lista in ordine decrescente e mostrala.

2. **Tuple immutabili**

    - Trasforma la lista del punto 1 in una tupla.
    - Prova ad assegnare un nuovo valore al primo elemento: che errore ottieni? Spiega perché.

3. **Set per eliminare duplicati**

    - Data la lista `numeri = [3, 5, 3, 7, 5, 9, 3]`, usa un set per rimuovere i duplicati.
    - Confronta la lunghezza prima e dopo la trasformazione.

4. **Quiz sui tipi**
    - Scrivi una funzione `tipo_collezione(obj)` che ritorni la stringa `"lista"`, `"tupla"`, `"set"` o `"dizionario"` in base al tipo dell’oggetto passato.

---

## Livello 2 – Controllo di flusso

5. **Categorie di voto (if / elif / else)**

    - Chiedi all’utente un voto (0-100).
    - Stampa “Insufficiente” (<60), “Sufficiente” (60-69), “Buono” (70-79), “Ottimo” (80-89), “Eccellente” (90-100).

6. **Tabelline con `for` e `range`**

    - Usa un ciclo `for` per stampare la tabellina del 7 da 1 a 10.
    - Estendi l’esercizio per stampare le tabelline da 1 a 10 in un formato a griglia.

7. **Inserimento controllato (`while`)**
    - Continua a chiedere all’utente un numero finché non digita `0`.
    - Alla fine mostra la somma e la media dei numeri inseriti (escludendo lo 0).

---

## Livello 3 – Insiemi di dati più ricchi

8. **Analisi di dizionario**

    - Crea un dizionario `spesa = {"mele": 3.2, "pane": 1.0, "latte": 1.5}` dove i valori sono prezzi.
    - Aggiungi un nuovo prodotto scelto dall’utente.
    - Calcola il costo totale e rimuovi l’articolo più caro.

9. **Occorrenze di parole**
    - Chiedi all’utente una frase.
    - Restituisci un dizionario con la frequenza di ciascuna parola (ignora maiuscole/minuscole e punteggiatura).
    - Visualizza le 3 parole più comuni in ordine decrescente di frequenza.

---

## Sfida finale

10. **Rubrica telefonica**
    -   Implementa un semplice menu testuale con queste opzioni:
        1. Aggiungi contatto (`nome` → `numero`)
        2. Cerca numero per nome
        3. Elenca tutti i contatti ordinati alfabeticamente
        4. Elimina un contatto
        5. Esci
    -   Usa un **dizionario** per archiviare i dati, i **set** per verificare duplicati di nomi, cicli `while` per mantenere il programma attivo, e una serie di condizioni `if` per gestire il menu.

---

### Consigli per lo studio

-   Dopo aver risolto un esercizio, prova a spiegare a voce alta perché la tua soluzione funziona: consolida la comprensione.
-   Se hai dubbi, stampa sempre i valori intermedi (con `print`) per vedere che cosa succede passo-passo.
-   Vuoi le soluzioni o degli hint dettagliati? Fammi sapere e li preparerò!
