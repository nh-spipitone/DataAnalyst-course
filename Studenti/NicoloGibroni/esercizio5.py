numeri = [7, -2, 0, 15, -9, 3, 0, 22, -5, 11, -1]
positivi = []
negativi = []
zeri = []
totale = 0

for i in numeri:
    if i > 0:
        positivi.append(i)
    elif i == 0:
        zeri.append(i)
    else:
        negativi.append(i)
    totale += i

media = totale / len(numeri)

sopra_media = []

for i in positivi:
    if i > media:
        sopra_media.append(i)

print(f"Positivi: {positivi}\nNegativi: {negativi}\nZeri: {zeri}\nMedia totale: {media}\nPositivi > media: {sopra_media}")