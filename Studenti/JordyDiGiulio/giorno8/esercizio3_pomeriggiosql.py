import pandas as pd
from sqlalchemy import create_engine, text

"""1.Crea una tabella prodotti con i campi:

id

nome

prezzo

categoria

e crea almeno 10 prodotti


2.Aggiorna il prezzo di un prodotto a 18.0 euro.


– DELETE + filtro
🔧 Obiettivo:
Elimina tutti i prodotti con prezzo inferiore a 2.0 euro.


4.TROVA tutti i prodotti che hanno un prezzo maggiore di 10 e della di una categoria a tua scelta


--------------------------------------
1.Crea una tabella con i campi:

id

cliente

prodotto

quantità

prezzo_unitario

Inserisci 10 ordini
Calcola la spesa totale per ogni cliente (quantità * prezzo_unitario) e mostra solo quelli che hanno speso più di 10 euro.

Aggiorna il prezzo_unitario di un prodtto a 1.2, solo se la quantità è maggiore di 5.

Elimina tutti gli ordini in cui quantità * prezzo_unitario < 5."""

# Connessione al DB (sostituisci con le tue credenziali reali)
engine = create_engine("postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase")

# 1. Crea tabella "prodotti" con 10 righe
df_prodotti = pd.DataFrame([
    {'id': 1, 'nome': 'Pane', 'prezzo': 1.5, 'categoria': 'Alimentari'},
    {'id': 2, 'nome': 'Latte', 'prezzo': 1.2, 'categoria': 'Alimentari'},
    {'id': 3, 'nome': 'Pasta', 'prezzo': 2.5, 'categoria': 'Alimentari'},
    {'id': 4, 'nome': 'Shampoo', 'prezzo': 4.0, 'categoria': 'Igiene'},
    {'id': 5, 'nome': 'Sapone', 'prezzo': 0.9, 'categoria': 'Igiene'},
    {'id': 6, 'nome': 'Cuffie', 'prezzo': 19.0, 'categoria': 'Elettronica'},
    {'id': 7, 'nome': 'Mouse', 'prezzo': 14.0, 'categoria': 'Elettronica'},
    {'id': 8, 'nome': 'Libro', 'prezzo': 11.5, 'categoria': 'Cartoleria'},
    {'id': 9, 'nome': 'Quaderno', 'prezzo': 1.0, 'categoria': 'Cartoleria'},
    {'id': 10, 'nome': 'Acqua', 'prezzo': 0.6, 'categoria': 'Alimentari'},
])

df_prodotti.to_sql('prodotti', engine, index=False, if_exists='replace')

# 2. Aggiorna prezzo di un prodotto a 18.0 (es: Mouse)
with engine.connect() as conn:
    conn.execute(text("""
        UPDATE prodotti
        SET prezzo = 18.0
        WHERE nome = 'Mouse'
    """))
    conn.commit()

# 3. Elimina prodotti con prezzo < 2.0
with engine.connect() as conn:
    conn.execute(text("""
        DELETE FROM prodotti
        WHERE prezzo < 2.0
    """))
    conn.commit()

# 4. Trova prodotti con prezzo > 10 e categoria 'Elettronica'
result1 = pd.read_sql_query("""
    SELECT * FROM prodotti
    WHERE prezzo > 10 AND categoria = 'Elettronica'
""", engine)

print("Prodotti con prezzo > 10 e categoria 'Elettronica':")
print(result1)


# 1. Crea tabella "ordini" con 10 righe
df_ordini = pd.DataFrame([
    {'id': 1, 'cliente': 'Anna', 'prodotto': 'Pane', 'quantità': 2, 'prezzo_unitario': 1.5},
    {'id': 2, 'cliente': 'Marco', 'prodotto': 'Latte', 'quantità': 1, 'prezzo_unitario': 1.2},
    {'id': 3, 'cliente': 'Luca', 'prodotto': 'Pasta', 'quantità': 3, 'prezzo_unitario': 2.5},
    {'id': 4, 'cliente': 'Sara', 'prodotto': 'Shampoo', 'quantità': 1, 'prezzo_unitario': 4.0},
    {'id': 5, 'cliente': 'Anna', 'prodotto': 'Cuffie', 'quantità': 1, 'prezzo_unitario': 19.0},
    {'id': 6, 'cliente': 'Luca', 'prodotto': 'Mouse', 'quantità': 2, 'prezzo_unitario': 14.0},
    {'id': 7, 'cliente': 'Sara', 'prodotto': 'Libro', 'quantità': 1, 'prezzo_unitario': 11.5},
    {'id': 8, 'cliente': 'Anna', 'prodotto': 'Acqua', 'quantità': 6, 'prezzo_unitario': 0.6},
    {'id': 9, 'cliente': 'Marco', 'prodotto': 'Quaderno', 'quantità': 10, 'prezzo_unitario': 0.8},
    {'id': 10, 'cliente': 'Luca', 'prodotto': 'Sapone', 'quantità': 1, 'prezzo_unitario': 0.9},
])

df_ordini.to_sql('ordini', engine, index=False, if_exists='replace')

# 2. Calcola spesa totale per cliente (> 10 euro)
query_spesa = """
    SELECT cliente, SUM(quantità * prezzo_unitario) AS spesa_totale
    FROM ordini
    GROUP BY cliente
    HAVING SUM(quantità * prezzo_unitario) > 10
"""
result2 = pd.read_sql_query(query_spesa, engine)
print("Clienti con spesa totale > 10 euro:")
print(result2)

# 3. Aggiorna prezzo_unitario a 1.2 dove quantità > 5
with engine.connect() as conn:
    conn.execute(text("""
        UPDATE ordini
        SET prezzo_unitario = 1.2
        WHERE quantità > 5
    """))
    conn.commit()

# 4. Elimina ordini con quantità * prezzo_unitario < 5
with engine.connect() as conn:
    conn.execute(text("""
        DELETE FROM ordini
        WHERE quantità * prezzo_unitario < 5
    """))
    conn.commit()