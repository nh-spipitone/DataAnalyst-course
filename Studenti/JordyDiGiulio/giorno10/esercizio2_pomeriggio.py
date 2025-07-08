import pandas as pd
import sqlite3

# DataFrame delle vendite
vendite = pd.DataFrame({
    'id_vendita': [1, 2, 3, 4],
    'prodotto_id': [201, 202, 201, 203],
    'quantità_venduta': [10, 5, 7, 3],
    'data_vendita': ['2024-01-10', '2024-01-11', '2024-01-12', '2024-01-13']
})

# DataFrame dei prodotti
prodotti = pd.DataFrame({
    'prodotto_id': [201, 202, 203],
    'nome_prodotto': ['Penna', 'Quaderno', 'Gomma'],
    'categoria': ['Cancelleria', 'Cancelleria', 'Accessori'],
    'prezzo_unitario': [1.5, 2.0, 1.0]
})

# Unione dei DataFrame
vendite_prodotti = pd.merge(vendite, prodotti, on='prodotto_id')

# Calcolo ricavo
vendite_prodotti['ricavo'] = vendite_prodotti['quantità_venduta'] * vendite_prodotti['prezzo_unitario']

# Ricavo totale per categoria
ricavo_per_categoria = vendite_prodotti.groupby('categoria')['ricavo'].sum().reset_index()

print("\nVendite con ricavi:")
print(vendite_prodotti)

print("\nRicavi per categoria:")
print(ricavo_per_categoria)