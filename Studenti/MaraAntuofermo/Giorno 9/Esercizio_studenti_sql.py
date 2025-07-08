import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase"
)

with engine.begin() as conn:
    conn.execute(
        text(
            """CREATE TABLE IF NOT EXISTS studenti(
                      id SERIAL PRIMARY KEY, 
                      studente VARCHAR(50),
                      materia VARCHAR(50),
                      voto INTEGER
                      );"""
        )
    )
    # ---------- INSERT -------------------------------------
    # conn.execute(
    #     text(
    #         "INSERT INTO studenti (studente, materia, voto) VALUES (:studente, :materia, :voto)"
    #     ),
    #     [
    #         {
    #             "studente": "Giulia",
    #             "materia": "Chimica",
    #             "voto": 30,
    #         },
    #         {
    #             "studente": "Alessandro",
    #             "materia": "Biologia",
    #             "voto": 19,
    #         },
    #         {
    #             "studente": "Francesca",
    #             "materia": "Storia",
    #             "voto": 13,
    #         },
    #         {
    #             "studente": "Matteo",
    #             "materia": "Geografia",
    #             "voto": 25,
    #         },
    #         {
    #             "studente": "Elena",
    #             "materia": "Biologia",
    #             "voto": 20,
    #         },
    #         {
    #             "studente": "Davide",
    #             "materia": "Chimica",
    #             "voto": 18,
    #         },
    #     ],
    # )


tabella = pd.read_sql(text("SELECT * FROM studenti;"), con=engine)
print(tabella)

# Media voti per studente


media_voti = pd.read_sql(
    "SELECT studente,AVG(voto) AS media_voti FROM studenti GROUP BY studente;",
    con=engine,
)
print("\nMedia voti per studente:")
print(media_voti)

# Studenti con voto maggiore di 18
query = "SELECT studente,AVG(voto) as media_voti from studenti GROUP BY studente HAVING AVG(voto) >18;"
# No, non è possibile ottenere lo stesso risultato usando WHERE al posto di HAVING in questo caso.
# WHERE filtra le righe prima dell'aggregazione, mentre HAVING filtra dopo l'aggregazione.
# Per filtrare sulla media (che è un valore aggregato), bisogna usare HAVING.

studenti_maggiori_18 = pd.read_sql(
    query,
    con=engine,
)

print("\nStudenti con media voti maggiore di 18:")
print(studenti_maggiori_18)
