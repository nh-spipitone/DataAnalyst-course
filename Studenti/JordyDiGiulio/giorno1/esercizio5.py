numeri = [7, -2, 0, 15, -9, 3, 0, 22, -5, 11, -1]

positivi = []
negativi = []
zeri = []

totale = 0

for num in numeri:
    if num > 0:
        positivi.append(num)
    elif num < 0:
        negativi.append(num)
    else:
        zeri.append(num)
    
    totale = totale + num

media = totale / len(numeri)

sopra_media = []

for pos in positivi:
    if pos > media:
        sopra_media.append(pos)

print(f'I valori positivi sono: {positivi}')
print(f'I valori negativi sono: {negativi}')
print(f'Gli zeri sono {zeri}')
print(f'La media è uguale a: {media}')
print(f'I valori sopra la media sono: {sopra_media}')