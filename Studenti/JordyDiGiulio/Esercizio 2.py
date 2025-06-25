# Dizionario che contiene i dipendenti con i loro nomi come chiavi e le età come valori
employees = {"Anna": 28, "Luca": 35, "Mara": 42, "Giovanni": 25, "Paolo": 38}

# Lista vuota per memorizzare i nomi dei dipendenti over 30
dipendenti_over_30 = []
# Variabile per calcolare la somma totale delle età
sommaeta = 0
# Contatore per il numero di dipendenti over 30
dipendenti_over_30_count = 0

# Ciclo che itera su ogni coppia nome-età nel dizionario employees
for nome, eta in employees.items():

    # Verifica se l'età è maggiore di 30
    if eta > 30:
        # Aggiunge il nome alla lista dei dipendenti over 30
        dipendenti_over_30.append(nome)
        # Incrementa il contatore dei dipendenti over 30
        dipendenti_over_30_count += 1
    # Aggiunge l'età corrente alla somma totale delle età
    sommaeta += eta

# Verifica se i dipendenti over 30 sono più della metà del totale
if dipendenti_over_30_count > len(employees) / 2:
    # Stampa "Team Senior" se la maggioranza ha più di 30 anni
    print("Team Senior")
else:
    # Stampa "Team Junior" se la maggioranza ha 30 anni o meno
    print("Team Junior")

# Calcola l'età media dividendo la somma delle età per il numero totale di dipendenti
mediaeta = int(sommaeta / len(employees))

# Stampa la lista dei dipendenti over 30
print("Dipendenti over 30:", dipendenti_over_30)
# Stampa l'età media dei dipendenti
print("Eta media dei dipendenti:", mediaeta)
