import pandas as pd                 # Importa la libreria pandas per la manipolazione dei dati
import sqlite3                      # Importa la libreria sqlite3 per lavorare con database SQLite

conn = sqlite3.connect("esercizio_dipendenti.db")  # Crea una connessione al database SQLite (o lo crea se non esiste)

dipendenti_df = pd.DataFrame({      # Crea un DataFrame pandas con i dati dei dipendenti
    'id': [1, 2, 3, 4],
    'nome': ['Giulia', 'Marco', 'Elena', 'Luca'],
    'dipartimento': ['HR', 'IT', 'Marketing', 'IT'],
    'stipendio': [900, 2200, 2000, 2100]
})

dipendenti_df.to_sql('dipendenti', conn, if_exists='replace', index=False)  # Salva il DataFrame come tabella 'dipendenti' nel database, sovrascrivendo se esiste

conn.execute("UPDATE dipendenti SET stipendio = 2300 WHERE nome = 'Elena'") # Aggiorna lo stipendio di Elena a 2300 euro
conn.commit()                         # Salva le modifiche nel database

conn.execute("DELETE FROM dipendenti WHERE dipartimento = 'IT' AND stipendio > 2100") # Elimina i dipendenti dell'IT con stipendio superiore a 2100
conn.commit()                         # Salva le modifiche nel database

df_bassi = pd.read_sql_query("SELECT nome FROM dipendenti WHERE stipendio < 1000", conn) # Seleziona i nomi dei dipendenti con stipendio inferiore a 1000 euro

print("Dipendenti con stipendio inferiore a 1000 euro:") # Stampa una descrizione
print(df_bassi)                    # Stampa il DataFrame risultante

conn.close()                       # Chiude la connessione al database