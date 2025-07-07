import pandas as pd
from sqlalchemy import create_engine, text


"""
ESERCIZIO:Crea una tabella con questi campi:

id

nome

dipartimento

stipendio

E inserisci 4 dipendenti. 
POI Aggiorna lo stipendio di un dipendente a 2300 euro. 
POI Elimina i dipendenti del dipartimento "IT" che hanno uno stipendio superiore a 2100. 
INFINE trova tutti i dipendenti con uno stipendio minore a 1000.
"""


# Connessione (aggiorna con i tuoi dati reali)
engine = create_engine("postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase")

# 2. Crea DataFrame con 4 dipendenti
df = pd.DataFrame([
    {'id': 1, 'nome': 'Anna', 'dipartimento': 'IT', 'stipendio': 2200},
    {'id': 2, 'nome': 'Marco', 'dipartimento': 'HR', 'stipendio': 1800},
    {'id': 3, 'nome': 'Luca', 'dipartimento': 'IT', 'stipendio': 2500},
    {'id': 4, 'nome': 'Sara', 'dipartimento': 'Marketing', 'stipendio': 900}
])

# 3. Scrivi la tabella nel DB (sovrascrive se già esiste)
df.to_sql('dipendenti', engine, index=False, if_exists='replace')

# 4. Aggiorna lo stipendio di Marco a 2300
with engine.connect() as conn:
    conn.execute(text("""
        UPDATE dipendenti
        SET stipendio = 2300
        WHERE nome = 'Marco'
    """))
    conn.commit()

# 5. Elimina i dipendenti del dipartimento "IT" con stipendio > 2100
with engine.connect() as conn:
    conn.execute(text("""
        DELETE FROM dipendenti
        WHERE dipartimento = 'IT' AND stipendio > 2100
    """))
    conn.commit()

# 6. Seleziona i dipendenti con stipendio < 1000
result = pd.read_sql_query("""
    SELECT * FROM dipendenti
    WHERE stipendio < 1000
""", engine)

print("Dipendenti con stipendio < 1000:")
print(result)