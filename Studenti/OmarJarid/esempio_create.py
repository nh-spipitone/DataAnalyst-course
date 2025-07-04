import pandas as pd
from sqlalchemy import create_engine, text

# Creazione connessione al database
engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase"
)

with engine.begin() as conn:
    conn.execute(
        text(
            """
            CREATE TABLE IF NOT EXISTS schiavi (
                id           SERIAL PRIMARY KEY,
                nome         VARCHAR(50),
                eta          INTEGER,
                sesso        VARCHAR(10),
                nazionalita  VARCHAR(50),
                data_nascita DATE,
                lavoro       VARCHAR(50),
                salario      NUMERIC(10, 2)
            );
            """
        )
    )

query = "SELECT * FROM schiavi"
tabella = pd.read_sql(query, engine)
print(tabella)