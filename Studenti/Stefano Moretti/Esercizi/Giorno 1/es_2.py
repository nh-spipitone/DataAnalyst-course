employees = {'Anna': 28, 'Luca': 35, 'Mara': 42, 'Giovanni': 25, 'Paolo': 38}

dipendenti_over_30 = []

somma_eta = 0

dipendenti_over_30_count = 0
for name, age in employees.items():
    if age >= 30:
        dipendenti_over_30.append(name)
        dipendenti_over_30_count += 1
    somma_eta += age

if dipendenti_over_30_count > len(employees) / 2:
    print("Team Senior")
else:
    print("Team Junior")


print(f"I dipendenti over 30 sono: {dipendenti_over_30}")


media_eta = sum(employees.values()) / len(employees)
print(f"L'età media dei dipendenti è: {media_eta}")



