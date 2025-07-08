import pandas as pd                # Importa la libreria pandas per la manipolazione dei dati
import sqlite3                     # Importa la libreria sqlite3 per lavorare con database SQLite

conn = sqlite3.connect("esercizio_ordini_completo.db")  # Crea una connessione al database SQLite

# Crea un DataFrame pandas con i dati degli ordini
ordini_df = pd.DataFrame({
    'id': list(range(1, 11)),     # Colonna 'id' da 1 a 10
    'cliente': ['Anna', 'Luca', 'Anna', 'Marco', 'Luca', 'Sara', 'Anna', 'Luca', 'Marco', 'Sara'],  # Nomi clienti
    'prodotto': ['Penna', 'Notebook', 'Quaderno', 'Zaino', 'Penna', 'Quaderno', 'Penna', 'Matita', 'Zaino', 'Penna'],  # Prodotti ordinati
    'quantità': [3, 1, 5, 2, 10, 2, 6, 4, 1, 8],      # Quantità ordinate
    'prezzo_unitario': [1.0, 3.5, 2.0, 20.0, 1.0, 2.0, 1.0, 0.8, 18.0, 1.0]  # Prezzo unitario dei prodotti
})

ordini_df.to_sql('ordini', conn, if_exists='replace', index=False)  # Salva il DataFrame come tabella 'ordini' nel database

# Esegue una query SQL per calcolare la spesa totale per cliente (solo chi spende più di 10 euro)
df_spese = pd.read_sql_query("""
SELECT cliente,
       SUM(quantità * prezzo_unitario) AS totale_spesa -- totale_spesa= quantita * prezzo
FROM ordini
GROUP BY cliente
HAVING totale_spesa > 10 -- WHERE totale_spesa > 10
""", conn)

print(" Clienti con spesa totale > 10 euro:")  # Stampa intestazione
print(df_spese)                                # Stampa il risultato della query

# Aggiorna il prezzo_unitario a 1.2 per le 'Penna' con quantità > 5
conn.execute("""
UPDATE ordini
SET prezzo_unitario = 1.2
WHERE prodotto = 'Penna' AND quantità > 5
""")
conn.commit()  # Applica la modifica al database

# Elimina gli ordini con valore totale (quantità * prezzo_unitario) inferiore a 5
conn.execute("""
DELETE FROM ordini
WHERE (quantità * prezzo_unitario) < 5
""")
conn.commit()  # Applica la modifica al database

# Legge la tabella 'ordini' aggiornata dal database
df_finale = pd.read_sql_query("SELECT * FROM ordini", conn)
print("\n Tabella 'ordini' dopo UPDATE e DELETE:")  # Stampa intestazione
print(df_finale)                                    # Stampa la tabella aggiornata

conn.close()  # Chiude la connessione al database