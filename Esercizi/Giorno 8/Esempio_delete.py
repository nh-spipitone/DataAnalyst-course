import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5433/mydatabase"
)


with engine.begin() as conn:
    conn.execute(
        text(
            """
        DELETE FROM schiavi
        WHERE nome = 'Ahmed'
        """
        )
    )

variabile = pd.read_sql("SELECT * FROM schiavi", engine)
print(variabile)  # Stampa il contenuto della tabella dopo l'elimin
