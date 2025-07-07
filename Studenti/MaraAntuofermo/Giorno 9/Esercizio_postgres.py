import pandas as pd 
from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase")

from datetime import date 

vendite_data = [{"id_vendita": 1, "data_vendita": date(2025, 1, 2), "titolo": "Il Nome della Rosa",    "autore": "Umberto Eco",   "quantita": 2, "prezzo_unitario": 12.90},
    {"id_vendita": 2, "data_vendita": date(2025, 1, 3), "titolo": "1984",                  "autore": "George Orwell", "quantita": 1, "prezzo_unitario": 10.50},
    {"id_vendita": 3, "data_vendita": date(2025, 1, 3), "titolo": "Il barone rampante",    "autore": "Italo Calvino", "quantita": 3, "prezzo_unitario": 11.20},
    {"id_vendita": 4, "data_vendita": date(2025, 1, 5), "titolo": "Il Nome della Rosa",    "autore": "Umberto Eco",   "quantita": 1, "prezzo_unitario": 12.90},
    {"id_vendita": 4, "data_vendita": date(2024, 3, 7), "titolo": "Piccole donne",    "autore": "Louisa May Alcott",   "quantita": 1, "prezzo_unitario": 14.90}]

df = pd.DataFrame(vendite_data)

df.to_sql("vendite", engine, if_exists="replace", index=False)

query = text(""" 
    SELECT autore,
           SUM(quantita)                          AS copie_totali,
           ROUND(SUM(quantita * prezzo_unitario)::numeric, 2) AS ricavo_totale
    FROM vendite
    GROUP BY autore
    ORDER BY ricavo_totale DESC;""")

risultato = pd.read_sql(query, engine)
print(risultato)

#4 Compiti da svolgere

top_3_autori_query = text(""" 
    SELECT autore, 
    SUM(quantita) AS copie_totali 
    FROM vendite
    GROUP BY autore 
    ORDER BY copie_totali DESC LIMIT 3;""")

top_3_autori = pd.read_sql(top_3_autori_query, engine)
print(top_3_autori)

r_mensile_query = text(""" 
    SELECT DATE_TRUNC('month', data_vendita)::date AS mese, 
    ROUND(SUM(quantita * prezzo_unitario)::numeric, 2) AS ricavo_totale 
    FROM vendite 
    GROUP BY mese 
    ORDER BY mese;""")

ricavo_mensile = pd.read_sql(r_mensile_query , engine)
print(ricavo_mensile)

