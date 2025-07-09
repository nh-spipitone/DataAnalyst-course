import pandas as pd
import sqlite3 

# DataFrame degli ordini
ordini = pd.DataFrame({
    'id_ordine': [1, 2, 3, 4],
    'cliente_id': [101, 102, 101, 103],
    'prodotto': ['Penna', 'Quaderno', 'Matita', 'Gomma'],
    'quantità': [3, 5, 10, 2],
    'prezzo_unitario': [1.5, 2.0, 0.5, 1.0]
})

# DataFrame dei clienti
clienti = pd.DataFrame({
    'cliente_id': [101, 102, 103],
    'nome_cliente': ['Mario Rossi', 'Luisa Verdi', 'Anna Bianchi'],
    'indirizzo': ['Via Roma 1', 'Via Milano 3', 'Via Napoli 5']
})

# Unione dei DataFrame
ordini_clienti = pd.merge(ordini, clienti, on='cliente_id')

# Calcolo totale per ogni ordine
ordini_clienti['totale_ordine'] = ordini_clienti['quantità'] * ordini_clienti['prezzo_unitario']

# Calcolo totale speso per ogni cliente
totale_per_cliente = ordini_clienti.groupby('nome_cliente')['totale_ordine'].sum().reset_index()

print("\nDataFrame completo con totale ordine:")
print(ordini_clienti)

print("\nTotale speso per cliente:")
print(totale_per_cliente)