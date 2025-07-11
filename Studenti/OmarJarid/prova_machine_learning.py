import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df_dati = pd.read_csv(r'Esercizi\Giorno 12\linear_regression_dataset.csv')

x = df_dati[['Feature']].values
y = df_dati['Target'].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

model = LinearRegression()
model.fit(x_train, y_train)

print(f"Coefficiente (pendenza): {model.coef_[0][0]:.3f}")
print(f"Intercetta: {model.intercept_[0]:.3f}")
print(f"R^2: {model.score(x_test, y_test):.3f}")

plt.scatter(x, y, label='Dati')
x_line = x.copy()
x_line.sort(axis=0)
y_line = model.predict(x_line)
plt.plot(x_line, y_line, color='red', label='Regr. Lineare')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.title('Regressione Lineare')
plt.legend()
plt.show()