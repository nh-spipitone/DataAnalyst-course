import pandas as pd
from sqlalchemy import create_engine, text

# Creazione connessione al database
engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase"
)


with engine.begin() as conn:  # apertura connessione + commit automatico
    conn.execute(
        text(
            """
        CREATE TABLE IF NOT EXISTS schiavi (           -- creo tabella se non esiste
            id      SERIAL PRIMARY KEY,                    -- chiave primaria autoincrementante
            nome    VARCHAR(50),                           -- nome della persona
            eta     INTEGER,                             -- età della persona (max 999)
            sesso   VARCHAR(10),                          -- sesso della persona (max 10 caratteri)
            nazionalita VARCHAR(50),                       -- nazionalità della persona (max 50 caratteri)
            data_nascita DATE,                            -- data di nascita della persona
            lavoro   VARCHAR(50),                          -- lavoro della persona (max 50 caratteri)
            salario  NUMERIC(10,2)                         -- salario della persona (max 999)
        );
    """
        )
    )

query = "SELECT * FROM schiavi"
tabella = pd.read_sql(query, engine)
print(tabella)  # Stampa il contenuto della tabella
