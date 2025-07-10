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

# mostra i risultati in un grafico plot
plt.scatter(
    età, velocità, color="blue", label="Dati"
)  # Crea un grafico a dispersione dei dati
plt.plot(
    età, slope * età + intercept, color="red", label="Regressione Lineare"
)  # Disegna la retta di regressione
plt.xlabel("Età")  # Etichetta asse x
plt.ylabel("Velocità")  # Etichetta asse y
plt.title("Regressione Lineare tra Età e Velocità")  # Titolo del grafico
plt.legend()  # Mostra la legenda
plt.show()  # Visualizza il grafico
