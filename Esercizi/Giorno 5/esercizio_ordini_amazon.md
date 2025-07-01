# Esercizio: Analisi storico ordini Amazon con Pandas e Matplotlib

**Obiettivo:**  
Analizza i dati degli ordini Amazon di un utente, per scoprire le abitudini di spesa e visualizzare alcune statistiche.

---

## Dataset (`ordini_amazon.csv`)

Crea un file chiamato `ordini_amazon.csv` con questo esempio di dati:

```csv
Data,Articolo,Categoria,Prezzo,Quantità,Stato
2024-01-04,Cuffie Bluetooth,Elettronica,39.99,1,Consegnato
2024-01-18,T-shirt nera,Abbigliamento,14.99,2,Consegnato
2024-02-05,Libro Python,Libri,23.50,1,Consegnato
2024-02-18,Lampada LED,Casa,27.90,1,Consegnato
2024-03-03,Scarpe sportive,Abbigliamento,54.00,1,Consegnato
2024-03-20,Custodia telefono,Elettronica,12.99,1,Consegnato
2024-04-01,Pentola antiaderente,Casa,31.90,1,Consegnato
2024-04-14,Mouse wireless,Elettronica,18.99,1,Reso
2024-05-02,Libro Data Science,Libri,28.00,1,Consegnato
2024-05-16,Calzini sportivi,Abbigliamento,9.99,3,Consegnato
```

---

## ConsegnA

1. **Carica i dati con pandas.**
2. **Filtra solo gli ordini con stato "Consegnato".**
3. **Aggiungi una colonna "Totale"** (`Prezzo * Quantità`).
4. **Calcola il totale speso per categoria**.
5. **Crea un grafico a barre delle spese totali per categoria**.
6. **Visualizza l’andamento mensile della spesa totale** (grafico a linee).
7. **(Extra)** Qual è il mese in cui hai speso di più? E la categoria su cui hai speso di più?

---
