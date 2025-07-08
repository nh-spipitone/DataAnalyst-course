import pandas as pd
from datetime import date
import sqlite3

conn = sqlite3.connect("my_database.db")

vendite_data = [
    {"id_vendita": 1, "data_vendita": date(2025, 1, 2).strftime("%Y-%m-%d"), "titolo": "Il Nome della Rosa",    "autore": "Umberto Eco",   "quantita": 2, "prezzo_unitario": 12.90},
    {"id_vendita": 2, "data_vendita": date(2025, 1, 3).strftime("%Y-%m-%d"), "titolo": "1984",                  "autore": "George Orwell", "quantita": 1, "prezzo_unitario": 10.50},
    {"id_vendita": 3, "data_vendita": date(2025, 1, 3).strftime("%Y-%m-%d"), "titolo": "Il barone rampante",    "autore": "Italo Calvino", "quantita": 3, "prezzo_unitario": 11.20},
    {"id_vendita": 4, "data_vendita": date(2025, 1, 5).strftime("%Y-%m-%d"), "titolo": "Il Nome della Rosa",    "autore": "Umberto Eco",   "quantita": 1, "prezzo_unitario": 12.90}
]

df = pd.DataFrame(vendite_data)

df.to_sql("vendite", conn, if_exists="replace", index=False)

query = """
    SELECT autore,
           SUM(quantita)                          AS copie_totali,
           ROUND(SUM(quantita * prezzo_unitario), 2) AS ricavo_totale
    FROM vendite
    GROUP BY autore
    ORDER BY ricavo_totale DESC;
"""

risultato = pd.read_sql(query, conn)
print(risultato)

top_3_autori_query = """
    SELECT autore,
              SUM(quantita) AS copie_totali
    FROM vendite
    GROUP BY autore
    ORDER BY copie_totali DESC
    LIMIT 3;
"""

top_3_autori = pd.read_sql(top_3_autori_query, conn)
print(top_3_autori)

ricavo_mensile_query = """
    SELECT strftime('%Y-%m', data_vendita) AS mese,
           ROUND(SUM(quantita * prezzo_unitario), 2) AS ricavo_totale
    FROM vendite
    GROUP BY mese
    ORDER BY mese;

"""

ricavo_mensile = pd.read_sql(ricavo_mensile_query, conn)
print(ricavo_mensile)

conn.close()