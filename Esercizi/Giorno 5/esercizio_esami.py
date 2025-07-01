import pandas as pd  # Importa la libreria pandas per la manipolazione dei dati
import matplotlib.pyplot as plt  # Importa matplotlib per la creazione di grafici

# 1. Carica i dati
df = pd.read_csv(
    r"Esercizi\Giorno 5\studio_esame.csv"
)  # Legge il file CSV e lo carica in un DataFrame

# 2. Medie
media_ore = df["OreStudio"].mean()  # Calcola la media delle ore di studio
media_punteggio = df[
    "PunteggioEsame"
].mean()  # Calcola la media dei punteggi degli esami
print(
    f"Media ore di studio: {media_ore:.1f}"
)  # Stampa la media delle ore con 1 decimale
print(
    f"Media punteggio esame: {media_punteggio:.1f}"
)  # Stampa la media dei punteggi con 1 decimale

# 3. Scatter plot
plt.figure(figsize=(7, 4))  # Crea una nuova figura con dimensioni 7x4 pollici
plt.scatter(
    df["OreStudio"], df["PunteggioEsame"]
)  # Crea uno scatter plot con ore di studio sull'asse X e punteggi sull'asse Y
plt.title("Ore di studio vs Punteggio esame")  # Imposta il titolo del grafico
plt.xlabel("Ore di studio")  # Imposta l'etichetta dell'asse X
plt.ylabel("Punteggio esame")  # Imposta l'etichetta dell'asse Y

# 4. Evidenzia lo studente top
idx_top = df[
    "PunteggioEsame"
].idxmax()  # Trova l'indice della riga con il punteggio massimo
x_top = df.loc[
    idx_top, "OreStudio"
]  # Ottiene le ore di studio dello studente con punteggio massimo
y_top = df.loc[idx_top, "PunteggioEsame"]  # Ottiene il punteggio massimo
nome_top = df.loc[
    idx_top, "Studente"
]  # Ottiene il nome dello studente con punteggio massimo
plt.scatter(
    x_top, y_top, s=120, edgecolors="red", facecolors="none", linewidths=2
)  # Evidenzia il punto dello studente top con un cerchio rosso
plt.text(
    x_top + 0.2, y_top, nome_top, color="red"
)  # Aggiunge il nome dello studente accanto al punto

plt.grid(True)  # Abilita la griglia nel grafico
plt.tight_layout()  # Ottimizza automaticamente il layout del grafico
plt.show()  # Mostra il grafico

# 5. Extra: correlazione
corr = df["OreStudio"].corr(
    df["PunteggioEsame"]
)  # Calcola il coefficiente di correlazione di Pearson tra ore di studio e punteggi
print(
    f"Correlazione ore–punteggio: {corr:.2f}"
)  # Stampa la correlazione con 2 decimali
