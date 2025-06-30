# Esercizio Python: Gestione Biblioteca (OOP & Logica)

# Devi creare un semplice gestionale per una biblioteca che tiene traccia dei libri e dei prestiti.

# Crea una classe Libro con:
# Attributi: titolo (stringa), autore (stringa), disponibile (booleano, di default True)
# Metodo: presta() che imposta disponibile a False.
# Metodo: restituisci() che imposta disponibile a True.

class Libro:
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
        self.__disponibile = True

    def presta(self):
        if self.__disponibile:
            self.__disponibile = False
            print(f"Il libro '{self.titolo}' è stato prestato.")
        else:
            print(f"Il libro '{self.titolo}' non è disponibile per il prestito.")

    def restituisci(self):
        self.__disponibile = True
        print(f"Il libro '{self.titolo}' è stato restituito.")

    def is_disponibile(self):
        return self.__disponibile

    def mostra_info(self):
        stato = "disponibile" if self.__disponibile else "prestato"
        print(f"Titolo: {self.titolo}, Autore: {self.autore}, Stato: {stato}")

    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}"

class Biblioteca:
    def __init__(self):
        self.libri = []
        self.__prestati = []

    def aggiungi_lista_libri(self, lista_libri):
        self.libri.extend(lista_libri)

    def mostra_libri(self):
        for libro in self.libri:
            libro.mostra_info()

    def presta_libro(self, titolo):
        for libro in self.libri:
            if libro.titolo == titolo:
                if libro.is_disponibile():
                    self.__prestati.append(libro)
                libro.presta()
                return
        print(f"Il libro '{titolo}' non esiste nella biblioteca.")
            
    def restituisci_libro(self, titolo):
        for libro in self.__prestati:
            if libro.titolo == titolo:
                libro.restituisci()
                self.__prestati.remove(libro)
                return
        if titolo in [libro.titolo for libro in self.libri]:
            print(f"Il libro '{titolo}' non è stato prestato.")
        else:
            print(f"Il libro '{titolo}' non esiste nella biblioteca.")

    def conta_libri_non_disponibili(self):
        return len(self.__prestati)
            
    def mostra_libri_disponibili(self):
        for libro in self.libri:
            if libro.is_disponibile():
                print(libro)
        if len(self.__prestati) > 0:
            print("Totale libri prestati:", len(self.__prestati))

    def mostra_libri_prestati(self):
        if len(self.__prestati) == 0:
            print("Nessun libro è attualmente prestato.")
        else:
            print("Libri attualmente prestati:")
            for libro in self.__prestati:
                print(libro)

# Nel programma principale, crea una lista di almeno 5 libri diversi (titolo e autore a piacere).
# Stampa tutti i libri disponibili, indicando titolo e autore.
# Simula il prestito di due libri a scelta chiamando il metodo .presta() sugli oggetti corrispondenti.
# Stampa nuovamente la lista dei libri disponibili (devono essere diminuiti di due).
# Simula la restituzione di uno dei libri prestati, poi stampa di nuovo la lista dei disponibili.
# Conta e stampa quanti libri NON sono disponibili.

## Prima versione del codice, senza la classe Biblioteca
# if __name__ == "__main__":
#     # Creazione di una lista di libri
#     biblioteca = [
#         Libro("Il Signore degli Anelli", "J.R.R. Tolkien"),
#         Libro("1984", "George Orwell"),
#         Libro("Il Codice Da Vinci", "Dan Brown"),
#         Libro("Harry Potter e la Pietra Filosofale", "J.K. Rowling"),
#         Libro("Il Grande Gatsby", "F. Scott Fitzgerald"),
#         Libro("Orgoglio e Pregiudizio", "Jane Austen"),
#         Libro("Moby Dick", "Herman Melville"),
#         Libro("Il Nome della Rosa", "Umberto Eco"),
#         Libro("La Divina Commedia", "Dante Alighieri"),
#     ]

    # non_disponibili = 0
    # # Stampa dei libri disponibili
    # print("Libri disponibili:")
    # for libro in biblioteca:
    #     if libro.is_disponibile():
    #         libro.mostra_info()
    #     else:
    #         non_disponibili += 1


    # # Simulazione del prestito di due libri
    # print("\nPrestito di due libri:")
    # biblioteca[0].presta()  # Prestito di "Il Signore degli Anelli"
    # biblioteca[2].presta()  # Prestito di "Il Codice Da Vinci"

    # # Stampa dei libri disponibili dopo il prestito
    # print("\nLibri disponibili dopo il prestito:")
    # for libro in biblioteca:
    #     libro.mostra_info()
        
    # # Simulazione della restituzione di un libro
    # print("\nRestituzione di un libro:")
    # biblioteca[0].restituisci() # Restituzione di "Il Signore degli Anelli"

    # # Stampa dei libri disponibili dopo la restituzione
    # print("\nLibri disponibili dopo la restituzione:")
    # for libro in biblioteca:
    #     libro.mostra_info()

    # # Conteggio dei libri non disponibili
    # non_disponibili = sum(1 for libro in biblioteca if not libro._Libro__disponibile)
    # print(f"\nNumero di libri non disponibili: {non_disponibili}")


# Programma principale con la classe Biblioteca
if __name__ == "__main__":
    # Creazione di una lista di libri
    lista_libri = [
        Libro("Il Signore degli Anelli", "J.R.R. Tolkien"),
        Libro("1984", "George Orwell"),
        Libro("Il Codice Da Vinci", "Dan Brown"),
        Libro("Harry Potter e la Pietra Filosofale", "J.K. Rowling"),
        Libro("Il Grande Gatsby", "F. Scott Fitzgerald"),
        Libro("Orgoglio e Pregiudizio", "Jane Austen"),
        Libro("Moby Dick", "Herman Melville"),
        Libro("Il Nome della Rosa", "Umberto Eco"),
        Libro("La Divina Commedia", "Dante Alighieri"),
    ]

    # Creazione della biblioteca e aggiunta dei libri
    biblioteca = Biblioteca()
    biblioteca.aggiungi_lista_libri(lista_libri)

    # Stampa dei libri disponibili
    print("Libri disponibili:")
    biblioteca.mostra_libri_disponibili()

    # Simulazione del prestito di due libri
    print("\nPrestito di libri:")
    biblioteca.presta_libro("Il Signore degli Anelli")  # Prestito di "Il Signore degli Anelli"
    biblioteca.presta_libro("Il Codice Da Vinci")  # Prestito di "Il Codice Da Vinci"
    biblioteca.presta_libro("Se una notte d'inverno un viaggiatore")  # Tentativo di prestito di un libro non presente
    biblioteca.presta_libro("Il Signore degli Anelli")  # Tentativo di prestito di un libro già prestato

    # Stampa dei libri disponibili dopo il prestito
    print("\nLibri disponibili dopo il prestito:")
    biblioteca.mostra_libri_disponibili()
    # Stampa dei libri prestati
    biblioteca.mostra_libri_prestati()

    # Simulazione della restituzione di un libro
    print("\nRestituzione di libri:")
    biblioteca.restituisci_libro("Il Signore degli Anelli")  # Restituzione di "Il Signore degli Anelli"
    biblioteca.restituisci_libro("Il Grande Gatsby")  # Restituzione di "Il Grande Gatsby" (non prestato)
    biblioteca.restituisci_libro("Se una notte d'inverno un viaggiatore")  # Tentativo di restituzione di un libro non presente

    # Stampa dei libri disponibili dopo la restituzione
    print("\nLibri disponibili dopo la restituzione:")
    biblioteca.mostra_libri_disponibili()
    biblioteca.mostra_libri_prestati()

