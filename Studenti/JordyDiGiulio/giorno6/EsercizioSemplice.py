import pandas as pd
import matplotlib.pyplot as plt

# Caricamento dati
vendite = pd.DataFrame(
    {
        "Prodotto": ["A", "B", "C", "A", "B", "C"],
        "Mese": ["Gen", "Gen", "Gen", "Feb", "Feb", "Feb"],
        "Quantità": [10, 15, 8, 12, 9, 11],
    }
)
# Analisi: vendite totali per prodotto
totale_prodotti = vendite.groupby("Prodotto")["Quantità"].sum()
print(totale_prodotti.reset_index())
# Visualizzazione
totale_prodotti.plot(kind="bar", color="skyblue")
plt.title("Vendite Totali per Prodotto")
plt.ylabel("Unità Vendute")
plt.show()
