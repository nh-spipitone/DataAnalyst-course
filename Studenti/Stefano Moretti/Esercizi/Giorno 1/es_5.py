numeri = [7, -2, 0, 15, -9, 3, 0, 22, -5, 11, -1]

positivi = []
negativi = []
zeri = []
sopra_media = []
totale = 0

for num in numeri:
    if num > 0:
        positivi.append(num)
    elif num < 0:
        negativi.append(num)
    elif num == 0:
        zeri.append(num)
    totale = totale + num

media = sum(numeri) / len(numeri)

for num in numeri:
    if num > media:
        sopra_media.append(num) 



print("Numeri positivi:", positivi)
print("Numeri negativi:", negativi)
print("Numeri zero:", zeri)
print("Media:", media)
print("Numeri sopra la media:", sopra_media)