import pandas as pd
from sqlalchemy import create_engine, text

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

# DDL – Data Definition Language
# Create, Alter, Drop, Truncate, Rename

# Create Crea una  nuova tabella o database
# Alter Modifica una tabella esistente (aggiunge, modifica o elimina colonne)
# Drop Elimina una tabella o database
# Truncate Elimina tutti i dati da una tabella senza eliminarla
# Rename Rinomina una tabella o database

# DML – Data Manipulation Language
# Insert Update Delete
# Insert Inserisce nuovi dati in una tabella
# Update Aggiorna dati esistenti in una tabella
# Delete Elimina dati da una tabella


# DQL – Data Query Language
# Select
# Select Recupera dati da una o più tabelle


# ===========================================================
# DDL – Creo e poi modifico la tabella -----------------------
# ===========================================================
with engine.begin() as conn:  # apertura connessione + commit automatico
    # ---------- CREATE -------------------------------------
    conn.execute(
        text(
            """
        CREATE TABLE IF NOT EXISTS transazioni (           -- creo tabella se non esiste
            id      SERIAL PRIMARY KEY,                    -- chiave primaria autoincrementante
            nome    VARCHAR(50),                           -- nome della persona
            importo NUMERIC(10,2)                          -- importo (max 99999999.99)
        );
    """
        )
    )

    # ---------- ALTER --------------------------------------
    conn.execute(
        text(
            """
        ALTER TABLE transazioni
        ADD COLUMN IF NOT EXISTS data DATE                 -- aggiungo colonna data
        DEFAULT CURRENT_DATE;                              -- valore di default: data odierna
    """
        )
    )


query = "SELECT * FROM transazioni"  # Query per leggere i dati dalla tabella
tabella = pd.read_sql(
    query, engine
)  # Legge i dati dalla tabella e li carica in un DataFrame
print(tabella)  # Stampa il contenuto della tabella

# with engine.begin() as conn:
#     # ---------- INSERT -------------------------------------
#     conn.execute(
#         text("INSERT INTO transazioni (nome, importo) VALUES (:nome, :imp)"),
#         [  # passo più righe in una sola volta
#             {"nome": "Anna", "imp": 1200.50},
#             {"nome": "Marco", "imp": 950.75},
#             {"nome": "Lucia", "imp": 2300.00},
#             {"nome": "Paolo", "imp": 1450.25},
#             {"nome": "Giulia", "imp": 3100.80},
#             {"nome": "Luca", "imp": 1800.00},  # riga extra per l’esempio update
#         ],
#     )

# print("###########\n")
# tabella = pd.read_sql(query, engine)
# print(tabella)  # Stampa il contenuto della tabella dopo l'inserimento


# # Inserimento dati nel database
# # df.to_sql("transazioni", engine, if_exists="replace", index=False)
# # Lettura dati con query SQL
# query = "SELECT nome, importo FROM transazioni WHERE importo > 1500"
# risultato = pd.read_sql(query, engine)
# print(risultato)


with engine.begin() as conn:
    # ---------- UPDATE -------------------------------------
    conn.execute(
        text(
            """
        UPDATE transazioni
        SET importo = importo * 1.10                       -- aumento del 10 %
        WHERE nome = 'Luca';
    """
        )
    )

query = "SELECT nome, importo FROM transazioni WHERE importo > 1500"
risultato = pd.read_sql(query, engine)
print(risultato)

with engine.begin() as conn:
    conn.execute(
        text(
            """
        DELETE FROM transazioni
        WHERE importo < 1000;                              -- rimuovo record sotto i 1 000 €
    """
        )
    )
query = "SELECT * FROM transazioni"
tabella = pd.read_sql(query, engine)
print(tabella)  # Stampa il contenuto della tabella dopo l'aggiorn
