import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style = "whitegrid")

df = sns.load_dataset("tips")
print(df.head())

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data = df,
    x = "total_bill",
    y = "tip",
    hue = "time",
    size = "size",
    palette = "deep"
)

plt.title("Relazione tra Conto Totale e Mancia")
plt.show()