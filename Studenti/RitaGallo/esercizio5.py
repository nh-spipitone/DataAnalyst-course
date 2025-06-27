numeri = [7, -2, 0, 15, -9, 3, 0, 22, -5, 11, -1]

positivi = []
negativi = []
zeri = []

media = 0
totale = 0

for num in numeri:
    if num > 0:
        positivi.append(num)
    elif num < 0:
        negativi.append(num)
    else:
        zeri.append(num)

    totale += num
    media += 1

media = totale /len(numeri)

sopra_media = []

for pos in positivi:
    if pos > media:
        sopra_media.append(pos)

print(f"i valori positivi: {positivi}")
print(f"i valori negativi: {negativi}")
print(f"i volori zeri: {zeri}")
print(f"la media è uguale a: {media}")
print(f"i valori sopra la media sono: {sopra_media}")
