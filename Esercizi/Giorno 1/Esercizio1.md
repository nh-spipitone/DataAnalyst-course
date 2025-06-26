## Soluzione

```python
numeri = [7, -2, 0, 15, -9, 3, 0, 22, -5, 11, -1]

positivi = []
negativi = []
zeri = []
totale = 0          # accumulatore della somma totale

# Primo ciclo: classificazione e somma
for n in numeri:
    totale += n          # aggiorna la somma
    if n > 0:
        positivi.append(n)
    elif n < 0:
        negativi.append(n)
    else:
        zeri.append(n)

# Calcolo della media aritmetica
media = totale / len(numeri)

# Secondo ciclo: selezione dei positivi sopra la media
sopra_media = []
for n in positivi:
    if n > media:
        sopra_media.append(n)

# Stampa dei risultati
print("Positivi:", positivi)
print("Negativi:", negativi)
print("Zeri:", zeri)
print("Media totale:", media)
print("Positivi > media:", sopra_media)
```

Eseguendo il codice otterrai un output simile a:

```
Positivi: [7, 15, 3, 22, 11]
Negativi: [-2, -9, -5, -1]
Zeri: [0, 0]
Media totale: 3.6363636363636362
Positivi > media: [7, 15, 22, 11]
```
