import pandas as pd
from sqlalchemy import create_engine, text

# Connessione al DB (modifica con i tuoi dati)
engine = create_engine("postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase")

# 1. Crea DataFrame con voti e studenti
df_voti = pd.DataFrame([
    {'id': 1, 'studente': 'Luca', 'materia': 'Matematica', 'voto': 7},
    {'id': 2, 'studente': 'Luca', 'materia': 'Fisica', 'voto': 5},
    {'id': 3, 'studente': 'Anna', 'materia': 'Matematica', 'voto': 8},
    {'id': 4, 'studente': 'Anna', 'materia': 'Fisica', 'voto': 7},
    {'id': 5, 'studente': 'Marco', 'materia': 'Matematica', 'voto': 4},
    {'id': 6, 'studente': 'Marco', 'materia': 'Fisica', 'voto': 5},
    {'id': 7, 'studente': 'Sara', 'materia': 'Matematica', 'voto': 9},
    {'id': 8, 'studente': 'Sara', 'materia': 'Fisica', 'voto': 10},
])

# 2. Scrivi la tabella voti nel DB
df_voti.to_sql('voti', engine, index=False, if_exists='replace')

# 3. Calcola la media voti per studente (SQL)
query_media = """
    SELECT studente, AVG(voto) AS media_voto
    FROM voti
    GROUP BY studente
    HAVING AVG(voto) >= 6
"""
media_voti = pd.read_sql_query(query_media, engine)
print("Studenti con media voto >= 6:")
print(media_voti)

# 4. Cambia il voto di una materia per uno studente (es. Marco in Fisica da 5 a 6)
with engine.connect() as conn:
    conn.execute(text("""
        UPDATE voti
        SET voto = 6
        WHERE studente = 'Marco' AND materia = 'Fisica'
    """))
    conn.commit()

# 5. Aggiungi colonna 'data_di_nascita' e aggiorna i dati per ogni studente
with engine.connect() as conn:
    # Aggiungi colonna se non esiste (attenzione: esegui solo 1 volta!)
    try:
        conn.execute(text("ALTER TABLE voti ADD COLUMN data_di_nascita DATE"))
    except Exception as e:
        # Se errore perché colonna già esiste, passa
        pass

    # Aggiorna le date di nascita per ogni studente (prendi solo 1 data per studente, es. id=1)
    conn.execute(text("""
        UPDATE voti SET data_di_nascita = '2005-03-15' WHERE studente = 'Luca'
    """))
    conn.execute(text("""
        UPDATE voti SET data_di_nascita = '2004-11-22' WHERE studente = 'Anna'
    """))
    conn.execute(text("""
        UPDATE voti SET data_di_nascita = '2005-07-09' WHERE studente = 'Marco'
    """))
    conn.execute(text("""
        UPDATE voti SET data_di_nascita = '2006-01-30' WHERE studente = 'Sara'
    """))
    conn.commit()

# 6. Stampa studenti nati nel 2005 con media voti > 4
query_2005 = """
    SELECT studente, AVG(voto) AS media_voto, MIN(data_di_nascita) AS data_di_nascita
    FROM voti
    WHERE EXTRACT(YEAR FROM data_di_nascita) = 2005
    GROUP BY studente
    HAVING AVG(voto) > 4
"""
result_2005 = pd.read_sql_query(query_2005, engine)
print("\nStudenti nati nel 2005 con media voto > 4:")
print(result_2005)
