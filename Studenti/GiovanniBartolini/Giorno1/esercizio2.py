# 2: Dato un dizionario di impiegati
# a) Stampa i nomi dei dipendenti con età ≥ 30
# b) Calcola l'età media del team
# c) Se più della metà del team ha almeno 30 anni, stampa "Team Senior", altrimenti "Team Junior"

employees = {'Anna': 28, 'Luca': 35, 'Mara': 42, 'Giovanni': 25, 'Paolo': 38}
print(f"Employees dictionary: {employees}")

team_size = len(employees)
age_sum = 0
over30 = []
for name, age in employees.items():
    if age >= 30:
        over30.append(name)
    age_sum += age

# a)
print(f"Employees with age >= 30: {over30}")

#b)
age_average = age_sum / team_size
print(f"The age average of the team is {age_average}")

#c)
senior_team = len(over30) > (team_size/2)
if senior_team:
    print("Team Senior")
else:
    print("Team Junior")


