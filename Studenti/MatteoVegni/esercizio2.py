employees = {"Anna": 28, "Luca": 35, "Mara": 42, "Giovanni": 25, "Paolo": 38}

dipendenti_over_30 = []
sommaeta = 0
dipendenti_over_30_count = 0

for nome, eta in employees.items():
    if eta > 30:
        dipendenti_over_30.append(nome)
        dipendenti_over_30_count += 1
    sommaeta += eta

if dipendenti_over_30_count > len(employees) / 2:
    print("Team Senior")
else:
    print("Team junior")

mediaeta = int(sommaeta / len(employees))
print("Dipendenti over 30:", dipendenti_over_30)

print("Eta media dei dipendenti:", mediaeta)

