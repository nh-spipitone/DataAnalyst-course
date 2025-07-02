# Importa la libreria pandas per manipolazione dati
import pandas as pd

# Importa matplotlib per la creazione di grafici
import matplotlib.pyplot as plt

# Importa numpy per operazioni numeriche e generazione dati casuali
import numpy as np

# Simulazione dati finanziari
# Imposta il seed per rendere riproducibili i numeri casuali
np.random.seed(42)
# Crea un range di date dal 1 gennaio 2022 per 100 giorni consecutivi
date_range = pd.date_range(start="2022-01-01", periods=100, freq="D")
# Crea un DataFrame con dati simulati di due azioni
azioni = pd.DataFrame(
    {
        # Colonna con le date
        "Data": date_range,
        # Prezzo azione A: numeri casuali normali (media 100, dev std 5) sommati cumulativamente + 100
        "Prezzo_A": np.random.normal(100, 5, 100).cumsum() + 100,
        # Prezzo azione B: numeri casuali normali (media 150, dev std 3) sommati cumulativamente + 150
        "Prezzo_B": np.random.normal(150, 3, 100).cumsum() + 150,
    }
)
# Calcolo rendimento percentuale
# Calcola il rendimento percentuale giornaliero dell'azione A
azioni["Rendimento_A"] = azioni["Prezzo_A"].pct_change() * 100
# Calcola il rendimento percentuale giornaliero dell'azione B
azioni["Rendimento_B"] = azioni["Prezzo_B"].pct_change() * 100
# Analisi correlazione
# Calcola la matrice di correlazione tra i rendimenti delle due azioni
corr = azioni[["Rendimento_A", "Rendimento_B"]].corr()

# Visualizzazione andamento prezzi
# Crea un grafico lineare con le date sull'asse x e i prezzi delle azioni sull'asse y
azioni.plot(
    x="Data",  # Colonna per l'asse x
    y=["Prezzo_A", "Prezzo_B"],  # Colonne per l'asse y
    figsize=(12, 6),  # Dimensioni del grafico
    title="Andamento Prezzi Azioni",  # Titolo del grafico
)
# Mostra il grafico
plt.show()
