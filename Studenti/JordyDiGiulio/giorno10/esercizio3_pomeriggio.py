import pandas as pd
import sqlite3

# DataFrame dei dipendenti
dipendenti = pd.DataFrame({
    'id_dipendente': [1, 2, 3, 4],
    'nome_dipendente': ['Giulia', 'Marco', 'Sara', 'Luca'],
    'dipartimento': ['HR', 'IT', 'HR', 'IT']
})

# DataFrame degli stipendi
stipendi = pd.DataFrame({
    'id_dipendente': [1, 2, 3, 4],
    'stipendio': [2100, 2500, 1800, 2300]
})

# Unione dei DataFrame
dipendenti_stipendi = pd.merge(dipendenti, stipendi, on='id_dipendente')

# Media stipendio per dipartimento
media_stipendi = dipendenti_stipendi.groupby('dipartimento')['stipendio'].mean().reset_index()

# Dipartimenti con stipendio medio superiore a 2000
dipartimenti_superiori = media_stipendi[media_stipendi['stipendio'] > 2000]

print("\nDipendenti con stipendi:")
print(dipendenti_stipendi)

print("\nMedia stipendi per dipartimento:")
print(media_stipendi)

print("\nDipartimenti con stipendio medio > 2000:")
print(dipartimenti_superiori)