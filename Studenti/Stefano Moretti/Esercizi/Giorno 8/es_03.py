import pandas as pd                 # Importa la libreria pandas per la manipolazione dei dati
import sqlite3                      # Importa la libreria sqlite3 per lavorare con database SQLite

conn = sqlite3.connect("esercizio_prodotti_completo.db")

prodotti_df = pd.DataFrame({
    'id': list(range(1, 11)),
    'nome': [
        'Penna', 'Quaderno', 'Zaino', 'Matita', 'Borraccia',
        'Notebook', 'Evidenziatore', 'Calcolatrice', 'Agenda', 'Righello'
    ],
    'prezzo': [1.0, 2.5, 30.0, 0.8, 15.0, 3.0, 1.5, 25.0, 8.0, 1.2],
    'categoria': [
        'Cartoleria', 'Cartoleria', 'Accessori', 'Cartoleria', 'Accessori',
        'Tecnologia', 'Cartoleria', 'Tecnologia', 'Cartoleria', 'Cartoleria'
    ]
})

prodotti_df.to_sql('prodotti', conn, if_exists='replace', index=False)  # Salva il DataFrame come tabella 'prodotti' nel database, sovrascrivendo se esiste

conn.execute("""
UPDATE prodotti
SET prezzo = 18.0
WHERE nome = 'Borraccia'
""")
conn.commit()

conn.execute("""
DELETE FROM prodotti
WHERE prezzo < 2.0
""")
conn.commit()

df_risultato = pd.read_sql_query("""
SELECT * FROM prodotti
WHERE prezzo > 10 AND categoria = 'Accessori'
""", conn)

print(" Prodotti con prezzo > 10 e categoria 'Accessori':")
print(df_risultato)

conn.close()  # Chiude la connessione al database