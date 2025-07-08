import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5433/mydatabase"
)

voti_df = pd.DataFrame(
    {
        "id": [1, 2, 3, 4, 5, 6],
        "studente": ["Marco", "Anna", "Luca", "Anna", "Luca", "Marco"],
        "materia": [
            "Matematica",
            "Italiano",
            "Storia",
            "Matematica",
            "Fisica",
            "Storia",
        ],
        "voto": [7, 9, 5, 6, 4, 5],
    }
)
with engine.begin() as conn:
    voti_df.to_sql("voti", conn, if_exists="replace", index=False)


tabella = pd.read_sql(text("SELECT * FROM voti;"), con=engine)
print(tabella)

with engine.begin() as conn:
    conn.execute(
        text(
            """
        UPDATE voti SET voto= 8
        where studente = 'Marco' and materia = 'Storia';

    """
        )
    )

tabella = pd.read_sql(text("SELECT * FROM voti;"), con=engine)
print(tabella)

with engine.begin() as conn:
    conn.execute(
        text(
            """
        ALTER TABLE voti ADD COLUMN data_nascita DATE;
    """
        )
    )

# aggiungi data di nascita ad ogni studente
with engine.begin() as conn:
    conn.execute(
        text(
            """
        UPDATE voti SET data_nascita = '2000-01-01'
        where studente = 'Marco';

        UPDATE voti SET data_nascita = '2001-02-02'
        where studente = 'Anna';

        UPDATE voti SET data_nascita = '2002-03-03'
        where studente = 'Luca';
    """
        )
    )

tabella = pd.read_sql(text("SELECT * FROM voti;"), con=engine)
print(tabella)
