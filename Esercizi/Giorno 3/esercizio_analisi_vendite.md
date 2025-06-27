# Esercizio: Analisi di base di un dataset di vendite con **funzioni**, `if`, `while` e **pandas**

> Livello: _beginner data analyst_ – l’obiettivo è prendere dimestichezza con la lettura di file CSV, la gestione del flusso di controllo in Python e le prime operazioni di analisi dati con **pandas**.

---

## 1. Dati di partenza

Scarica (o crea) un file **`vendite.csv`** con le seguenti colonne:

| data       | prodotto | quantita | prezzo_unitario |
|------------|----------|----------|-----------------|
| 2025-01-02 | Penna    | 30       | 1.20            |
| 2025-01-02 | Quaderno | 15       | 2.50            |
| 2025-01-03 | Penna    | 25       | 1.20            |
| …          | …        | …        | …               |

Sono sufficienti **10–20 righe** di esempio.

---

## 2. Requisiti dello script `analisi_vendite.py`

### 2.1. Funzione `carica_dati(percorso: str) -> pd.DataFrame`
* Usa `pd.read_csv`.
* Se il file **non esiste** solleva `FileNotFoundError`.
* Se mancano colonne obbligatorie, stampa un messaggio d’errore e **termina** con `sys.exit(1)`.

### 2.2. Funzione `riepilogo_vendite(df: pd.DataFrame) -> pd.DataFrame`
Restituisce un **DataFrame** di riepilogo con:
* `totale_quantita` (somma di `quantita`)
* `totale_ricavi` (`quantita * prezzo_unitario`)
* `ordine_medio` (`totale_ricavi / numero_righe`)

### 2.3. Ciclo interattivo (`while True`)
1. Chiedi all’utente di inserire un **nome prodotto** (o `exit` per uscire).
2. Se il prodotto esiste nel dataset:  
   * Filtra il DataFrame.  
   * Stampa a video **quantità totale** e **ricavi totali** di quel prodotto.
3. Altrimenti avvisa che il prodotto non è presente.

### 2.4. Salvataggio
* Salva il DataFrame di riepilogo in `riepilogo_vendite.csv`.
* Stampa “File salvato!” solo se il salvataggio ha successo (usa `if` e `try / except`).

---

## 3. Vincoli tecnici

* **Non** usare librerie diverse da `pandas` e quelle della **standard library** (`os`, `sys`, `csv`, …).
* Mantieni il codice in un **blocco `if __name__ == "__main__":`**.
* Usa *type hints* e una breve **docstring** per ogni funzione.

---

## 4. Output atteso (esempio)

```
> python analisi_vendite.py vendite.csv
✅ Dati caricati: 15 righe.

==== RIEPILOGO GENERALE ====
Totale quantità: 350
Totale ricavi  : € 678.50
Ordine medio   : € 45.23

— Digita un nome prodotto (exit per uscire) —
> Penna
Penna → Quantità: 180 / Ricavi: € 216.00
> Matita
⚠️  Prodotto "Matita" non trovato.
> exit
📄 Report salvato in riepilogo_vendite.csv
```

---

## 5. Extra facoltativi

1. **Gestione date**: carica `data` come tipo `datetime` e permetti filtri per intervallo di date.  
2. **Visualizzazione**: usa matplotlib per disegnare un grafico a barre dei ricavi per prodotto.  
3. **Test**: scrivi 3–4 test con `pytest` che verifichino le funzioni core.

---

_Suggerimento_: risolvi i requisiti **uno alla volta**, committando su Git ad ogni step. Cerca di far passare `flake8` o `ruff` prima di procedere all’extra!
