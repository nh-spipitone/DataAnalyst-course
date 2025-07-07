import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import date

# 1. Setup
Base = declarative_base()
engine = create_engine("sqlite:///:memory:", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# 2. Modello per la tabella ordini
class Ordine(Base):
    __tablename__ = 'ordini'
    
    id = Column(Integer, primary_key=True)
    cliente = Column(String)
    prodotto = Column(String)
    quantità = Column(Integer)
    prezzo_unitario = Column(Float)
    data_ordine = Column(Date)

Base.metadata.create_all(engine)

# 3. Inserimento di almeno 10 ordini
ordini = [
    Ordine(cliente="Alice", prodotto="Mouse", quantità=1, prezzo_unitario=15.0, data_ordine=date(2025, 7, 1)),
    Ordine(cliente="Bob", prodotto="Tastiera", quantità=1, prezzo_unitario=25.0, data_ordine=date(2025, 7, 2)),
    Ordine(cliente="Claudia", prodotto="USB", quantità=2, prezzo_unitario=2.0, data_ordine=date(2025, 7, 3)),
    Ordine(cliente="Daniele", prodotto="Monitor", quantità=1, prezzo_unitario=120.0, data_ordine=date(2025, 7, 3)),
    Ordine(cliente="Elisa", prodotto="Mouse", quantità=1, prezzo_unitario=15.0, data_ordine=date(2025, 7, 4)),
    Ordine(cliente="Franco", prodotto="USB", quantità=1, prezzo_unitario=2.0, data_ordine=date(2025, 7, 4)),
    Ordine(cliente="Giorgia", prodotto="Tastiera", quantità=2, prezzo_unitario=25.0, data_ordine=date(2025, 7, 5)),
    Ordine(cliente="Hassan", prodotto="Cavo HDMI", quantità=1, prezzo_unitario=4.5, data_ordine=date(2025, 7, 6)),
    Ordine(cliente="Irene", prodotto="Mouse", quantità=2, prezzo_unitario=15.0, data_ordine=date(2025, 7, 6)),
    Ordine(cliente="Luca", prodotto="Tastiera", quantità=1, prezzo_unitario=25.0, data_ordine=date(2025, 7, 7)),
]

session.add_all(ordini)
session.commit()

# 4. Calcola la spesa totale per ogni cliente
df = pd.read_sql_table("ordini", engine)
df["totale"] = df["quantità"] * df["prezzo_unitario"]
spesa_per_cliente = df.groupby("cliente")["totale"].sum().reset_index()
print("💰 Spesa totale per cliente:\n", spesa_per_cliente)

# 5. Trova i clienti che hanno speso più di 50 euro
clienti_over_50 = spesa_per_cliente[spesa_per_cliente["totale"] > 50]
print("\n🏆 Clienti che hanno speso più di 50€:\n", clienti_over_50)

# 6. Elimina ordini con quantità * prezzo_unitario < 5
ordini_da_eliminare = df[df["quantità"] * df["prezzo_unitario"] < 5]["id"].tolist()
session.query(Ordine).filter(Ordine.id.in_(ordini_da_eliminare)).delete(synchronize_session=False)
session.commit()

# 7. Trova prodotti ordinati più di 3 volte in totale (quantità totale > 3)
df_updated = pd.read_sql_table("ordini", engine)
prodotti_frequenti = df_updated.groupby("prodotto")["quantità"].sum().reset_index()
prodotti_3plus = prodotti_frequenti[prodotti_frequenti["quantità"] > 3]
print("\n📦 Prodotti ordinati più di 3 volte:\n", prodotti_3plus)