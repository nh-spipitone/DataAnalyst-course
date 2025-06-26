# #punto 5

# voto = int(input("digita un voto tra 0 e 100: "))

# if voto <60:
#     print("insufficente")
# elif voto <= 69:
#     print("sufficiente")
# elif voto <= 79:
#     print("buono")
# elif voto <= 89:
#     print("ottimo")
# else:
#     print("eccellente")

# print("il voto è:", voto)

# punto 6

tabellina_del_7 = []

for n in range(1, 11):
    riga = ""
    for i in range(1, 11):
        tabellina = n * i
        tabellina_del_7.append(f"7x{i}={tabellina}")
        riga += f"{n}x{i}={tabellina} "
    print(riga)

somma = 0
media = 0
contatore = 0
while True:
    n = float(input("digita un numero o usa 0 per terminare:"))
    if n == 0:
        break
    contatore += 1
    somma = somma + n
media = somma / contatore


# numeri = []  # Inizializza una lista vuota per memorizzare i numeri inseriti
# totale = 0  # Inizializza la variabile per calcolare la somma manualmente

# while True:  # Ciclo infinito che continua finché non viene interrotto
#     n = float(
#         input("digita un numero o usa 0 per terminare: ")
#     )  # Chiede all'utente di inserire un numero
#     if n == 0:  # Controlla se l'utente ha inserito 0 per terminare
#         break  # Esce dal ciclo
#     numeri.append(n)  # Aggiunge il numero alla lista
#     totale += n  # Aggiunge il numero al totale manuale

# print("somma:", sum(numeri))  # Stampa la somma usando la funzione built-in sum()
# print("somma:", totale)  # Stampa la somma calcolata manualmente
# print("media:", totale / len(numeri))  # Stampa la media usando il totale manuale
# print("media:", sum(numeri) / len(numeri))  # Stampa la media usando la funzione sum()


spesa = {"mele": 3.2, "pane": 1.0, "latte": 1.5}
totale = 0
inserisci_articolo = str(input("Inserisci un articolo da aggiungere alla spesa: "))
inserisci_prezzo = float(input("Inserisci il suo prezzo: "))
spesa[inserisci_articolo] = inserisci_prezzo

print("Lista della spesa aggiornata: ", spesa)


for articolo, prezzo in spesa.items():
    print(f"{articolo}: {prezzo} euro")
    totale += prezzo
print(f"Totale spesa: {totale} euro")


# totale = 0
# for prezzo in spesa.values():
#     print(f"Prezzo: {prezzo} euro")
#     totale += prezzo
# print(f"Totale spesa: {totale} euro")


print("Benvenuto nella rubrica telefonica!")  # Stampa il messaggio di benvenuto
rubrica = {}  # Inizializza un dizionario vuoto per memorizzare i contatti
while True:  # Ciclo infinito per il menu principale
    comando = int(  # Converte l'input dell'utente in intero
        input(
            "Cosa vuoi fare?\n1. Aggiungi contatto\n2. Cerca numero per nome\n3 Elenca tutti i contatti in ordine alfabetico\n4. Elimina un contatto\n5. Esci"
        )  # Mostra il menu delle opzioni disponibili
    )
    if comando == 5:  # Se l'utente sceglie l'opzione 5 (Esci)
        print("Uscita dal programma.")  # Stampa il messaggio di uscita
        break  # Esce dal ciclo principale
    elif comando == 1:  # Se l'utente sceglie l'opzione 1 (Aggiungi contatto)
        nome = input("Inserisci il nome del contatto: ")  # Chiede il nome del contatto
        if nome in rubrica:  # Controlla se il contatto esiste già
            print("Il contatto esiste già.")  # Informa che il contatto è già presente
            continue  # Continua il ciclo senza aggiungere il contatto
        numero = int(
            input("Inserisci il numero di telefono: ")
        )  # Chiede il numero di telefono
        rubrica[nome] = numero  # Aggiunge il contatto al dizionario
        print(f"Contatto {nome} aggiunto con successo.")  # Conferma l'aggiunta
    elif comando == 2:  # Se l'utente sceglie l'opzione 2 (Cerca numero)
        nome = input(
            "Inserisci il nome del contatto da cercare: "
        )  # Chiede il nome da cercare
        if nome in rubrica:  # Controlla se il contatto esiste
            print(f"Il numero di {nome} è: {rubrica[nome]}")  # Mostra il numero trovato
        else:
            print("Contatto non trovato.")  # Informa che il contatto non esiste
    elif comando == 3:  # Se l'utente sceglie l'opzione 3 (Elenca contatti)
        if not rubrica:  # Controlla se la rubrica è vuota
            print("La rubrica è vuota.")  # Informa che non ci sono contatti
        else:
            print("Contatti in ordine alfabetico:")  # Intestazione per la lista
            for nome in sorted(rubrica):  # Itera sui nomi ordinati alfabeticamente
                print(
                    f"{nome}: {rubrica[nome]}"
                )  # Stampa ogni contatto con il suo numero
    elif comando == 4:  # Se l'utente sceglie l'opzione 4 (Elimina contatto)
        nome = input(
            "Inserisci il nome del contatto da eliminare: "
        )  # Chiede il nome da eliminare
        if nome in rubrica:  # Controlla se il contatto esiste
            rubrica.pop(nome)  # Rimuove il contatto dal dizionario
            print(f"Contatto {nome} eliminato con successo.")  # Conferma l'eliminazione
        else:
            print("Contatto non trovato.")  # Informa che il contatto non esiste
    else:
        print("Comando non valido. Riprova.")  # Gestisce input non validi
