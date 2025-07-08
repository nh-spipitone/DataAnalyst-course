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
            INSERT INTO schiavi (nome, eta, sesso, nazionalita, data_nascita, lavoro, salario) 
            VALUES(:nome, :eta, :sesso, :nazionalita, :data_nascita, :lavoro, :salario)
            """
        ), 
        [
            {
                "nome": "Marco",
                "eta": 25,
                "sesso": "maschio",
                "nazionalita": "italiano",
                "data_nascita": "2000-01-01",
                "lavoro": "programmatore",
                "salario": 5000.00
            },
            {
                "nome": "Luca",
                "eta": 30,
                "sesso": "maschio",
                "nazionalita": "italiano",
                "data_nascita": "1995-05-10",
                "lavoro": "programmatore",
                "salario": 6000.00
            },
            {
                "nome": "Giulia",
                "eta": 28,
                "sesso": "femmina",
                "nazionalita": "italiano",
                "data_nascita": "1998-09-15",
                "lavoro": "programmatore",
                "salario": 5500.00
            },
            {
                "nome": "Paolo",
                "eta": 32,
                "sesso": "maschio",
                "nazionalita": "italiano",
                "data_nascita": "1992-03-20",
                "lavoro": "programmatore",
                "salario": 5800.00
            },
            {
                "nome": "Giorgia",
                "eta": 27,
                "sesso": "femmina",
                "nazionalita": "italiano",
                "data_nascita": "1999-07-25",
                "lavoro": "programmatore",
                "salario": 5200.00
            },
            {
                "nome": "Mikko",
                "eta": 31,
                "sesso": "maschio",
                "nazionalita": "finlandese",
                "data_nascita": "1994-11-30",
                "lavoro": "programmatore",
                "salario": 5900.00
            }
        ]
    )

query = "SELECT * FROM schiavi"
tabella = pd.read_sql(query, engine)
print(tabella)