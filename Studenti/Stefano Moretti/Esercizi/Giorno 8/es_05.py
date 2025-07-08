import pandas as pd
import sqlite3

conn = sqlite3.connect("esercizio_voti_completo.db")

voti_df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'studente': ['Marco', 'Anna', 'Luca', 'Anna', 'Luca', 'Marco'],
    'materia': ['Matematica', 'Italiano', 'Storia', 'Matematica', 'Fisica', 'Storia'],
    'voto': [7, 9, 5, 6, 4, 5]
})
voti_df.to_sql('voti', conn, if_exists='replace', index=False)

media_df = pd.read_sql_query("""
SELECT studente, AVG(voto) AS media_voti
FROM voti
GROUP BY studente
HAVING media_voti >= 6
""", conn)
print("Studenti con media voti >= 6:")
print(media_df)

conn.execute("""
UPDATE voti
SET voto = 8
WHERE studente = 'Marco' AND materia = 'Storia'
""")
conn.commit()

conn.execute("ALTER TABLE voti ADD COLUMN data_nascita TEXT")

conn.execute("UPDATE voti SET data_nascita = '2005-03-10' WHERE studente = 'Marco'")
conn.execute("UPDATE voti SET data_nascita = '2004-05-15' WHERE studente = 'Anna'")
conn.execute("UPDATE voti SET data_nascita = '2005-11-20' WHERE studente = 'Luca'")
conn.commit()

df_studenti_2005 = pd.read_sql_query("""
SELECT studente, AVG(voto) AS media_voti, data_nascita
FROM voti
WHERE strftime('%Y', data_nascita) = '2005'
GROUP BY studente
HAVING media_voti > 4
""", conn)

print("\nStudenti nati nel 2005 con media voti > 4:")
print(df_studenti_2005)

conn.close()