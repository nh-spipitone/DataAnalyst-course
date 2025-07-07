import pandas as pd
from sqlalchemy import create_engine, text

# Creazione connessione al database
engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase"
)

with engine.begin() as conn:
    conn.execute(
        text("""CREATE TABLE IF NOT EXISTS schiavi (
                id           SERIAL PRIMARY KEY,
                studente VARCHAR(50),
                materia VARCHAR(50),
                voto INTEGER);"""))

tabella = pd.read_sql("SELECT * FROM studenti;", con=engine)
print(tabella)
