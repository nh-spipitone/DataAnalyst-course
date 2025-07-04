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
    # ---------- INSERT -------------------------------------
    conn.execute(
        text(
            "INSERT INTO schiavi (nome, eta, sesso, nazionalita, data_nascita, lavoro, salario) "
            "VALUES (:nome, :eta, :sesso, :nazionalita, :data_nascita, :lavoro, :salario)"
        ),
        [
            {
                "nome": "Mario",
                "eta": 34,
                "sesso": "M",
                "nazionalita": "Italiana",
                "data_nascita": "1990-05-12",
                "lavoro": "Fabbro",
                "salario": 1200.00,
            },
            {
                "nome": "Sara",
                "eta": 28,
                "sesso": "F",
                "nazionalita": "Spagnola",
                "data_nascita": "1995-03-22",
                "lavoro": "Cuoca",
                "salario": 1100.50,
            },
            {
                "nome": "Ahmed",
                "eta": 40,
                "sesso": "M",
                "nazionalita": "Egiziana",
                "data_nascita": "1983-11-10",
                "lavoro": "Muratore",
                "salario": 1300.75,
            },
            {
                "nome": "Elena",
                "eta": 31,
                "sesso": "F",
                "nazionalita": "Greca",
                "data_nascita": "1992-07-18",
                "lavoro": "Sarta",
                "salario": 1050.00,
            },
        ],
    )

tabella = pd.read_sql("SELECT * FROM schiavi", engine)
print(tabella)  # Stampa il contenuto della tabella dopo l'inserimento
