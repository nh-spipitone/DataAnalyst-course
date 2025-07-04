import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5433/mydatabase"
)

# id      SERIAL PRIMARY KEY,                    -- chiave primaria autoincrementante
#             nome    VARCHAR(50),                           -- nome della persona
#             eta     INTEGER,                             -- età della persona (max 999)
#             sesso   VARCHAR(10),                          -- sesso della persona (max 10 caratteri)
#             nazionalita VARCHAR(50),                       -- nazionalità della persona (max 50 caratteri)
#             data_nascita DATE,                            -- data di nascita della persona
#             lavoro   VARCHAR(50),                          -- lavoro della persona (max 50 caratteri)
#             salario  NUMERIC(10,2)                         -- salario della persona (max 999)


with engine.begin() as conn:
    # ---------- UPDATE -------------------------------------
    conn.execute(
        text(
            """
        UPDATE schiavi
        SET salario = salario *0.8
        where salario >1100
    """
        )
    )

variabile = pd.read_sql("SELECT * FROM schiavi", engine)
print(variabile)  # Stampa il contenuto della tabella dopo l'aggiornamento
