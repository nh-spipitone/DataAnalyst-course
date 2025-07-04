import pandas as pd
from sqlalchemy import create_engine

# Creazione connessione al database
engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5433/mydatabase"
)

# Creazione tabella da DataFrame
df = pd.DataFrame(
    {
        "id": range(1, 6),
        "nome": ["Anna", "Marco", "Lucia", "Paolo", "Giulia"],
        "importo": [1200.50, 950.75, 2300.00, 1450.25, 3100.80],
    }
)
# Inserimento dati nel database
df.to_sql("transazioni", engine, if_exists="replace", index=False)
# Lettura dati con query SQL
query = "SELECT nome, importo FROM transazioni WHERE importo > 1500"
risultato = pd.read_sql(query, engine)
print(risultato)
