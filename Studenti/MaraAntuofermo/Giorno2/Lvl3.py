#Livello 3 
#Punto 8

spesa = {"mele": 3.2, "pane": 1.0, "latte": 1.5}
totale = 0

inserisci_articolo = str(input("Inserisci nuovo articolo: "))
inserisci_prezzo = float(input("Inserisci il prezzo: "))
spesa[inserisci_articolo] = inserisci_prezzo

for articolo, prezzo in spesa.items():
    print(f"{articolo}: {prezzo} euro")
    totale += prezzo

#Aleternativa 
#for prezzo in spesa.values():
    #print(f"Prezzo: {prezzo} euro")
    #totale += prezzo



#Punto 10

print("Benvenuto nella rubrica telefonica!")
rubrica = {}

while True:
    comando = int(input("Cosa vuoi fare? \n1. Aggiungi un contatto \n2. Cerca numero per nome \n3. Elenca tutti i contatti ordinati alfabeticamente \n4. Elimina un contatto \n5. Esci\n \n Digita qui"))
    if comando == 5:
        print("Uscita dal programma.")
        break #Esce dal ciclo
    elif comando == 1:
        nome = input("Inserisci il nome del contatto: ")
        if nome in rubrica:
            print("Il contatto esiste già.")
            continue #Continua il ciclo senza aggiungere il contatto
            continua = input("Vuoi aggiornare il numero? (s/n): ")
        numero = int(input("Inserisci il numero di telefono: "))
        rubrica[nome] = numero
        print(f"Contatto {nome} aggiunto con successo.")
    elif comando == 2:
        nome = input("Inserisci il nome del contatto da cercare: ")
        if nome in rubrica:
            print(f"Il numero di {nome} è: {rubrica[nome]}")
        else:
            print("Contatto non trovato.")

    elif comando == 3:
        if not rubrica:
            print("La rubrica è vuota.")
        else:
            print("Contatti in ordine alfabetico:")
            for nome in sorted(rubrica):
                print(f"{nome}: {rubrica[nome]}")
    
    elif comando == 4:
        nome = input("Inserisci il nome del contatto da eliminare: ")
        if nome in rubrica:
            rubrica.pop(nome)
            print(f"Contatto {nome} eliminato con successo.")
        else:
            print("Contatto non trovato.")

    else:
        print("Comando non valido. Riprova.")
    

    

