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
            DELETE FROM schiavi
            WHERE nome = 'Giulia';
        """
        )
    )

query = "SELECT * FROM schiavi"
tabella = pd.read_sql(query, engine)
print(tabella)