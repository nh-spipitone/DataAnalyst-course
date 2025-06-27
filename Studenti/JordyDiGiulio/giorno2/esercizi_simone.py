# 1. TEMPERATURA IN LISTA

temperature_massime = [34, 36, 38, 30, 37, 40, 35]

totale_temperature = sum(temperature_massime)

media = totale_temperature / len(temperature_massime)

temperatura_maggiore = max(temperature_massime)
temperatura_minore = min(temperature_massime)

lista_inversa = sorted(temperature_massime, reverse=True)

dizionario_print = {
    'Media': media,
    'Temperatura Maggiore': temperatura_maggiore,
    'Temperatura Minore': temperatura_minore,
    'Lista Invertita': lista_inversa
}

print(dizionario_print)




# 2. TUPLE IMMUTABILI

tupla_temperature = tuple(temperature_massime)

#tupla_temperature[0] = 12
#TypeError: 'tuple' object does not support item assignment --> La tupla è immutabile e non ammette cambiamenti di valori al suo interno




# 3. SET PER ELIMINARE DUPLICATI

numeri = [3, 5, 3, 7, 5, 9, 3]

set_numeri = set(numeri)

print(f'Lunghezza originale: {len(numeri)}\nLunghezza set: {len(set_numeri)}')




# 4. QUIZ SUI TIPI 

def tipo_collezione(item):

    if isinstance(item, list):
        print('Lista')
    elif isinstance(item, tuple):
        print('Tupla')
    elif isinstance(item, set):
        print('Set')
    elif isinstance(item, dict):
        print('Dizionario')



# 5. CATEGORIE DI VOTO

voto = int(input('Inserisci un voto da 0 a 100: '))

if voto < 60:
    print('Insufficiente')
elif voto < 70:
    print('Sufficiente')
elif voto < 80:
    print('Buono')
elif voto < 90:
    print('Ottimo')
else:
    print('Eccellente')




# 6. TABELLINA CON FOR E RANGE

for numero in range(1, 11):
    print(f'7 x {numero} == {7*numero}')




# 7. INSERIMENTO CONTROLLATO

not_zero = True
lista_numeri = []

while not_zero:
    numero_utente = int(input('prego inserire un numero: '))   
    lista_numeri.append(numero_utente)

    if numero_utente == 0:
        break

lista_numeri.pop()
somma = sum(lista_numeri)
media_numeri = somma/len(lista_numeri)

print(f'Somma = {somma}')
print(f'media = {media_numeri}')



# 8. ANALISI DI DIZIONARIO

spesa = {
    "mele": 3.2,
      "pane": 1.0,
        "latte": 1.5
        }

prodotto = str(input('Inserire prodotto da aggiungere: '))
prezzo = float(input('Inserisci prezzo del prodotto: '))

spesa[prodotto] = prezzo

costo_totale = sum(spesa.values())

nome_articolo_caro = max(spesa, key=spesa.get)

del spesa[nome_articolo_caro]

print(spesa)


# 9. OCCORRENZA DI PAROLE

frase = input("Inserisci una frase: ")


frase = frase.lower()
punteggiatura = ".,;:!?()[]{}\"'-"
for simbolo in punteggiatura:
    frase = frase.replace(simbolo, "")

parole = frase.split()

frequenze = {}
for parola in parole:
    if parola in frequenze:
        frequenze[parola] += 1
    else:
        frequenze[parola] = 1

print("Frequenze delle parole:", frequenze)


parole_comuni = sorted(frequenze.items(), key=lambda item: item[1], reverse=True)[:3]

print("Le 3 parole più comuni:")
for parola, conta in parole_comuni:
    print(f"{parola}: {conta}")


# 10. RUBRICA TELEFONICA

rubrica = {}        
nomi_salvati = set()  

while True:
    print("\n--- MENU ---")
    print("1. Aggiungi contatto")
    print("2. Cerca numero per nome")
    print("3. Elenca tutti i contatti (in ordine alfabetico)")
    print("4. Elimina un contatto")
    print("5. Esci")

    scelta = input("Scegli un'opzione (1-5): ")

    if scelta == "1":
        nome = input("Nome: ").strip()
        if nome in nomi_salvati:
            print("Contatto già presente.")
        else:
            numero = input("Numero: ").strip()
            rubrica[nome] = numero
            nomi_salvati.add(nome)
            print("Contatto aggiunto.")

    elif scelta == "2":
        nome = input("Nome da cercare: ").strip()
        if nome in rubrica:
            print(f"{nome}: {rubrica[nome]}")
        else:
            print("Contatto non trovato.")

    elif scelta == "3":
        if not rubrica:
            print("Nessun contatto salvato.")
        else:
            print("Contatti ordinati:")
            for nome in sorted(rubrica):
                print(f"{nome}: {rubrica[nome]}")

    elif scelta == "4":
        nome = input("Nome da eliminare: ").strip()
        if nome in rubrica:
            del rubrica[nome]
            nomi_salvati.remove(nome)
            print("Contatto eliminato.")
        else:
            print("Contatto non trovato.")

    elif scelta == "5":
        print("Uscita dal programma.")
        break