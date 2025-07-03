import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"Esercizi\Giorno 7\Esercizio Voti\voti.csv")
print(df.head())

# Calcola e stampa la media dei voti di ciascun alunno (media delle 3 materie per ogni riga).
media_voti_alunni = df[["Matematica", "Italiano", "Storia"]].mean(axis = 1)
print(media_voti_alunni.reset_index())

media_voti_materia = df[["Matematica", "Italiano", "Storia"]].mean()
print(media_voti_materia)

indice_alunno_migliore = media_voti_alunni.idxmax()
nome_alunno_migliore = df.loc[indice_alunno_migliore, "Nome"]
media_alunno_migliore = media_voti_alunni.max()
print(f"Alunno con la media più alta: {nome_alunno_migliore} con una media di {media_alunno_migliore:.2f}")

nomi = df["Nome"]

# Grafico a barre.
plt.figure(figsize = (10, 8))
sns.barplot(x = nomi, y = media_voti_alunni)
plt.title("Media voti alunni", fontsize = 16)
plt.xlabel("Alunni", fontsize = 14)
plt.ylabel("Media voti", fontsize = 14)
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()