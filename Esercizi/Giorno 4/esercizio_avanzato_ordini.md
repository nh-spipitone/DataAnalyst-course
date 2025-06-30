# 📝 Esercizio avanzato: Analisi ordini di un e-commerce

## Scenario

Hai a disposizione un file `ordini.csv` che contiene i dati di un piccolo e-commerce nell’ultimo mese. Ogni riga rappresenta un ordine ricevuto.

Esempio dati:

```
OrdineID,Data,Cliente,Prodotto,Quantità,Prezzo_unitario,Spedito
1001,2024-06-01,Mario Rossi,Laptop,1,800.0,True
1002,2024-06-01,Giulia Bianchi,Mouse,2,15.5,True
1003,2024-06-02,Luigi Verdi,Monitor,1,200.0,False
1004,2024-06-03,Mario Rossi,Mouse,1,15.5,True
1005,2024-06-03,Anna Neri,Laptop,2,790.0,True
1006,2024-06-03,Giulia Bianchi,Monitor,1,195.0,False
1007,2024-06-04,Anna Neri,Mouse,3,14.0,True
```

---

## Punti della consegna

1. **Carica** il file `ordini.csv` in un DataFrame Pandas e visualizza le prime 5 righe.
2. **Aggiungi** una colonna “Totale” calcolando per ogni ordine `Quantità * Prezzo_unitario`.
3. **Filtra** gli ordini che **NON sono ancora stati spediti** e stampa la lista (con Data, Cliente, Prodotto e Totale).
4. **Calcola** il fatturato totale per ogni cliente (somma dei Totali) e ordina la classifica decrescente.
5. **Trova** il prodotto più venduto in termini di quantità totale.
6. **(Extra)** Trova per ogni giorno il fatturato giornaliero (anche con un grafico a barre).
7. **(Extra)** Calcola la media del prezzo unitario per ogni prodotto.

---

## Suggerimenti

- Usa i metodi `groupby`, `sum`, `sort_values`, `loc`, ecc.
- Per il grafico puoi usare `matplotlib` (`import matplotlib.pyplot as plt`).

---
