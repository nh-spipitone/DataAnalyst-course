# #livello1
# #punto1
# temperatura_max = [25, 30, 33, 35, 29]

# media = 0

# for temp in temperatura_max:
#     media += temp

# media = media / len(temperatura_max)

# print(f"la media della temperatura massima della settimana è {media} C°")

# temperatura_max.sort(reverse=True)

# print(f"la temperatura massima della settimana è {temperatura_max} C°")

# #punto2

# tupla_temperatura = tuple(temperatura_max)

# print(f"la tupla delle temperature massime è {tupla_temperatura}")

# # tupla_temperatura [0] = 24 immutabile

# #punto3
# numeri = [3, 5, 3, 7, 5, 9, 3]

# print("lunghezza numeri:", len(numeri))

# numeri_unici = list(set(numeri))    #elimina i duplicati e converte in lista

# numeri_unici.sort(reverse=True)      #ordina i numeri in ordine decrescente

# print(f"nuova lista numeri: {numeri_unici}")

# print("nuova lunghezza numeri:", len(numeri_unici))

# #punto4




#livello2
#punto5
# voto = int(input("digita un voto tra 0 e 100:"))

# if voto < 60:
#     print("insufficiente")

# elif voto < 70 or voto == 60:
#     print("sufficiente")
# elif voto < 80 or voto == 70:
#     print("buono")

# elif voto < 90 or voto == 80:
#     print("ottimo")

# else:
#     print("eccellente")

# print("il voto è:", voto)

# #punto6

tabellina_7 = []

for n in range(1,11):
    riga = ""
    for i in range(1,11):
        tabellina = n * i
        tabellina_7.append(f"7 x {i} = {tabellina}")
        riga += f" {n} x {i} = {tabellina}"
    print(riga)

# #punto8

somma = 0
media = 0
contatore = 0
while True:
    n = float(input("digita un numero oppure usa 0 per terminare:"))
    if n == 0:
        break
    contatore += 1
    somma = somma + n
media = somma /contatore


# numeri = []
# totale = 0
# while True:
#     n = float(input("digita un numero dalla lista oppure 0 per terminare:"))
#     if n == 0:
#         break
#     numeri.append(n)
#     totale += n

# print("somma:", sum(numeri))
# print("somma:", totale)
# print("media:", totale / len(numeri))
# print("media:", sum(numeri) / len(numeri))

    
    
    #esercizio3
    #punto8
    
spesa = {"mele": 3.2, "pane": 1.0, "latte": 1.5}
totale = 0
inserisci_articolo = str(input("inserisci un articolo da aggiungere alla spesa: "))
inserisci_prezzo = float(input("inserisci il suo prezzo:"))
spesa[inserisci_articolo] = inserisci_prezzo
print("lista della spesa aggiunta:", spesa)


for aricolo, prezzo in spesa.items():
    print(f"prezzo: {prezzo} euro")
    totale += prezzo
print(f"totale spesa: {totale} euro")

# totale = 0
# for prezzo in spesa.values():
#     print(f"prezzo : {prezzo} euro")
#     totale += prezzo
# print(f"totale spesa: {totale} euro")


#punto9
print("Benvenuto nella rubrica telefonica !")
rubrica = {}
while True:
    comando = int(input("cosa vuoi fare? \n 1. aggiungi contatto \n2. cerca contatto \n3. elenca tutti i contatti in ordine alfabetico \4. elimina contatto \n5. esci"))
    if comando == 5:
        print("uscita dal programma")
        break
    elif comando == 1:
        nome = input("inserisci nome del contatto:")
        if nome in rubrica:
            print("il contatto esiste già.")
            continue # continua il ciclo sena aggiungere contatto
        numero = int(input("inserisci il numero di telefono:"))
        rubrica [nome] = numero
        print(f"contatto {nome} aggiunto con successo.")
    elif comando == 2:
        nome = input("inserisci il nome del contatto da cercare:")
        if nome in rubrica:
            print(f"il numero di {nome} è: {rubrica [nome]}")
        else:
            print("contatto non trovato")

    elif comando == 3:
        if not rubrica:
            print("la rubrica è vuota")
        else:
            print("elenco contatti in ordine alfabetico")
            for nome in sorted(rubrica):
                print(f"{nome}: {rubrica [nome]}")

    elif comando == 4:
        nome = input("inserisci il nome del contatto da eliminare:")
        if nome in rubrica:
            rubrica.pop(nome)
            print(f"contatto {nome} eliminato con successo")
        else:
            print("contatto eliminato")

    else:
        print("comando non valido riprova")
        



