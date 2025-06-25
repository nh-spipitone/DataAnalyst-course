## Consegna (livello intermedio – solo costrutti base)

Realizza un programma Python che rispetti **unicamente** i seguenti strumenti:

-   liste/tuple
-   cicli `for` **oppure** `while`
-   istruzione `if`
-   variabili semplici (`int`, `float`, `str`, …)
-   funzioni built-in basilari (`print`, `len`)

---

### Dati iniziali

All’inizio del file di codice trovi già questa lista di interi (positivi, negativi e zeri):

```python
numeri = [7, -2, 0, 15, -9, 3, 0, 22, -5, 11, -1]
```

---

### Obiettivo

Scorrendo la lista **una sola volta** (un solo ciclo dall’inizio alla fine), completa i passaggi sotto **nell’ordine indicato**.

| Passo | Operazione da eseguire                                                                                                                                             | Vincoli                                   |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------- |
| 1     | Crea tre nuove liste vuote: `positivi`, `negativi`, `zeri`.                                                                                                        | Solo assegnazione semplice.               |
| 2     | Durante lo scorrimento, inserisci ogni valore della lista originale in una delle tre nuove liste, a seconda che sia maggiore di 0, minore di 0, oppure uguale a 0. | Usa solo `if` (anche `elif` e `else`).    |
| 3     | **Contestualmente** (senza un secondo ciclo) calcola la **somma totale** dei valori, salvandola in una variabile `totale`.                                         | Aggiorna `totale` dentro lo stesso ciclo. |
| 4     | Al termine del ciclo, calcola la **media aritmetica** dei valori (usa `totale` e `len(numeri)`) e salvala in `media`.                                              | Nessuna funzione aggiuntiva.              |
| 5     | Fai un **secondo ciclo** soltanto sulla lista `positivi` per creare una quarta lista `sopra_media` con tutti i numeri positivi strettamente maggiori della media.  | Solo un altro ciclo con `if`.             |
| 6     | Stampa in ordine: `positivi`, `negativi`, `zeri`, `media` (come numero), `sopra_media`.                                                                            | Formato libero ma chiaro.                 |

Esempio di output possibile (i valori cambiano se modifichi `numeri`):

```
Positivi:       [7, 15, 3, 22, 11]
Negativi:       [-2, -9, -5, -1]
Zeri:           [0, 0]
Media totale:   3.6363636363636362
Positivi > media: [7, 15, 22, 11]
```

---

### Suggerimenti

-   Per calcolare `media` dopo il primo ciclo:
    ```python
    media = totale / len(numeri)
    ```
-   Usa `.append()` per aggiungere elementi alle liste.
-   Ricorda di **non** usare funzioni avanzate o scorciatoie; l’esercizio serve ad allenare cicli e condizioni di base.

Buon lavoro!
