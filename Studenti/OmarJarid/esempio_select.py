import pandas as pd
from sqlalchemy import create_engine, text

# Creazione connessione al database
engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase"
)

query = "SELECT * FROM schiavi"
tabella = pd.read_sql(query, engine)
print(tabella)
print("***********************************************\n")

query = "SELECT * FROM schiavi ORDER BY salario"
tabella = pd.read_sql(query, engine)
print(tabella)
print("***********************************************\n")

query = "SELECT nome FROM schiavi WHERE nazionalita = 'italiano'"
tabella = pd.read_sql(query, engine)
print(tabella)
print("***********************************************\n")

query = "SELECT nazionalita, SUM(salario) AS totale_salario FROM schiavi GROUP BY nazionalita"
tabella = pd.read_sql(query, engine)
print(tabella)
print("***********************************************\n")

