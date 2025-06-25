# Questa esercitazione contiene quattro esercizi di difficoltà media pensati per consolidare le nozioni su liste, insiemi, dizionari e controllo del flusso in Python.

# 1: Data una lista di numeri: 
# a) Crea una nuova lista contenente solo i numeri pari, 
# b) Utilizzando una list comprehension, genera una lista con i quadrati di tutti i numeri.
# c) Stampa la lunghezza di entrambe le liste risultanti.

numbers = [12, 7, 9, 20, 33, 4, 18]
print(f"Starting number list: {numbers}")

even_numbers = []
square_numbers = []
for num in numbers:
    #a)
    if num % 2 == 0:
        even_numbers.append(num)
    #b)
    square_numbers.append(num*num)

print(f"Even number list: {even_numbers}")
print(f"Square number list: {square_numbers}")

#c)
print(f"The lenght of the even number list is {len(even_numbers)}, and of the square number list is {len(square_numbers)}\n")


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

