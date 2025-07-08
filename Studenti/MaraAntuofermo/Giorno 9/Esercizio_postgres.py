# Importiamo Pandas per la manipolazione dei dati tabellari
import pandas as pd 

# Importiamo SQLAlchemy per la connessione e interazione con il database SQL
from sqlalchemy import create_engine, text

# Creiamo l'engine per connetterci al database PostgreSQL
engine = create_engine("postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase")

# Importiamo la classe date per gestire le date di vendita
from datetime import date 

# Creiamo una lista di dizionari, ognuno rappresenta una vendita
vendite_data = [
    {"id_vendita": 1, "data_vendita": date(2025, 1, 2), "titolo": "Il Nome della Rosa",    "autore": "Umberto Eco",        "quantita": 2, "prezzo_unitario": 12.90},
    {"id_vendita": 2, "data_vendita": date(2025, 1, 3), "titolo": "1984",                  "autore": "George Orwell",     "quantita": 1, "prezzo_unitario": 10.50},
    {"id_vendita": 3, "data_vendita": date(2025, 1, 3), "titolo": "Il barone rampante",    "autore": "Italo Calvino",     "quantita": 3, "prezzo_unitario": 11.20},
    {"id_vendita": 4, "data_vendita": date(2025, 1, 5), "titolo": "Il Nome della Rosa",    "autore": "Umberto Eco",        "quantita": 1, "prezzo_unitario": 12.90},
    {"id_vendita": 4, "data_vendita": date(2024, 3, 7), "titolo": "Piccole donne",         "autore": "Louisa May Alcott", "quantita": 1, "prezzo_unitario": 14.90}
]

# Convertiamo la lista di dizionari in un DataFrame Pandas
df = pd.DataFrame(vendite_data)

# Scriviamo il DataFrame nel database come tabella "vendite"
# if_exists="replace" sovrascrive la tabella se esiste già
df.to_sql("vendite", engine, if_exists="replace", index=False)

# Query SQL per ottenere ricavi e copie totali per autore
query = text(""" 
    SELECT autore,
           SUM(quantita) AS copie_totali,
           ROUND(SUM(quantita * prezzo_unitario)::numeric, 2) AS ricavo_totale
    FROM vendite
    GROUP BY autore
    ORDER BY ricavo_totale DESC;
""")

# Eseguiamo la query e carichiamo il risultato in un DataFrame
risultato = pd.read_sql(query, engine)

# Stampiamo il risultato della prima query
print(risultato)

# -------- COMPITO 1: Top 3 autori per numero di copie vendute --------

# Query SQL per ottenere i 3 autori che hanno venduto più copie
top_3_autori_query = text(""" 
    SELECT autore, 
           SUM(quantita) AS copie_totali 
    FROM vendite
    GROUP BY autore 
    ORDER BY copie_totali DESC 
    LIMIT 3;
""")

# Eseguiamo la query e carichiamo il risultato in un DataFrame
top_3_autori = pd.read_sql(top_3_autori_query, engine)

# Stampiamo il risultato della seconda query
print(top_3_autori)

# -------- COMPITO 2: Ricavo totale per mese --------

# Query SQL per calcolare il ricavo mensile (tronchiamo la data al mese)
r_mensile_query = text(""" 
    SELECT DATE_TRUNC('month', data_vendita)::date AS mese, 
           ROUND(SUM(quantita * prezzo_unitario)::numeric, 2) AS ricavo_totale 
    FROM vendite 
    GROUP BY mese 
    ORDER BY mese;
""")

# Eseguiamo la query e carichiamo il risultato in un DataFrame
ricavo_mensile = pd.read_sql(r_mensile_query , engine)

# Stampiamo il risultato della terza query
print(ricavo_mensile)
