import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date

# 1. Setup database
Base = declarative_base()
engine = create_engine("postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase")
Session = sessionmaker(bind=engine)
session = Session()

# 2. Definizione della tabella
class Prestito(Base):
    __tablename__ = 'prestiti'
    
    id = Column(Integer, primary_key=True)
    utente = Column(String)
    libro = Column(String)
    data_prestito = Column(Date)
    restituito = Column(Boolean)

Base.metadata.create_all(engine)

# 3. Inserimento di almeno 10 prestiti
prestiti = [
    Prestito(utente="Anna", libro="1984", data_prestito=date(2021, 1, 10), restituito=False),
    Prestito(utente="Luca", libro="Il signore degli anelli", data_prestito=date(2023, 5, 22), restituito=True),
    Prestito(utente="Anna", libro="Il piccolo principe", data_prestito=date(2021, 7, 3), restituito=False),
    Prestito(utente="Marco", libro="Sapiens", data_prestito=date(2022, 8, 15), restituito=True),
    Prestito(utente="Luca", libro="Harry Potter", data_prestito=date(2024, 2, 1), restituito=False),
    Prestito(utente="Giulia", libro="Il codice da Vinci", data_prestito=date(2020, 3, 10), restituito=True),
    Prestito(utente="Elisa", libro="La strada", data_prestito=date(2021, 12, 12), restituito=False),
    Prestito(utente="Anna", libro="La coscienza di Zeno", data_prestito=date(2022, 11, 9), restituito=True),
    Prestito(utente="Marco", libro="Educated", data_prestito=date(2021, 6, 20), restituito=False),
    Prestito(utente="Giulia", libro="Il nome della rosa", data_prestito=date(2023, 4, 30), restituito=False),
]

session.add_all(prestiti)
session.commit()

# 4. Trova tutti i prestiti attivi (non restituiti)
df = pd.read_sql_table("prestiti", engine)
prestiti_attivi = df[df["restituito"] == False]
print("Prestiti attivi (non restituiti):\n", prestiti_attivi)

# 5. Aggiorna tutti i prestiti del 2021 a "restituito = 1"
session.query(Prestito)\
    .filter(Prestito.data_prestito.between(date(2021, 1, 1), date(2021, 12, 31)))\
    .update({Prestito.restituito: True}, synchronize_session=False)
session.commit()

# 6. Conta quanti libri ogni utente ha preso in prestito (totali, non solo attivi)
df_updated = pd.read_sql_table("prestiti", engine)
conteggio_per_utente = df_updated.groupby("utente")["id"].count().reset_index(name="totale_prestiti")
print("Libri presi in prestito per utente:\n", conteggio_per_utente)