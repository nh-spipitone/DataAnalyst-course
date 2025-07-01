
# Esercizio: Quanto contano le ore di studio?

**Obiettivo:**  
Esplora la relazione tra il tempo dedicato allo studio e il risultato dell’esame usando *pandas* e *matplotlib*.

---

## Dataset (`studio_esame.csv`)

Crea un file chiamato `studio_esame.csv` con il seguente contenuto di esempio:

```csv
Studente,OreStudio,PunteggioEsame
Alice,4,78
Bruno,6,85
Carla,3,65
Davide,8,92
Elisa,2,58
Fabio,5,80
Giorgia,7,88
Hassan,1,50
Irene,9,95
Luca,4,72
```

---

## ConsegnA

1. **Carica** il file con *pandas*.  
2. Calcola e stampa:  
   - la **media delle ore di studio**  
   - la **media dei punteggi d’esame**  
3. **Crea uno scatter plot** con:  
   - asse x = OreStudio  
   - asse y = PunteggioEsame  
4. **Evidenzia** sul grafico lo studente con il punteggio più alto (marcatore speciale o etichetta).  
5. *(Extra)* Calcola il **coefficiente di correlazione** tra ore di studio e punteggio finale e mostra il valore.

---

## Esempio di codice di partenza

```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. Carica i dati
df = pd.read_csv('studio_esame.csv')

# 2. Medie
media_ore = df['OreStudio'].mean()
media_punteggio = df['PunteggioEsame'].mean()
print(f"Media ore di studio: {media_ore:.1f}")
print(f"Media punteggio esame: {media_punteggio:.1f}")

# 3. Scatter plot
plt.figure(figsize=(7,4))
plt.scatter(df['OreStudio'], df['PunteggioEsame'])
plt.title('Ore di studio vs Punteggio esame')
plt.xlabel('Ore di studio')
plt.ylabel('Punteggio esame')

# 4. Evidenzia lo studente top
idx_top = df['PunteggioEsame'].idxmax()
x_top = df.loc[idx_top, 'OreStudio']
y_top = df.loc[idx_top, 'PunteggioEsame']
nome_top = df.loc[idx_top, 'Studente']
plt.scatter(x_top, y_top, s=120, edgecolors='red', facecolors='none', linewidths=2)
plt.text(x_top + 0.2, y_top, nome_top, color='red')

plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Extra: correlazione
corr = df['OreStudio'].corr(df['PunteggioEsame'])
print(f"Correlazione ore–punteggio: {corr:.2f}")
```

---

Buon lavoro!
