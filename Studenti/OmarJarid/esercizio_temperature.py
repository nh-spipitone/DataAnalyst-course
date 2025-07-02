import pandas as pd
import matplotlib.pyplot as plt

def carica_dati(percorso: str) -> pd.DataFrame:
    df = pd.read_csv(percorso)
    return df

df = carica_dati("Esercizi\\Giorno 5\\temperature.csv")
print(df.head())

df["Data"] = pd.to_datetime(df["Data"])

# Calcola la temperatura media della prima settimana.
prima_settimana = df[df["Data"].dt.day <= 7]

media_prima_settimana = prima_settimana["Temperatura"].mean()
print(f"La temperatura media della prima settimana è {media_prima_settimana:.2f}°C")

media_totale = df["Temperatura"].mean()
print(f"La temperatura media totale è {media_totale:.2f}°C")

plt.figure(figsize = (10, 8))
plt.plot(df["Data"], df["Temperatura"], color = "turquoise")
plt.title("Andamento delle temperature giornaliere", fontsize = 16)
plt.xlabel("Data", fontsize = 14)
plt.ylabel("Temperatura (°C)", fontsize = 14)
plt.tight_layout()
plt.show()

df["Giorno"] = df["Data"].dt.to_period("D")
giorni_temperatura = df.groupby("Giorno")["Temperatura"]

giorno_caldo = giorni_temperatura.max().idxmax()
temperatura_calda = giorni_temperatura.max().max()
print(f"Il giorno con la temperatura più alta è {giorno_caldo} con una temperatura di {temperatura_calda}°C")

giorno_freddo = giorni_temperatura.min().idxmin()
temperatura_fredda = giorni_temperatura.min().min()
print(f"Il giorno con la temperatura più bassa è {giorno_freddo} con una temperatura di {temperatura_fredda}°C")