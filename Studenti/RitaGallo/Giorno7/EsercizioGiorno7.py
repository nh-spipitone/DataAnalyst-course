import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("DataAnalyst-course//Esercizi//Giorno 7//Esercizio Voti//voti.csv")
print(df.head())

media_voti_alunno = df[["Matematica", "Italiano", "Storia"]].mean(axis = 1)        #axis = 1 per calcolare la media per riga
print(media_voti_alunno.reset_index())

media_voti_materie = df[["Matematica", "Italiano", "Storia"]].mean()          
print(media_voti_materie)

indice_alunno_migliore = media_voti_alunno.idxmax()
nome_alunno_migliore = df.loc[indice_alunno_migliore, "Nome"]
media_alunno_migliore = media_voti_alunno.max()
print(nome_alunno_migliore)

nomi_alunni = df["Nome"]

plt.bar(nomi_alunni, media_voti_alunno, color = "skyblue", edgecolor = "black")
plt.title("Media dei voti in un grafico a barre")
plt.xlabel("Studenti")
plt.ylabel("Voti")
plt.tight_layout()
plt.show()



