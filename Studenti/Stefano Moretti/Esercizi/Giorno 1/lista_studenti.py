class gestionale_scuola:
    def __init__(self):
        gestionale_studenti()



def gestionale_studenti():
    print("Benvenuto nel gestore di studenti!")
    studenti = []
    x = True
    while x:
        try:
            comando = str(input("Cosa vuoi fare? Digita un numero per:\n1. Aggiungere uno studente\n2. Visualizzare gli studenti\n3. Rimuovere uno studente\n4. Svuotare la lista\n5. Uscire\n"))
            if comando == "1":
                studente = str(input("Inserisci il nome dello studente: "))
                studenti.append(studente)
                if not studente.strip():
                    raise ValueError("Il nome dello studente non può essere vuoto.")
                print(f"Studente '{studenti[-1]}' aggiunto con successo!")
            elif comando == "2":
                print(f"Lista degli studenti: {studenti}")
            elif comando == "3":
                if not studenti:
                    print("La lista degli studenti è vuota. Non posso rimuovere uno studente.")
                else:
                    studente_rimosso = str(input("Inserisci il nome dello studente da rimuovere: "))
                    if studente_rimosso in studenti:
                        studenti.remove(studente_rimosso)
                        print(f"Studente '{studente_rimosso}' rimosso con successo!")
                    else:
                        print(f"Studente '{studente_rimosso}' non trovato nella lista.")
            elif comando == "4":
                studenti.clear()
                print("Lista degli studenti svuotata con successo!")
            elif comando == "5":
                print("Arrivederci!")
                x = False
        except ValueError as e:
            print(f"Errore: {e}. Per favore, inserisci un valore valido.")
            continue
            
if __name__ == "__main__":
    gestionale_scuola()

