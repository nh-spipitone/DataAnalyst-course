import matplotlib.pyplot as plt  # Importa la libreria per creare grafici
import numpy as np  # Importa la libreria per operazioni numeriche e array
from scipy import stats  # Importa il modulo per statistiche e regressione

# Dati di esempio
età = np.array([25, 30, 35, 40, 45, 50, 55, 60, 65])  # Array con i valori delle età
velocità = np.array(
    [12, 11.5, 10.8, 10.2, 9.5, 9.0, 8.2, 7.5, 6.8]
)  # Array con le velocità corrispondenti

# Calcolo della regressione lineare
slope, intercept, r_value, p_value, std_err = stats.linregress(
    età, velocità
)  # Calcola i parametri della retta di regressione

# Creazione della linea di regressione
linea_regressione = (
    intercept + slope * età
)  # Calcola i valori della retta di regressione per ogni età

# Visualizzazione
plt.figure(figsize=(10, 6))  # Crea una nuova figura con dimensioni specificate
plt.scatter(
    età, velocità, color="blue", label="Dati osservati"
)  # Crea uno scatter plot dei dati osservati
plt.plot(
    età,
    linea_regressione,
    color="red",
    label=f"Linea di regressione (y={intercept:.2f}+{slope:.2f}x)",
)  # Disegna la linea di regressione sui dati
plt.title("Relazione tra Età e Velocità di Corsa")  # Imposta il titolo del grafico
plt.xlabel("Età (anni)")  # Imposta l'etichetta dell'asse x
plt.ylabel("Velocità (km/h)")  # Imposta l'etichetta dell'asse y
plt.legend()  # Mostra la legenda
plt.grid(True)  # Mostra la griglia sul grafico
plt.show()  # Visualizza il grafico

# Coefficiente di determinazione
print(f"R²: {r_value**2:.3f}")  # Stampa il coefficiente di determinazione R²
