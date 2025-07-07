import pandas as pd
from datetime import date
from sqlalchemy import create_engine, text

# Dati d’esempio (potete modificarli o ampliarli)
vendite_data = [
    {"id_vendita": 1, "data_vendita": date(2025, 1, 2), "titolo": "Il Nome della Rosa",    "autore": "Umberto Eco",   "quantita": 2, "prezzo_unitario": 12.90},
    {"id_vendita": 2, "data_vendita": date(2025, 1, 3), "titolo": "1984",                  "autore": "George Orwell", "quantita": 1, "prezzo_unitario": 10.50},
    {"id_vendita": 3, "data_vendita": date(2025, 1, 3), "titolo": "Il barone rampante",    "autore": "Italo Calvino", "quantita": 3, "prezzo_unitario": 11.20},
    {"id_vendita": 4, "data_vendita": date(2025, 1, 5), "titolo": "Il Nome della Rosa",    "autore": "Umberto Eco",   "quantita": 1, "prezzo_unitario": 12.90},
]

df = pd.DataFrame(vendite_data)

# Connessione a PostgreSQL e salvataggio
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase",
    echo = False   # True per loggare l’SQL generato
)

# Scrive (o sovrascrive) la tabella "vendite"
df.to_sql("vendite", engine, if_exists = "replace", index = False)

# Query di esempio
query = text("""
    SELECT 
             autore,
             SUM(quantita)                             AS copie_totali,
             ROUND(SUM(quantita * prezzo_unitario)::numeric, 2) AS ricavo_totale
    FROM     vendite
    GROUP BY autore
    ORDER BY ricavo_totale DESC;
""")

risultato = pd.read_sql(query, engine)
print(risultato)

# Top 3 autori per numero di copie vendute
top_3_autori_query = text("""
    SELECT 
             autore,
             SUM(quantita) AS copie_totali
    FROM     vendite
    GROUP BY autore
    ORDER BY copie_totali DESC
    LIMIT    3;
""")

risultato_top_3_autori = pd.read_sql(top_3_autori_query, engine)
print(risultato_top_3_autori)

# Ricavo totale per mese
ricavo_mensile_query = text("""
    SELECT 
             DATE_TRUNC('month', data_vendita)::date AS mese,
             ROUND(SUM(quantita * prezzo_unitario)::numeric, 2) AS ricavo_totale
    FROM     vendite
    GROUP BY mese
    ORDER BY mese;
""")

risultato_ricavo_mensile = pd.read_sql(ricavo_mensile_query, engine)
print(risultato_ricavo_mensile)
