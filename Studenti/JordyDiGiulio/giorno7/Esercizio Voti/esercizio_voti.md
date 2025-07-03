
# Esercizio: Analisi dei voti degli studenti

Hai a disposizione il file **voti.csv** con la seguente struttura:

| Nome   | Matematica | Italiano | Storia |
|--------|------------|----------|--------|
| Anna   | 7          | 8        | 6      |
| Marco  | 5          | 6        | 7      |
| Sara   | 9          | 7        | 8      |
| Luca   | 6          | 5        | 6      |
| Giulia | 8          | 9        | 7      |

## Obiettivi

1. Carica il file `voti.csv` in un DataFrame pandas.
2. Calcola e stampa la **media dei voti di ciascun alunno** (media delle tre materie per ogni riga).
3. Calcola e stampa la **media dei voti per ciascuna materia** (media per colonna).
4. Trova e stampa il nome dell’alunno con la media più alta.
5. **Crea un grafico a barre** che mostri la media dei voti di ciascun alunno.

### Suggerimenti
- Per la media sulle righe puoi usare `.mean(axis=1)`, per quella sulle colonne `.mean(axis=0)`.
- Per il grafico a barre puoi usare `matplotlib.pyplot.bar()`.
- Dai un titolo e delle etichette agli assi del grafico.

**Buon lavoro!**
