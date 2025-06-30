import pandas as pd

df = pd.read_csv(r'Studenti\JordyDiGiulio\giorno4\ordini.csv')

print(df.head())

df['Totale'] = df['Quantità'] * df['Prezzo_unitario']

lista_non_spediti = []
for i, ordine in df.iterrows():

    if not ordine['Spedito']:
        lista_non_spediti.append((ordine['OrdineID'], ordine['Data'], 
                                  ordine['Cliente'], ordine['Prodotto'], ordine['Totale']))
    
print(lista_non_spediti)

fatturato_clienti = df.groupby('Cliente')['Totale'].sum().sort_values(ascending=False)

print(fatturato_clienti)

prodotto_più_venduto = df.groupby('Prodotto')['Quantità'].sum().idxmax()


print(prodotto_più_venduto)


# calcola fatturato giornaliero 






    




