import pandas as pd
from sqlalchemy import create_engine, text

# Crea un motore di connessione al database PostgreSQL
engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5433/mydatabase"
)

# Legge l'intera tabella "schiavi" dal database e la carica in un DataFrame pandas
tabella = pd.read_sql("SELECT * FROM schiavi", engine)
print(tabella)  # Stampa il contenuto della tabella dopo l'inserimento

print("########\n")

# Seleziona tutti i record dalla tabella "schiavi" e li ordina in base al campo "salario" (in ordine crescente)
schiavi_in_ordine_salario = pd.read_sql(
    "SELECT * FROM schiavi ORDER BY salario", engine
)
print(schiavi_in_ordine_salario)  # Stampa la tabella ordinata per salario

# Seleziona solo il campo "nome" dalla tabella "schiavi" dove la nazionalità è "Italiana"
nomi_schiavi_italiani = pd.read_sql(
    "SELECT nome FROM schiavi WHERE nazionalita = 'Italiana'", engine
)
print(nomi_schiavi_italiani)  # Stampa i nomi degli schiavi italiani

# Calcola la somma totale dei salari per ogni nazionalità presente nella tabella "schiavi"
totale_salario_per_nazionalita = pd.read_sql(
    "SELECT nazionalita, SUM(salario) AS totale_salario FROM schiavi GROUP BY nazionalita",
    engine,
)
print(totale_salario_per_nazionalita)  # Stampa il totale del salario per nazionalità


pd.read_sql(
    "SELECT nazionalita, SUM(salario) AS totale_salario FROM schiavi GROUP BY nazionalita",
    engine,
).to_csv("totale_salario_per_nazionalita.csv", index=False)
