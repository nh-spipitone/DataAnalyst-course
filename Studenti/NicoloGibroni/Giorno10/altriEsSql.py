import pandas as pd
from sqlalchemy import create_engine, text

username = "root"
password = "root"
host = "localhost"
port = 3306
database = "corso_data_analyst"

DATABASE_URL = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(DATABASE_URL)



# create_table_query = """
# CREATE TABLE IF NOT EXISTS clienti (
#     cliente_id INT AUTO_INCREMENT PRIMARY KEY,
#     nome_cliente VARCHAR(100),
#     indirizzo VARCHAR(100)
# );
# """
# create_table_query2 = """
# CREATE TABLE IF NOT EXISTS ordini (
#     id_ordine INT AUTO_INCREMENT PRIMARY KEY,
#     cliente_id INT,
#     quantità INT,
#     prezzo_unitario INT,
#     FOREIGN KEY (cliente_id) REFERENCES clienti(cliente_id)
# );
# """
# insert_query = """
# INSERT INTO clienti (nome_cliente, indirizzo) VALUES 
# ('Mario Rossi', 'Via Roma 12'),
# ('Luca Bianchi', 'Corso Italia 55'),
# ('Giulia Verdi', 'Via Milano 8'),
# ('Francesca Neri', 'Via Torino 23'),
# ('Andrea Russo', 'Viale Venezia 77'),
# ('Sara Conti', 'Piazza Duomo 10'),
# ('Davide Gallo', 'Via Firenze 34'),
# ('Elisa Bruni', 'Via Napoli 19'),
# ('Marco Ferri', 'Via Bologna 3'),
# ('Chiara Moretti', 'Viale Genova 60');
# """
# insert_query2 = """
# INSERT INTO ordini (cliente_id, quantità, prezzo_unitario) VALUES
# (2, 3, 25),
# (1, 1, 50),
# (3, 5, 15),
# (4, 2, 40),
# (5, 4, 30),
# (6, 6, 10),
# (7, 2, 45),
# (8, 3, 20),
# (9, 1, 100),
# (10, 4, 12);
# """
# with engine.begin() as conn:
#     conn.execute(text(create_table_query))
#     conn.execute(text(create_table_query2))
#     conn.execute(text(insert_query))
#     conn.execute(text(insert_query2))
#     clienti = pd.read_sql("SELECT * FROM clienti", conn)
#     ordini = pd.read_sql("SELECT * FROM ordini", conn)

# df_merged = pd.merge(
#     ordini,
#     clienti,
#     how="left",
#     on="cliente_id"
# )
# df_merged["totale"] = df_merged["quantità"] * df_merged["prezzo_unitario"]
# print(df_merged)



# ---------------------------------------------------------------------------


create_table_vendite = """
CREATE TABLE IF NOT EXISTS vendite (
    id_vendita INT AUTO_INCREMENT PRIMARY KEY,
    prodotto_id INT,
    quantità_venduta INT,
    prezzo_unitario INT,
    data_vendita DATE
);
"""

create_table_ritorni = """
CREATE TABLE IF NOT EXISTS ritorni (
    id_ritorno INT AUTO_INCREMENT PRIMARY KEY,
    id_vendita INT,
    quantità_ritornata INT,
    data_ritorno DATE,
    FOREIGN KEY (id_vendita) REFERENCES vendite(id_vendita)
);
"""

insert_vendite = """
INSERT INTO vendite (prodotto_id, quantità_venduta, prezzo_unitario, data_vendita) VALUES
(101, 10, 20, '2025-06-01'),
(102, 5, 50, '2025-06-03'),
(103, 8, 15, '2025-06-05'),
(104, 3, 40, '2025-06-07'),
(105, 12, 10, '2025-06-10');
"""

insert_ritorni = """
INSERT INTO ritorni (id_vendita, quantità_ritornata, data_ritorno) VALUES
(1, 2, '2025-06-02'),
(3, 1, '2025-06-06'),
(5, 4, '2025-06-12');
"""

with engine.begin() as conn:
    conn.execute(text(create_table_vendite))
    conn.execute(text(create_table_ritorni))
    conn.execute(text(insert_vendite))
    conn.execute(text(insert_ritorni))

    vendite = pd.read_sql("SELECT * FROM vendite", conn)
    ritorni = pd.read_sql("SELECT * FROM ritorni", conn)

df_merged = pd.merge(
    vendite,
    ritorni,
    how="left",
    on="id_vendita"
)
df_merged["totale_ricavo"] = df_merged["quantità_venduta"] * df_merged["prezzo_unitario"]
df_merged["totale_perdita"] = df_merged["quantità_ritornata"] * df_merged["prezzo_unitario"]
df_merged["utile_netto"] = df_merged["totale_ricavo"] - df_merged["totale_perdita"]
print(df_merged[df_merged["utile_netto"]>0])





# Per i clienti premium, calcola la media della spesa e confrontala con la media della spesa dei clienti base.
create_table_clienti = """
CREATE TABLE IF NOT EXISTS clienti (
    cliente_id INT AUTO_INCREMENT PRIMARY KEY,
    nome_cliente VARCHAR(100),
    tipo_cliente VARCHAR(20)  -- 'premium' o 'base'
);
"""
create_table_transazioni = """
CREATE TABLE IF NOT EXISTS transazioni (
    id_transazione INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    importo_transazione FLOAT,
    data_transazione DATE,
    FOREIGN KEY (cliente_id) REFERENCES clienti(cliente_id)
);
"""
insert_clienti = """
INSERT INTO clienti (nome_cliente, tipo_cliente) VALUES
('Mario Rossi', 'premium'),
('Luca Bianchi', 'base'),
('Giulia Verdi', 'premium'),
('Francesca Neri', 'base'),
('Andrea Russo', 'premium'),
('Sara Conti', 'base');
"""
insert_transazioni = """
INSERT INTO transazioni (cliente_id, importo_transazione, data_transazione) VALUES
(1, 250.00, '2025-06-01'),
(1, 400.00, '2025-06-10'),
(2, 150.00, '2025-06-03'),
(2, 100.00, '2025-06-04'),
(3, 500.00, '2025-06-05'),
(3, 600.00, '2025-06-20'),
(4, 50.00,  '2025-06-07'),
(5, 1200.00,'2025-06-09'),
(6, 200.00, '2025-06-15');
"""
with engine.begin() as conn:
    conn.execute(text(create_table_clienti))
    conn.execute(text(create_table_transazioni))
    conn.execute(text(insert_clienti))
    conn.execute(text(insert_transazioni))
    clienti = pd.read_sql("SELECT * FROM clienti", conn)
    transazioni = pd.read_sql("SELECT * FROM transazioni", conn)

df_merged = pd.merge(
    clienti,
    transazioni,
    how="left",
    on="cliente_id"
)
totali = df_merged.groupby("cliente_id")["importo_transazione"].sum().reset_index()
totali.rename(columns={"importo_transazione": "totale_speso"}, inplace=True)
df_merged = pd.merge(
    df_merged,
    totali,
    how="left",
    on="cliente_id"
)
print(df_merged[df_merged["totale_speso"]>1000])
print(df_merged.groupby("tipo_cliente")["importo_transazione"].mean().reset_index())