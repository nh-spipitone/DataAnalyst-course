import pandas as pd
from sqlalchemy import create_engine, text

# Crea un motore di connessione al database PostgreSQL
engine = create_engine("postgresql+psycopg2://myuser:mypassword@localhost:5433/mydatabase")

with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO transazioni (nome, importo) VALUES (:nome, :importo)"),
        [
            {"nome": "Anna", "importo": 1200.50},
            {"nome": "Marco", "importo": 950.75},
            {"nome": "Lucia", "importo": 2300.00},
            {"nome": "Paolo", "importo": 1450.25},
            {"nome": "Giulia", "importo": 3100.80},
        ]
    )