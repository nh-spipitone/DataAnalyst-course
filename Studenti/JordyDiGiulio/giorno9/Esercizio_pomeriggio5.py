import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date

# 1. Setup database
Base = declarative_base()
engine = create_engine("sqlite:///:memory:", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# 2. Definizione tabella prenotazioni
class Prenotazione(Base):
    __tablename__ = 'prenotazioni'
    
    id = Column(Integer, primary_key=True)
    cliente = Column(String)
    data_prenotazione = Column(Date)
    numero_persone = Column(Integer)
    fascia_oraria = Column(String)  # "pranzo" o "cena"

Base.metadata.create_all(engine)

# 3. Inserimento di almeno 10 prenotazioni
prenotazioni = [
    Prenotazione(cliente="Anna", data_prenotazione=date(2025, 7, 1), numero_persone=2, fascia_oraria="pranzo"),
    Prenotazione(cliente="Luca", data_prenotazione=date(2025, 7, 2), numero_persone=4, fascia_oraria="cena"),
    Prenotazione(cliente="Marco", data_prenotazione=date(2025, 7, 3), numero_persone=1, fascia_oraria="pranzo"),
    Prenotazione(cliente="Giulia", data_prenotazione=date(2025, 7, 4), numero_persone=5, fascia_oraria="cena"),
    Prenotazione(cliente="Elena", data_prenotazione=date(2025, 7, 5), numero_persone=3, fascia_oraria="pranzo"),
    Prenotazione(cliente="Franco", data_prenotazione=date(2025, 7, 6), numero_persone=6, fascia_oraria="cena"),
    Prenotazione(cliente="Irene", data_prenotazione=date(2025, 7, 7), numero_persone=2, fascia_oraria="pranzo"),
    Prenotazione(cliente="Hassan", data_prenotazione=date(2025, 7, 8), numero_persone=4, fascia_oraria="cena"),
    Prenotazione(cliente="Paolo", data_prenotazione=date(2025, 7, 9), numero_persone=3, fascia_oraria="pranzo"),
    Prenotazione(cliente="Chiara", data_prenotazione=date(2025, 7, 10), numero_persone=1, fascia_oraria="cena"),
]

session.add_all(prenotazioni)
session.commit()

# 4. Trova tutte le prenotazioni da 4 o più persone
df = pd.read_sql_table("prenotazioni", engine)
gruppi_grandi = df[df["numero_persone"] >= 4]
print("🍽️ Prenotazioni con 4 o più persone:\n", gruppi_grandi)

# 5. Elimina prenotazioni con meno di 2 persone
ids_da_eliminare = df[df["numero_persone"] < 2]["id"].tolist()
session.query(Prenotazione).filter(Prenotazione.id.in_(ids_da_eliminare)).delete(synchronize_session=False)
session.commit()

# 6. Calcola la media numero_persone per fascia_oraria
df_updated = pd.read_sql_table("prenotazioni", engine)
media_per_fascia = df_updated.groupby("fascia_oraria")["numero_persone"].mean().reset_index()
print("\n📊 Numero medio di persone per fascia oraria:\n", media_per_fascia)