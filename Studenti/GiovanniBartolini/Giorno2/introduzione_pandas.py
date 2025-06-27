import pandas as pd

df = pd.read_csv('/home/giovanni/Programs/Python3/DataAnalyst-course/Esercizi/Giorno 2/prova.csv')

print("DataFrame originale:")
print(df)

df['Totale'] = df['Prezzo_unitario'] * df['Quantità']
print("\nDataFrame con la colonna 'Totale':")
print(df)

ricavo_totale = df['Totale'].sum()
print(f"\nRicavo totale: {ricavo_totale:.2f}€")

print("Lunghezza: ", len(df['Prezzo_unitario']))
media_prezzo_unitario = df['Prezzo_unitario'].sum() / len(df['Prezzo_unitario'])
print(f"Media dei prezzi unitari: {media_prezzo_unitario:.2f}€")

# Statistiche sui prezzi unitari con funzioni predefinite
print("\nStatistiche sui prezzi unitari:")
print("Somma:    \t", df['Prezzo_unitario'].sum())
print("Media:    \t", df['Prezzo_unitario'].mean())
print("Massimo:  \t", df['Prezzo_unitario'].max())
print("Minimo:   \t", df['Prezzo_unitario'].min())
print("Dev. standard: \t", df['Prezzo_unitario'].std())

