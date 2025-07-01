import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("DataAnalyst-course/Esercizi/Giorno 5/temperature.csv")

df["Data"] = pd.to_datetime(df["Data"])

#Filtro giorni solo della prima settimana 
prima_settimana = df[df["Data"].dt.day<= 7]

media_settimana = prima_settimana["Temperatura"].mean()

media_totale = df["Temperatura"].mean()


#Per mostrare solo le prime cifre decimali (formattazione)
print(f"La media delle temperature dal 1 al 7 gennaio è {media_settimana:.2f} °C ")

print(f"La temperatura media totale è di {media_totale: .2f} °C")

plt.figure(figsize = (10, 8))


plt.plot(df["Data"], df["Temperatura"], marker = "o")

plt.title("Temperature giornaliere", fontsize = 16)
plt.xlabel("Data", fontsize = 13)
plt.ylabel("Temperatura", fontsize = 13)
plt.show()


