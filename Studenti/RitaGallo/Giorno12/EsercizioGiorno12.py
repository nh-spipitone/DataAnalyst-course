import numpy as np
import pandas as pd
import sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df_dati = pd.read_csv("DataAnalyst-course//Esercizi//Giorno 12//linear_regression_dataset.csv")

x = df_dati[["Feature"]].values
y = df_dati[["Target"]].values

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, Y_train)

print(f"Coefficiente (pendenza): {model.coef_[0][0]:.3f}")
print(f"Intercetta : {model.itercept_[0]:.3f}")
print(f"R^2: {model.score(X_test, Y_test):.3f}")

plt.scarter(x, y, label="Dati")
X_line = x.copy()
X_line.sort(axis=0)
Y_line = model.predict(X_line)
plt.plot(X_line, Y_line, color = "red", label = "Regr. Lineare")
plt.xlabel("Feature")
plt.ylabel("Target")
plt.title("Regressione Lineare")
plt.legend()
plt.show()
