import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date

# 1. Setup database
Base = declarative_base()
engine = create_engine("sqlite:///:memory:", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# 2. Definizione della tabella ordini
class Ordine(Base):
    __tablename__ = 'ordini'
    
    id = Column(Integer, primary_key=True)
    cliente = Column(String)
    prodotto = Column(String)
    quantità = Column(Integer)
    prezzo_unitario = Column(Float)
    data_ordine = Column(Date)

Base.metadata.create_all(engine)

# 3. Inserisci almeno 15 ordini
ordini = [
    Ordine(cliente="Anna", prodotto="Penna", quantità=2, prezzo_unitario=1.5, data_ordine=date(2025, 7, 1)),
    Ordine(cliente="Luca", prodotto="Quaderno", quantità=3, prezzo_unitario=2.0, data_ordine=date(2025, 7, 2)),
    Ordine(cliente="Marco", prodotto="Zaino", quantità=1, prezzo_unitario=25.0, data_ordine=date(2025, 7, 3)),
    Ordine(cliente="Giulia", prodotto="Penna", quantità=5, prezzo_unitario=1.2, data_ordine=date(2025, 7, 4)),
    Ordine(cliente="Sara", prodotto="Matita", quantità=10, prezzo_unitario=0.4, data_ordine=date(2025, 7, 5)),
    Ordine(cliente="Elena", prodotto="Astuccio", quantità=1, prezzo_unitario=6.5, data_ordine=date(2025, 7, 6)),
    Ordine(cliente="Franco", prodotto="Zaino", quantità=1, prezzo_unitario=30.0, data_ordine=date(2025, 7, 7)),
    Ordine(cliente="Paolo", prodotto="Quaderno", quantità=2, prezzo_unitario=2.5, data_ordine=date(2025, 7, 8)),
    Ordine(cliente="Anna", prodotto="Evidenziatore", quantità=3, prezzo_unitario=1.0, data_ordine=date(2025, 7, 9)),
    Ordine(cliente="Chiara", prodotto="Zaino", quantità=1, prezzo_unitario=28.0, data_ordine=date(2025, 7, 10)),
    Ordine(cliente="Giulia", prodotto="Matita", quantità=5, prezzo_unitario=0.5, data_ordine=date(2025, 7, 11)),
    Ordine(cliente="Luca", prodotto="Astuccio", quantità=1, prezzo_unitario=7.0, data_ordine=date(2025, 7, 12)),
    Ordine(cliente="Marco", prodotto="Evidenziatore", quantità=2, prezzo_unitario=1.5, data_ordine=date(2025, 7, 13)),
    Ordine(cliente="Sara", prodotto="Penna", quantità=2, prezzo_unitario=1.3, data_ordine=date(2025, 7, 14)),
    Ordine(cliente="Elena", prodotto="Quaderno", quantità=4, prezzo_unitario=2.0, data_ordine=date(2025, 7, 15)),
]

session.add_all(ordini)
session.commit()

# 4. Calcola il totale speso da ogni cliente
df = pd.read_sql_table("ordini", engine)
df["totale"] = df["quantità"] * df["prezzo_unitario"]
spesa_cliente = df.groupby("cliente")["totale"].sum().reset_index()
print("💰 Totale speso da ogni cliente:\n", spesa_cliente)

# 5. Calcola la spesa media generale
spesa_media_generale = spesa_cliente["totale"].mean()
print(f"\n📊 Spesa media generale: €{spesa_media_generale:.2f}")

# 6. Trova i clienti che hanno speso sopra la media generale
sopra_media = spesa_cliente[spesa_cliente["totale"] > spesa_media_generale]
print("\n🏆 Clienti che hanno speso sopra la media:\n", sopra_media)

# 7. Elimina gli ordini con totale riga < 3 €
id_da_eliminare = df[df["totale"] < 3]["id"].tolist()
session.query(Ordine).filter(Ordine.id.in_(id_da_eliminare)).delete(synchronize_session=False)
session.commit()

# Verifica finale (opzionale)
df_finale = pd.read_sql_table("ordini", engine)
print("\n📦 Ordini rimanenti dopo eliminazione (<3€):\n", df_finale)
