
# Project: Alla ricerca del **sonno perfetto** 😴🕵️‍♂️  
_Dataset: `Sleep_health_and_lifestyle_dataset.csv`_

Obiettivo: esplorare come **abitudini di vita** e **parametri fisiologici** influiscono su **qualità** e **durata** del sonno.  
Lavora in un notebook Jupyter (o file `.py`) utilizzando **Pandas** e **Matplotlib**.

---

## STEP 0 – Setup
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
```

> *Suggerimento:* dai un’occhiata a `df.head()` e `df.info()` per capire struttura e tipi di dato.

---

## STEP 1 – Pulizia minima
1. **Tipi di dato**  
   - Converti opportunamente le colonne numeriche.  
   - Trasforma la colonna `Sleep Disorder` in stringa e rimpiazza i `NaN` con `"None"`.

2. **Pressione sanguigna**  
   - La colonna `"Blood Pressure"` è in formato `"120/80"`.  
     Crea due nuove colonne: `Systolic` e `Diastolic` (interi).

> *Suggerimento:* `str.split("/", expand=True)` potrebbe tornarti utile.

---

## STEP 2 – Analisi esplorativa
Rispondi, con qualche statistica descrittiva, alle domande:

| # | Domanda |
|---|---------|
| 2.1 | Quanto dormono in media **uomini** vs **donne**? |
| 2.2 | Quante persone riportano **“Sleep Apnea”** rispetto a nessun disturbo? |
| 2.3 | La **Qualità del sonno** varia tra le categorie di **BMI**? |

> *Suggerimento:* `groupby`, `value_counts`, `agg`.

---

## STEP 3 – Visualizzazione (2 × 2 subplot)
Costruisci una figura con 4 grafici:

| Pos. | Grafico | Descrizione |
|------|---------|-------------|
| (0, 0) | Bar plot | Media **Sleep Duration** per **Occupation** (mostra solo le 6 professioni più frequenti). |
| (0, 1) | Scatter | **Sleep Duration** vs **Physical Activity Level**; colora i punti in base a **Stress Level**. |
| (1, 0) | Bar plot | Conteggio di ogni **Sleep Disorder** (incluso `"None"`). |
| (1, 1) | Line plot | Media **Heart Rate** per età. |

> *Suggerimento:* ricorda `fig, axes = plt.subplots(2, 2)` e `plt.tight_layout()`.

---

## STEP 4 – Indagine mirata
1. **Sleep Apnea vs None**  
   - Crea due subset (Apnea / None) e confronta **Stress Level** e **Sleep Duration**.

2. **Soglia di stress**  
   - Filtra le persone con `Stress Level ≥ 8` **e** `Sleep Duration < 6`.  
     Calcola quante sono e la loro età media.

> *Suggerimento:* una rapida visualizzazione (boxplot o histogram) può aiutare.

---

## STEP 5 – Domanda aperta (bonus)
> *Se dovessi dare un solo consiglio pratico per migliorare la qualità del sonno a chi lavora come **Software Engineer**, quale sarebbe?*  
> Scegli **una variabile dello stile di vita** che sembra avere la correlazione più forte con `Quality of Sleep` per quel gruppo.  
> Supporta la tua risposta con **una metrica** (es. correlazione) e **un grafico sintetico**.

---

### Checklist
- [ ] Colonne correttamente tipizzate (inclusi `Systolic` e `Diastolic`).
- [ ] Figura 2 × 2 creata senza errori.
- [ ] Confronto chiaro tra gruppi “Apnea” e “None”.
- [ ] Filtraggio “stress ≥ 8 & sleep < 6” eseguito e commentato.
- [ ] Osservazioni principali riportate in poche righe di markdown.

Buon divertimento!  
_(Se ti serve un hint in più o vuoi verificare i risultati, chiedi pure.)_
