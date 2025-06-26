#5: Data una lista di numeri iniziale, completa i seguenti obiettivi:
# # dividi i numeri i tre liste per positivi, negativi e zero
# # calcola la media
# # fai un secondo ciclo per creare una lista dei numeri posiitivi sopra la media
# # stampa le tre liste positivi, negativi e zero, la media e la lista dei numeri sopra la media

numeri = [7, -2, 0, 15, -9, 3, 0, 22, -5, 11, -1]
print("Lista originale:     ", numeri)

positivi = []
negativi = []
zero = []
totale = 0

#primo ciclo
for numero in numeri:
    if numero > 0:
        positivi.append(numero)
    elif numero < 0:
        negativi.append(numero)
    else:
        zero.append(numero)
    totale += numero

media = totale / len(numeri)

#secondo ciclo
numeri_sopra_media = []
for numero in positivi:
    if numero > media:
        numeri_sopra_media.append(numero)

# Stampa dei risultati
print("Numeri positivi:     ", positivi)
print("Numeri negativi:     ", negativi)
print("Numeri zero:         ", zero)
print("Media:               ", media)
print("Positivi sopra media:", numeri_sopra_media)
