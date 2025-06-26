# Lista di numeri da analizzare
numeri = [7, -2, 0, 15, -9, 3, 0, 22, -5, 11, -1]

# Inizializzazione di liste vuote per categorizzare i numeri
positivi = []  # Lista per i numeri positivi
negativi = []  # Lista per i numeri negativi
zeri = []  # Lista per gli zeri

# Variabile per calcolare la somma totale
totale = 0

# Ciclo per ogni numero nella lista
for num in numeri:
    # Se il numero è positivo
    if num > 0:
        positivi.append(num)  # Aggiunge alla lista dei positivi
    # Se il numero è negativo
    elif num < 0:
        negativi.append(num)  # Aggiunge alla lista dei negativi
    # Se il numero è zero
    else:
        zeri.append(num)  # Aggiunge alla lista degli zeri

    # Somma il numero corrente al totale
    totale = totale + num

# Calcola la media dividendo il totale per il numero di elementi
media = totale / len(numeri)

# Lista per i valori positivi sopra la media
sopra_media = []

# Ciclo per ogni numero positivo
for pos in positivi:
    # Se il numero positivo è maggiore della media
    if pos > media:
        sopra_media.append(pos)  # Aggiunge alla lista sopra_media

# Stampa i risultati
print(f"I valori positivi sono: {positivi}")
print(f"I valori negativi sono: {negativi}")
print(f"Gli zeri sono {zeri}")
print(f"La media è uguale a: {media}")
print(f"I valori sopra la media sono: {sopra_media}")
