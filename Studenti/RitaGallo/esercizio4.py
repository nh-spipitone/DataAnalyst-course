nomi = ["Anna", "Marco", "Elena", "Osvaldo", "Luca", "Irene", "Giorgio", "Umberto"]

vocali = []
consonanti = []

for n in nomi:
    if n[0].lower() in ("a", "e", "i", "o", "u"):
        vocali.append(n)

    else:
        consonanti.append(n)

print("i nomi che iniziano per vocale sono:", vocali)
print("i nomi che iniziano per cosonante sono:", consonanti)