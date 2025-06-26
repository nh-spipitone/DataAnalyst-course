# LIVELLO 1: Fondamentali

# 1. Temperature in lista:
# # Crea una lista con le temperature massime della settimana.
# # Stampa la media, la temperatura più alta e quella più bassa.
# # Ordina la lista in ordine decrescente e mostrala.

temperature = [32, 35, 29, 30, 28, 34, 31]

media = sum(temperature) / len(temperature)
temperatura_massima = max(temperature)
temperatura_minima = min(temperature)

print(f"Media: {media}°C")
print(f"Temperatura massima: {temperatura_massima}°C")
print(f"Temperatura minima: {temperatura_minima}°C")


# 2. Tuple immutabili
# # Trasforma la lista del punto 1 in una tupla.
# # Prova ad assegnare un nuovo valore al primo elemento: che errore ottieni? Spiega perché.

temperature_tuple = tuple(temperature)
#temperature_tuple[0] = 33  # non è possibile, ma per esempio
print(f"Temperatura in tupla: {temperature_tuple}")


# 3. Set per eliminare duplicati
# # Data una lista di numeri, usa un set per rimuovere i duplicati.
# # Confronta la lunghezza prima e dopo la trasformazione.

numeri = [3, 5, 3, 7, 5, 9, 3]
print(f"Lista originale: {numeri}")

# Creazione di un set per rimuovere i duplicati
numeri_set = set(numeri)

# Confronto delle lunghezze
print(f"Lunghezza lista originale: {len(numeri)}")
print(f"Lunghezza set senza duplicati: {len(numeri_set)}")
print(f"Set senza duplicati: {numeri_set}")


# 4. Quiz sui tipi
# # Scrivi una funzione tipo_collezione(obj) che ritorni la stringa "lista", "tupla", "set" o "dizionario" in base al tipo dell’oggetto passato.

def tipo_collezione(obj):
    if type(obj) == type(list()):
        return "lista"
    elif type(obj) == type(tuple()):
        return "tupla"
    elif type(obj) == type(set()):
        return "set"
    elif type(obj) == type(dict()):
        return "dizionario"
    else:
        return "tipo sconosciuto"
    
# Esempi di utilizzo della funzione
print(tipo_collezione([1, 2, 3]))  # lista
print(tipo_collezione((1, 2, 3)))  # tupla
print(tipo_collezione({1, 2, 3}))  # set
print(tipo_collezione({'a': 1, 'b': 2}))  # dizionario
print(tipo_collezione(42))  # tipo sconosciuto


# LIVELLO 2: Controllo di flusso

# 5. Categorie di voto (if / elif / else)
# # Chiedi all’utente un voto (0-100).
# # Stampa “Insufficiente” (<60), “Sufficiente” (60-69), “Buono” (70-79), “Ottimo” (80-89), “Eccellente” (90-100).

def categoria_voto(voto):
    if 0 <= voto < 60:
        return "Insufficiente"
    elif 60 <= voto < 70:
        return "Sufficiente"
    elif 70 <= voto < 80:
        return "Buono"
    elif 80 <= voto < 90:
        return "Ottimo"
    elif 90 <= voto <= 100:
        return "Eccellente"
    else:
        return "Voto non valido"
    
input_voto = 100 # int(input("Inserisci un voto (0-100): "))
print(categoria_voto(input_voto))


# 6. Tabelline con for e range
# # Usa un ciclo for per stampare la tabellina del 7 da 1 a 10.
# # Estendi l’esercizio per stampare le tabelline da 1 a 10 in un formato a griglia.

print("Tabellina del 7:")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")

print("\nTabelline da 1 a 10 in formato a griglia:")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j:2}", end="\t")
    print()
print()


# 7. Somma dei numeri con while
# # Chiedi all’utente di inserire numeri fino a che non inserisce 0.
# # Stampa la somma e la media dei numeri inseriti (escludendo lo 0 finale).

somma = 0
count = 0

# while True:
#     numero = int(input("Inserisci un numero (0 per terminare): "))
#     if numero == 0:
#         break
#     somma += numero
#     count += 1

if count > 0:
    media = somma / count
    print(f"Somma: {somma}, Media: {media}")
else:
    print("Nessun numero inserito.")
print()


# LIVELLO 3: Insiemi di dati più ricchi

# 8. Analisi di dizionario
# # Crea un dizionario spesa dove i valori sono prezzi.
# # Aggiungi un nuovo prodotto scelto dall’utente.
# # Calcola il costo totale e rimuovi l’articolo più caro.

