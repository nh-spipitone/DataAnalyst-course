import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date

# 1. Setup
Base = declarative_base()
engine = create_engine("sqlite:///:memory:", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# 2. Modello SQLAlchemy
class Dipendente(Base):
    __tablename__ = 'dipendenti'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    dipartimento = Column(String)
    stipendio = Column(Float)
    data_assunzione = Column(Date)

Base.metadata.create_all(engine)

# 3. Inserisci almeno 8 dipendenti
dipendenti = [
    Dipendente(nome="Mario Rossi", dipartimento="IT", stipendio=2500, data_assunzione=date(2018, 5, 20)),
    Dipendente(nome="Luisa Bianchi", dipartimento="HR", stipendio=2100, data_assunzione=date(2021, 3, 15)),
    Dipendente(nome="Giovanni Verdi", dipartimento="IT", stipendio=3000, data_assunzione=date(2019, 8, 1)),
    Dipendente(nome="Sara Neri", dipartimento="Marketing", stipendio=1800, data_assunzione=date(2022, 1, 10)),
    Dipendente(nome="Elena Gialli", dipartimento="Finance", stipendio=2300, data_assunzione=date(2017, 11, 5)),
    Dipendente(nome="Marco Blu", dipartimento="Finance", stipendio=2200, data_assunzione=date(2020, 6, 30)),
    Dipendente(nome="Anna Rosa", dipartimento="HR", stipendio=2000, data_assunzione=date(2016, 4, 25)),
    Dipendente(nome="Paolo Grigio", dipartimento="Marketing", stipendio=2700, data_assunzione=date(2023, 2, 8)),
]

session.add_all(dipendenti)
session.commit()

# 4. Calcola la media stipendio per ogni dipartimento
df = pd.read_sql_table("dipendenti", engine)
media_per_dip = df.groupby("dipartimento")["stipendio"].mean().reset_index()
print("📊 Media stipendio per dipartimento:\n", media_per_dip)

# 5. Aggiorna lo stipendio a 2000 per chi è stato assunto prima del 2020
session.query(Dipendente)\
    .filter(Dipendente.data_assunzione < date(2020, 1, 1))\
    .update({Dipendente.stipendio: 2000}, synchronize_session=False)
session.commit()

# 6. Calcola la media generale aggiornata
df_updated = pd.read_sql_table("dipendenti", engine)
media_generale = df_updated["stipendio"].mean()

# 7. Seleziona i dipendenti con stipendio sopra la media generale
sopra_media = df_updated[df_updated["stipendio"] > media_generale]
print("\n👔 Dipendenti con stipendio sopra la media generale (media =", round(media_generale, 2), "):\n", sopra_media)