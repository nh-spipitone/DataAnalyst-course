import pandas as pd                # Importa la libreria pandas per la manipolazione dei dati
import sqlite3                     # Importa la libreria sqlite3 per lavorare con database SQLite

# Crea un motore di connessione al database SQLite
conn = sqlite3.connect("my_database.db")  # Crea una connessione a un database SQLite chiamato 'my_database.db'

corsi_df = pd.DataFrame({          # Crea un DataFrame pandas con i dati dei corsi
    'id': [101, 102, 103],         # Colonna 'id' con gli identificativi dei corsi
    'nome_corso': ['Matematica', 'Fisica', 'Informatica'],  # Colonna 'nome_corso' con i nomi dei corsi
    'crediti': [6, 8, 9]           # Colonna 'crediti' con i crediti dei corsi
})

corsi_df.to_sql('corsi', conn, if_exists='replace', index=False)  # Salva il DataFrame come tabella 'corsi' nel database, sovrascrivendo se già esiste

conn.execute("INSERT INTO corsi (id, nome_corso, crediti) VALUES (104, 'Chimica', 7)")  # Inserisce un nuovo corso nella tabella 'corsi'
conn.commit()                        # Salva (committa) le modifiche fatte al database

df_filtrati = pd.read_sql_query("SELECT * FROM corsi WHERE crediti > 7", conn)  # Esegue una query per selezionare i corsi con più di 7 crediti

print("Corsi con più di 7 crediti:") # Stampa una descrizione dei dati filtrati
print(df_filtrati)                   # Stampa il DataFrame risultante dalla query

conn.close()                         # Chiude la connessione al database