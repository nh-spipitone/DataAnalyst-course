import pandas as pd  # Importa la libreria pandas per la manipolazione dei dati
import matplotlib.pyplot as plt  # Importa matplotlib per la creazione di grafici

# Carica i dati dal file CSV.
df = pd.read_csv("Esercizi\\Giorno 5\\ordini_amazon.csv")
# print(df.head()) # Stampa solo le prime 5 righe del DataFrame (opzionale per debug).

# Filtra solo gli ordini con stato "Consegnato".
df_consegnati = df[df["Stato"] == "Consegnato"]
# print(df_consegnati) # Stampa il DataFrame filtrato (opzionale per debug).

# Aggiungi una colonna "Totale" calcolata come Quantità * Prezzo.
df["Totale"] = df["Quantità"] * df["Prezzo"]

# Calcola il totale speso per ogni categoria raggruppando per "Categoria".
totale_per_categoria = df.groupby("Categoria")["Totale"].sum()
print(totale_per_categoria)  # Stampa il totale speso per categoria.

# Crea un grafico a barre delle spese totali per categoria.
plt.figure(figsize=(10, 8))  # Imposta la dimensione della figura.
totale_per_categoria = df.groupby("Categoria")[
    "Totale"
].sum()  # Ricalcola il totale per sicurezza.
totale_per_categoria.plot(kind="bar", color="turquoise")  # Crea il grafico a barre.
plt.title("Totale speso per categoria", fontsize=16)  # Titolo del grafico.
plt.xlabel("Categoria", fontsize=14)  # Etichetta asse x.
plt.ylabel("Totale speso (€)", fontsize=14)  # Etichetta asse y.
plt.tight_layout()  # Ottimizza il layout.
plt.show()  # Mostra il grafico.

# Converte la colonna "Data" in formato datetime.
df["Data"] = pd.to_datetime(df["Data"])
# Crea una nuova colonna "Mese" con solo anno e mese.
df["Mese"] = df["Data"].dt.to_period("M")
# Calcola la spesa totale per ogni mese.
spesa_mensile = df.groupby("Mese")["Totale"].sum()

# Crea un grafico della spesa mensile.
plt.figure(figsize=(8, 4))  # Imposta la dimensione della figura.
spesa_mensile.plot(
    marker="o", linestyle="-", color="orange"
)  # Crea il grafico a linee.
plt.title("Spesa mensile", fontsize=16)  # Titolo del grafico.
plt.xlabel("Data", fontsize=14)  # Etichetta asse x.
plt.ylabel("Spesa", fontsize=14)  # Etichetta asse y.
plt.show()  # Mostra il grafico.

# Trova il mese con la spesa più alta.
mese_più_costoso = spesa_mensile.idxmax()
print(f"Mese più costoso: {mese_più_costoso}")  # Stampa il mese più costoso.

# Trova la categoria con la spesa più alta.
categoria_più_costosa = totale_per_categoria.idxmax()
categoria_più_costosa_tot = totale_per_categoria.max()
print(
    f"La categoria più costosa è {categoria_più_costosa} con un totale di {categoria_più_costosa_tot} €"
)  # Stampa la categoria più costosa e il totale speso.
