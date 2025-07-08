## Mini-esercizio: **Pandas + SQLAlchemy + PostgreSQL** (senza CSV)

Lo scopo è mostrare l’intero ciclo **DataFrame → PostgreSQL → Pandas → analisi** impiegando SQLAlchemy, senza leggere o scrivere file esterni: il dataset viene costruito direttamente in codice.

---

### 1  Costruzione del DataFrame in memoria

```python
import pandas as pd
from datetime import date

# Dati d’esempio (potete modificarli o ampliarli)
vendite_data = [
    {"id_vendita": 1, "data_vendita": date(2025, 1, 2), "titolo": "Il Nome della Rosa",    "autore": "Umberto Eco",   "quantita": 2, "prezzo_unitario": 12.90},
    {"id_vendita": 2, "data_vendita": date(2025, 1, 3), "titolo": "1984",                  "autore": "George Orwell", "quantita": 1, "prezzo_unitario": 10.50},
    {"id_vendita": 3, "data_vendita": date(2025, 1, 3), "titolo": "Il barone rampante",    "autore": "Italo Calvino", "quantita": 3, "prezzo_unitario": 11.20},
    {"id_vendita": 4, "data_vendita": date(2025, 1, 5), "titolo": "Il Nome della Rosa",    "autore": "Umberto Eco",   "quantita": 1, "prezzo_unitario": 12.90},
    # …aggiungete altre righe a piacere…
]

df = pd.DataFrame(vendite_data)
```

---

### 2  Connessione a PostgreSQL e salvataggio

```python
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql://student:password@localhost:5432/libreria_db",
    echo=False   # True per loggare l’SQL generato
)

# Scrive (o sovrascrive) la tabella "vendite"
df.to_sql("vendite", engine, if_exists="replace", index=False)
```

---

### 3  Query di esempio (SQL “puro”)

```python
query = text("""  # triple quotes escaped inside python string
    SELECT autore,
           SUM(quantita)                          AS copie_totali,
           ROUND(SUM(quantita * prezzo_unitario), 2) AS ricavo_totale
    FROM vendite
    GROUP BY autore
    ORDER BY ricavo_totale DESC;
""")

risultato = pd.read_sql(query, engine)
print(risultato)
```

---

### 4  Compiti da svolgere

1. **Top 5 autori per copie vendute**  
   _Suggerimento_: `ORDER BY copie_totali DESC LIMIT 5`.

2. **Ricavo mensile**

    - In Pandas: `df['mese'] = df['data_vendita'].dt.to_period('M')` e poi `groupby('mese')`.
    - In SQL: `DATE_TRUNC('month', data_vendita)`.

3. **Margine medio per titolo**  
   Supponendo un costo fisso di **€ 5** a copia: `margine = prezzo_unitario - 5`, quindi calcolare il margine totale per titolo.

4. **Indice e performance**  
   Create un indice su `data_vendita` (`CREATE INDEX ...`) e confrontate i piani di esecuzione con `EXPLAIN ANALYZE` prima e dopo l’indice per una query di intervallo date.

---

### 5 Spunti di riflessione

-   **Push-down vs. in-memory**: quando conviene spostare il carico computazionale sul database rispetto a Pandas?
-   **Scalabilità**: cosa succede se il dataset diventa più grande della RAM?
-   **Transazioni**: per carichi rilevanti usare blocchi `with engine.begin(): …` per garantire atomicità e performance.
-   Differenza fra `to_sql(..., if_exists='append')` e `'replace'` in termini di gestione versioni/cronologia dati.

---
