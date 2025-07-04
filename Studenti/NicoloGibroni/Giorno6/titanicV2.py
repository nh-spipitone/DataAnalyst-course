import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"DataAnalyst-course\Studenti\NicoloGibroni\Giorno6\titanic-1.csv")
#Raggruppa per classe e sesso, e calcola il numero di sopravvissuti e la tariffa media
report = df.groupby(['Pclass', 'Sex']).agg(
    Sopravvissuti=('Survived', 'sum'),
    TariffaMedia=('Fare', 'mean')
).reset_index()

#Ordina i risultati per classe e sesso
report = report.sort_values(by=['Pclass', 'Sex'])

#Visualizza il DataFrame
print(report)

#Crea il grafico a barre per il numero di sopravvissuti
plt.figure(figsize=(8, 5))
for sex in ['male', 'female']:
    subset = report[report['Sex'] == sex]
    plt.bar(subset['Pclass'].astype(str), subset['Sopravvissuti'], label=sex, alpha=0.7)

plt.title('Sopravvissuti per Classe e Sesso')
plt.xlabel('Classe')
plt.ylabel('Numero di sopravvissuti')
plt.legend(title="Sesso")
plt.tight_layout()
plt.show()