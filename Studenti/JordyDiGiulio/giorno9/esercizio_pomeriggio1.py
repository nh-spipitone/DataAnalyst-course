import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql import select

# 1. Setup SQLAlchemy
Base = declarative_base()
engine = create_engine("postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase")
Session = sessionmaker(bind=engine)
session = Session()

# 2. Definizione del modello
class Libro(Base):
    __tablename__ = 'libri'
    
    id = Column(Integer, primary_key=True)
    titolo = Column(String)
    autore = Column(String)
    anno_pubblicazione = Column(Integer)
    disponibile = Column(Boolean)

# 3. Crea la tabella
Base.metadata.create_all(engine)

# 4. Inserisci 10 libri
libri_iniziali = [
    Libro(id=1, titolo="Il nome della rosa", autore="Umberto Eco", anno_pubblicazione=1980, disponibile=False),
    Libro(id=2, titolo="La solitudine dei numeri primi", autore="Paolo Giordano", anno_pubblicazione=2008, disponibile=True),
    Libro(id=3, titolo="Sapiens", autore="Yuval Noah Harari", anno_pubblicazione=2011, disponibile=True),
    Libro(id=4, titolo="Il codice da Vinci", autore="Dan Brown", anno_pubblicazione=2003, disponibile=False),
    Libro(id=5, titolo="L'amica geniale", autore="Elena Ferrante", anno_pubblicazione=2012, disponibile=True),
    Libro(id=6, titolo="1984", autore="George Orwell", anno_pubblicazione=1949, disponibile=False),
    Libro(id=7, titolo="Harry Potter", autore="J.K. Rowling", anno_pubblicazione=1997, disponibile=True),
    Libro(id=8, titolo="Educated", autore="Tara Westover", anno_pubblicazione=2018, disponibile=False),
    Libro(id=9, titolo="Becoming", autore="Michelle Obama", anno_pubblicazione=2018, disponibile=True),
    Libro(id=10, titolo="La strada", autore="Cormac McCarthy", anno_pubblicazione=2006, disponibile=False),
]

session.add_all(libri_iniziali)
session.commit()

# 5. Seleziona solo i libri disponibili e pubblicati dopo il 2010
query1 = session.query(Libro).filter(Libro.disponibile == True, Libro.anno_pubblicazione > 2010)
df1 = pd.read_sql(query1.statement, engine)
print("📘 Libri disponibili pubblicati dopo il 2010:\n", df1)

# 6. Aggiorna lo stato di un libro (es. id=4, da non disponibile a disponibile)
libro_da_aggiornare = session.query(Libro).filter_by(id=4).first()
if libro_da_aggiornare:
    libro_da_aggiornare.disponibile = True
    session.commit()

# 7. Elimina i libri pubblicati prima del 2000
session.query(Libro).filter(Libro.anno_pubblicazione < 2000).delete()
session.commit()

# 8. Aggiungi 3 libri nuovi
nuovi_libri = [
    Libro(titolo="La vita bugiarda degli adulti", autore="Elena Ferrante", anno_pubblicazione=2020, disponibile=True),
    Libro(titolo="The Midnight Library", autore="Matt Haig", anno_pubblicazione=2021, disponibile=False),
    Libro(titolo="Il colibrì", autore="Sandro Veronesi", anno_pubblicazione=2019, disponibile=True),
]
session.add_all(nuovi_libri)
session.commit()

# 9. Seleziona tutti i libri disponibili pubblicati dopo il 2003
query2 = session.query(Libro).filter(Libro.disponibile == True, Libro.anno_pubblicazione > 2003)
df2 = pd.read_sql(query2.statement, engine)
print("\n📗 Libri disponibili pubblicati dopo il 2003:\n", df2)