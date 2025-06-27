Lista = []


while True:
    try:
        nome = input("Inserisci il nome del viaggio (o 'fine' per terminare): ")
        if nome.lower() == 'fine':
            print(Lista)
            break
        data = input("Inserisci la data del viaggio: ")
        destinazione = input("Inserisci la destinazione del viaggio: ")
        
        # Aggiungi i dati alla lista come dizionario
        Lista.append({
            'Nome': nome,
            'Data': data,
            'Destinazione': destinazione
        })
    except Exception as e:
        print(f"Errore durante l'inserimento dei dati: {e}")
