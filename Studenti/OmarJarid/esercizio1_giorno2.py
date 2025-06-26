# Livello 1
temperature_max = [25, 30, 33, 35, 29, 25]

media = 0
massima = 0
minima = 9999999999999999

# Media
for temp in temperature_max: media += temp
media = media / len(temperature_max)

print(f"La media delle temperature è: {media} °C")

# Massima
for temp in temperature_max:
    if temp > massima: massima = temp

print(f"La temperatura massima è: {massima} °C")

# Minima
for temp in temperature_max:
    if temp < minima: minima = temp

print(f"La temperatura minima è: {minima} °C")

# Lista in ordine decrescente
temperature_max.sort(reverse = True)
print(f"Le temperature in ordine decrescente sono: {temperature_max}")

# Trasforma la lista in una tupla
tupla_temperature = tuple(temperature_max)
print(f"Le temperature in tupla sono: {tupla_temperature}")
#tupla_temperature[0] = 35

# Set per eliminare duplicati dalla lista
set_temperature = set(temperature_max)
print(f"Le temperature senza duplicati sono: {set_temperature}")
new_temperature = list(set_temperature)
print(f"Lunghezza prima: {len(temperature_max)}, Lunghezza dopo: {len(new_temperature)}")

# Livello 2
voto = int(input("Voto: "))
if 0 <= voto < 60:
    print("Insufficiente")
elif voto < 70:
    print("Sufficiente")
elif voto < 80:
    print("Buono")
elif voto < 90:
    print("Ottimo")
elif voto <= 100:
    print("Eccellente")
else:
    print("Voto non valido")

# Tabelline
# Tabellina del 7
for i in range(1, 11): print(f"7 x {i} = {7 * i}")

print()

for i in range(1, 11):
    riga=""
    for j in range(1, 11): riga += f"{i} x {j} = {i * j}\t"
    print(riga)

# Inserimento controllato

numeri = []

while True:
    num = float(input("Inserisci un numero o usa 0 per terminare: "))
    if num == 0: break
    numeri.append(num)

somma = sum(numeri)
media = somma / len(numeri)

print(f"La somma dei numeri inseriti è: {somma}")
print(f"La media dei numeri inseriti è: {media}")

# Livello 3

# Analisi di dizionario
spesa = {"mele": 3.2, "pane": 1.0, "latte": 1.5}
totale = 0

prodotto = input("Aggiungi un prodotto: ")
prezzo = float(input("Prezzo: "))

spesa[prodotto] = prezzo

for prodotto, prezzo in spesa.items(): totale += prezzo

print(f"Costo totale: {totale}")

# Rimuovi l'articolo più caro
max_prezzo = 0
max_prodotto = ""

for prodotto, prezzo in spesa.items():
    if prezzo > max_prezzo:
        max_prezzo = prezzo
        max_prodotto = prodotto

spesa.pop(max_prodotto)

totale = 0
for prodotto, prezzo in spesa.items(): totale += prezzo

print(f"Costo totale aggioranto: {totale}")

# Rubrica telefonica

print("Rubrica telefonica\n")

rubrica = {}

while True:
    #Menu
    print("1. Aggiungi contatto (nome e numero)")
    print("2. Cerca numero per nome")
    print("3. Elenca tutti i contatti ordinati alfabeticamente")
    print("4. Elimina un contatto")
    print("5. Esci\n")

    opzione = int(input("Scelta: "))

    match opzione:
        case 1:
            nome = input("Inserisci il nome del contatto: ")
            if nome in rubrica:
                print("Contatto già presente")
                continue

            numero = input("Inserisci il numero di telefono: ")
            rubrica[nome] = numero
            print(f"Contatto {nome} aggiunto con successo")
        case 2:
            nome = input("Inserisci il nome del contatto da cercare: ")
            if nome in rubrica:
                print(f"Numero di {nome}: {rubrica[nome]}")
            else:
                print("Contatto non trovato")
                continue
        case 3:
            print("Contatti in ordine alfabetico")
            for nome in sorted(rubrica): print(f"{nome}: {rubrica[nome]}")
        case 4:
            nome = input("Inserisci il nome del contatto da eliminare: ")
            if nome in rubrica:
                rubrica.pop(nome)
                print(f"Contatto {nome} eliminato con successo")
            else:
                print("Contatto non trovato")
                continue
        case 5:
            print("Uscita dal programma")
            break
        case _:
            print("Scelta non valida")