import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("DataAnalyst-course//Esercizi\Giorno 5//temperature.csv")

df["Data"] = pd.to_datetime(df["Data"])

#filtro giorni solo della prima settimana
prima_settimana = df[df["Data"].dt.day <= 7]

media_settimana = prima_settimana["Temperatura"] .mean()

media_totale = df["Temperatura"] .mean()

print(f"la media delle temperatura della settimana dal 1 al 7 gennaio è: {media_settimana:.2f} gradi")

print(f"la temperatura media totale del periodo analizzato è di: {media_totale:.2f} gradi")


plt.figure(figsize = (10, 8))
plt.plot(df["Data"], df["Temperatura"], marker = "o", linestyle = "-", color = "blue")
plt.title("Temperatura giornaliera", fontsize = 16)
plt.xlabel("Data", fontsize = 16)
plt.ylabel("Temperatura", fontsize = 16)
plt.tight_layout()
plt.show()

df["Giorno"] = df["Data"].dt.to_period("D")
giorni_temperature = df.groupby("Giorno")["Temperatura"]
giorno_caldo = giorni_temperature.max().idxmax()
giorno_caldo_value = giorni_temperature.max().max()
giorno_freddo = giorni_temperature.min().idxmin()
giorno_freddo_value = giorni_temperature.min().min()

print(f"il giorno piu caldo {giorno_caldo} con una temperatura di {giorno_caldo_value}")
print(f"il giorno piu freddo è {giorno_freddo} con una temperatura di {giorno_freddo_value}")



