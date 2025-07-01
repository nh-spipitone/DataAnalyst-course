# Esercizio: Analisi delle vendite con pandas e matplotlib

**Obiettivo:**  
Usa **pandas** per analizzare un piccolo dataset di vendite e visualizza i dati con **matplotlib**.

---

## Dataset

Scarica o crea un file chiamato `vendite.csv` con il seguente contenuto:

```csv
Data,Prodotto,Quantità,Prezzo_unitario
2024-07-01,Pane,10,1.0
2024-07-01,Latte,5,1.2
2024-07-02,Pane,8,1.0
2024-07-02,Biscotti,3,2.0
2024-07-03,Latte,7,1.2
2024-07-03,Pane,6,1.0
2024-07-04,Biscotti,2,2.0
2024-07-04,Pane,5,1.0
2024-07-05,Latte,4,1.2
2024-07-05,Biscotti,5,2.0
```

---

## ConsegnA

1. **Leggi il file `vendite.csv` usando pandas.**
2. **Calcola il fatturato giornaliero** (quantità \* prezzo_unitario) per ogni riga e aggiungi una nuova colonna "Fatturato".
3. **Calcola il fatturato totale per ogni prodotto** (usando `groupby`).
4. **Crea un grafico a barre** che mostri il fatturato totale per ogni prodotto usando matplotlib.

---

### Domande extra (opzionali):

-   Qual è il prodotto che ha generato più fatturato?
-   Aggiungi una legenda o modifica i colori del grafico.

---
