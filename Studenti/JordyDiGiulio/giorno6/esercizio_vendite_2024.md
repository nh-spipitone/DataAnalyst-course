
# Esercizio: *Vendite di prodotti nel 2024*
Basato sui concetti introdotti fino alla **slide 8** (creazione di *Series* e *DataFrame*, filtri di base `.loc`/boolean indexing, grafici con Matplotlib).

---

## 1 – Crea (o ricarica) il DataFrame
```python
import pandas as pd

dati = {
    "Mese": ["Gen", "Feb", "Mar", "Apr"] * 3,
    "Prodotto": ["A"]*4 + ["B"]*4 + ["C"]*4,
    "Quantità": [120, 135, 150, 145,   # A
                 90,  95,  100, 105,    # B
                 60,  65,   70,  80]    # C
}
df = pd.DataFrame(dati)
```

---

## 2 – Esplora
```python
df.head(6)
df.dtypes
```

---

## 3 – Filtri base (ripasso)
1. **Righe del prodotto B**  
   ```python
   df[df["Prodotto"] == "B"]
   ```
2. **Quantità > 100**  
   ```python
   df[df["Quantità"] > 100]
   ```
3. **Con `.loc`:** *Mese* e *Quantità* del prodotto **A**  
   ```python
   df.loc[df["Prodotto"] == "A", ["Mese", "Quantità"]]
   ```

---

## 3 bis – Filtri extra (novità)

| Obiettivo | Esempio di sintassi |
|-----------|--------------------|
| Prodotto C con quantità ≤ 70 | `df[(df["Prodotto"] == "C") & (df["Quantità"] <= 70)]` |
| Mesi di Gen o Feb | `df[df["Mese"].isin(["Gen", "Feb"])]` |
| Quantità compresa tra 90 e 130 (estremi inclusi) | `df[df["Quantità"].between(90, 130)]` |
| Tutti i dati tranne Aprile | `df[df["Mese"] != "Apr"]` |

---

## 4 – Aggregato semplice
```python
totali = df.groupby("Prodotto")["Quantità"].sum()
print(totali)  # Atteso: A=550, B=390, C=275
```

---

## 5 – Visualizzazione con due subplot
```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Subplot 1 – Grafico a barre dei totali
totali.plot(kind="bar", ax=axes[0])
axes[0].set_title("Totale vendite per prodotto")
axes[0].set_ylabel("Unità vendute")

# Subplot 2 – Andamento mensile del prodotto B
prod_b = df[df["Prodotto"] == "B"]
axes[1].plot(prod_b["Mese"], prod_b["Quantità"], marker="o")
axes[1].set_title("Prodotto B – andamento gennaio‑aprile")
axes[1].set_ylabel("Unità vendute")

plt.tight_layout()
plt.show()
```

### Cosa osservare
* Tre barre con altezze 550, 390, 275.
* Linea che sale da 90 a 105.
* Il layout è ottenuto con `plt.subplots(1, 2)`.

---

## 6 – Challenge facoltativo
1. Calcola il **totale per mese**:
   ```python
   df.groupby("Mese")["Quantità"].sum()
   ```
2. Crea un terzo filtro con l’espressione:

   > (Prodotto == "A" & Quantità > 130) | (Prodotto == "C" & Quantità < 70)

3. Sostituisci il line plot del secondo subplot con un **scatter plot**:
   ```python
   axes[1].scatter(prod_b["Mese"], prod_b["Quantità"])
   ```

---

### Soluzione attesa (rapida)
* **DataFrame:** 12 righe × 3 colonne.
* **Filtri:** prodotto B → 4 righe; Quantità > 100 → 7 righe.
* **Serie `totali`:** A = 550, B = 390, C = 275.

---

Buon lavoro!  
_(Per dubbi o approfondimenti, chiedi pure.)_
