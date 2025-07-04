import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase"
)

with engine.begin() as conn:  # apertura connessione + commit automatico
    # ---------- CREATE -------------------------------------
    conn.execute(
        text(
            """
        CREATE TABLE IF NOT EXISTS transazioni (           -- creo tabella se non esiste
            id      SERIAL PRIMARY KEY,                    -- chiave primaria autoincrementante
            nome    VARCHAR(50),                           -- nome della persona (max)
            età NUMERIC(10,2)                          -- età della persona (max)
            sesso VARCHAR(10)                           -- sesso della persona (max 10 caratteri)
            nazionalita VARCHAR(50)                      -- nazionalità della persona (max 50 caratteri)
        );
    """
        )
    )

    