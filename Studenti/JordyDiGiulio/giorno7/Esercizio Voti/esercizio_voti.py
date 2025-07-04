import pandas as pd
df= pd.read_csv(r"Esercizi\Giorno 7\Esercizio Voti\voti.csv")

print(df.head())

media_voti_alunni= df[["Matematica", "Italiano", "Storia"]].mean(axis=1)
print(media_voti_alunni)

media_voti_materia= df[["Matematica", "Italiano", "Storia"]].mean()

print(media_voti_materia)


indice_alunno_migliore= media_voti_alunni.idxmax()
nome_alunno_migliore= df.loc[indice_alunno_migliore,"Nome"]
media_alunno_migliore= media_voti_alunni.max()
print(nome_alunno_migliore)




nomi=df["Nome"]

import matplotlib.pyplot as plt

plt.bar(nomi, media_voti_alunni, color="skyblue")
plt.title("media voti su un grafico a barre")
plt.xlabel("studenti")
plt.ylabel("voti")
plt.show()