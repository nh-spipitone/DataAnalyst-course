'''
Esercizio 4 – Creazione nuova tabella
🔧 Obiettivo:
Crea un DataFrame chiamato corsi con colonne:

id

nome_corso

crediti

E salvalo nel database come tabella corsi.
Aggiungi un nuovo corso alla tabella corsi:

id: 104

nome: "Chimica"

crediti: 7
Seleziona tutti i corsi che hanno più di 7 crediti.
'''


from sqlalchemy import create_engine, text
import pandas as pd

# Connessione (aggiorna con i tuoi dati reali)
engine = create_engine("postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase")

# Crea DataFrame
dati_corsi = {
    'id': [101, 102, 103],
    'nome_corso': ['Matematica', 'Fisica', 'Biologia'],
    'crediti': [8, 6, 9]
}
df = pd.DataFrame(dati_corsi)

# Scrive la tabella nel database
df.to_sql('corsi', engine, index=False, if_exists='replace')

# Inserisce un nuovo corso
with engine.connect() as conn:
    conn.execute(text("""
        INSERT INTO corsi (id, nome_corso, crediti)
        VALUES (104, 'Chimica', 7)
    """))
    conn.commit()

# Legge i corsi con più di 7 crediti
query = "SELECT * FROM corsi WHERE crediti > 7"
risultato = pd.read_sql_query(query, engine)
print(risultato)

