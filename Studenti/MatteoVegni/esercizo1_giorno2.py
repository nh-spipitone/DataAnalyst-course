# **Temperature in lista**

#     - Crea una lista con le temperature massime della settimana.
#     - Stampa la media, la temperatura più alta e quella più bassa.
#     - Ordina la lista in ordine decrescente e mostrala.

temperature = [28, 30, 27, 32, 29, 31, 26]

somma= 0

for t in temperature:
    somma+= t

media= somma / len(temperature)

massima= temperature[0]
for t in temperature:
    if t > massima:
        massima = t

minima = temperature[0]
for t in temperature:
    if t < minima:
        minima = t

print("Somma delle temperature:", somma)
print("Media delle temperature:", media)
print("la max è:", massima)
print("la min è:", minima)

#Trasforma la lista del punto 1 in una tupla.
#Prova ad assegnare un nuovo valore al primo elemento:
#che errore ottieni? Spiega perché.

temperature_tuple = tuple(temperature)

print("Tupla delle temperature:", temperature_tuple)

#temperature_tuple[0] = 99  errore le tuple non possono essere modificate

# **Set per eliminare duplicati**

# Data la lista `numeri = [3, 5, 3, 7, 5, 9, 3]`, 
# usa un set per rimuovere i duplicati.
# Confronta la lunghezza prima e dopo la trasformazione.

numeri = [3, 5, 3, 7, 5, 9, 3]

lunghezza_numeri= len(numeri)

numeri_senza_duplicati = set(numeri)
lunghezza_numeri_senza_duplicati = len(numeri_senza_duplicati)

print("numero lista con duplicati:", lunghezza_numeri)
print("senza duplicati:", lunghezza_numeri_senza_duplicati)

#Scrivi una funzione `tipo_collezione(obj)` che ritorni la stringa `"lista"`, `"tupla"`, `"set"` o `"dizionario"` in base al tipo dell’oggetto passato.


