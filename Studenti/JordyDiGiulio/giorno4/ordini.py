import pandas as pd
import matplotlib.pyplot as plt

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


fatturato_giornaliero = df.groupby('Data')['Totale'].sum().reset_index()

print(fatturato_giornaliero)

plt.figure(figsize=(10,8))
plt.bar(fatturato_giornaliero['Data'], fatturato_giornaliero['Totale'], color='skyblue')
plt.title('Fatturato Giornaliero', fontsize=16)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Fatturato', fontsize=12)
plt.tight_layout()
plt.show()

media_prezzoXprodotto = df.groupby('Prodotto')['Prezzo_unitario'].mean().reset_index()

print(media_prezzoXprodotto)












    