spesa = {"mele": 3.2, "pane": 1.0, "latte": 1.5}
print(f"Dizionario spesa iniziale: {spesa}")

prodotto = "pasta" #input("Inserisci il nome del prodotto: ")
prezzo = 1 #float(input(f"Inserisci il prezzo di {prodotto}: "))
spesa[prodotto] = prezzo
print(f"Dizionario spesa aggiornato: {spesa}")

costo_totale = sum(spesa.values())
print(f"Costo totale della spesa: {costo_totale:.2f}€")

#prodotto_piu_caro = max(spesa, key=spesa.get) # <- metodo built-in, in alternativa:
prodotto_piu_caro = None
costo_max = max(spesa.values())
for p in spesa.keys():
    if spesa[p] == costo_max:
        prodotto_piu_caro = p
        break
del spesa[prodotto_piu_caro]
print(f"Prodotto più caro rimosso: {prodotto_piu_caro}")
print(f"Dizionario spesa dopo la rimozione: {spesa}")
costo_totale_aggiornato = sum(spesa.values())
print(f"Costo totale aggiornato della spesa: {costo_totale_aggiornato:.2f}€")
print()

# 9. Occorrenze di parole
# # Chiedi all’utente una frase.
# # Restituisci un dizionario con la frequenza di ciascuna parola (ignora maiuscole/minuscole e punteggiatura).
# # Visualizza le 3 parole più comuni in ordine decrescente di frequenza.

frase = "Ciao, ciao! Come va? Va bene, va bene. Ciao a tutti." #input("Inserisci una frase: ")
print(f"Frase inserita: {frase}")
import string
frase = frase.lower().translate(str.maketrans("", "", string.punctuation))
parole = frase.split()

frequenza = dict()
for parola in parole:
    if parola in frequenza:
        frequenza[parola] += 1
    else:
        frequenza[parola] = 1
print(f"Frequenza delle parole: {frequenza}")

da_stampare = 3
print(f"Le {da_stampare} parole più comuni sono:")
for i in range(da_stampare):
    if not frequenza:
        print("Non ci sono più parole da stampare.")
        break
    parola_max = max(frequenza, key=frequenza.get)
    print(f" - {parola_max}:  \t{frequenza[parola_max]}")
    del frequenza[parola_max]


# SFIDA FINALE: 

# 10. Rubrica telefonica
# # Implementa un semplice menu testuale con queste opzioni:
# # 1. Aggiungi contatto (nome → numero)
# # 2. Cerca numero per nome
# # 3. Elenca tutti i contatti ordinati alfabeticamente
# # 4. Elimina un contatto
# # 5. Esci
# # Usa un dizionario per archiviare i dati,  i set per verificare duplicati di nomi, cicli while per mantenere il programma attivo, e una serie di condizioni if per gestire il menu.

rubrica = {}
def mostra_menu():
    print("\nMenu Rubrica Telefonica:")
    print("1. Aggiungi contatto")
    print("2. Cerca numero per nome")
    print("3. Elenca tutti i contatti")
    print("4. Elimina un contatto")
    print("5. Esci")

mostra_menu()

while True:
    scelta = input("\nScegli un'opzione (1-5): ")
    
    if scelta == "1":
        nome = input("Inserisci il nome del contatto: ")
        numero = input("Inserisci il numero di telefono: ")
        if nome in rubrica:
            print(f"Il contatto '{nome}' esiste già con il numero {rubrica[nome]}.")
        else:
            rubrica[nome] = numero
            print(f"Contatto '{nome}' aggiunto con successo.")

    elif scelta == "2":
        nome = input("Inserisci il nome da cercare: ")
        if nome in rubrica:
            print(f"Numero di {nome}: {rubrica[nome]}")
        else:
            print(f"Contatto '{nome}' non trovato.")

    elif scelta == "3":
        if rubrica:
            print("Contatti nella rubrica:")
            for nome in sorted(rubrica):
                print(f"{nome}: {rubrica[nome]}")
        else:
            print("La rubrica è vuota.")

    elif scelta == "4":
        nome = input("Inserisci il nome del contatto da eliminare: ")
        if nome in rubrica:
            del rubrica[nome]
            print(f"Contatto '{nome}' eliminato.")
        else:
            print(f"Contatto '{nome}' non trovato.")

    elif scelta == "5":
        print("Uscita dal programma.")
        break

    else:
        print("Opzione non valida. Riprova.")
        mostra_menu() # così si evita di ripetere il menu ogni volta