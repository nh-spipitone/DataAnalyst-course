nomi = ["Anna", "Marco", "Elena", "Osvaldo", "Luca", "Irene", "Giorgio", "Umberto"]

nomi_vocali = []
nomi_consonanti = []

for n in nomi:
    if n[0] in ("A", "E", "I", "O", "U"):
        nomi_vocali.append(n)   
    else:
        nomi_consonanti.append(n)

print(f"I nomi che iniziano per vocale sono: {nomi_vocali} mentre quelli che iniziano per consonante sono: {nomi_consonanti}")