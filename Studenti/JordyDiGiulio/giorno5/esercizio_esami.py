import pandas as pd
import matplotlib.pyplot as plt

# carica file e stampa media ore studio e media punteggi esame
df = pd.read_csv('Studenti\JordyDiGiulio\giorno5\studio_esame.csv')

media_ore = df['OreStudio'].mean()
print(f'media ore : {media_ore}')

media_punteggi = df['PunteggioEsame'].mean()
print(f'media punteggio: {media_punteggi}')

x = df['OreStudio'].to_list()
y = df['PunteggioEsame'].to_list()

posizione_massimo = df['PunteggioEsame'].values.argmax()
nome_massimo = df['Studente'].iloc[posizione_massimo]

plt.figure(figsize=(10,8))
plt.scatter(x, y, marker='o', c='skyblue')
plt.plot(x[posizione_massimo], y[posizione_massimo], marker='o', color='red', label='studente migliore')
plt.text(x[posizione_massimo]-0.15, y[posizione_massimo]+0.4, nome_massimo)
plt.xlabel('OreStudio')
plt.ylabel('PunteggioEsame')
plt.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()


correlazione = df['OreStudio'].corr(df['PunteggioEsame'])
print(f'coeff. correlazione: {correlazione:.2f}')