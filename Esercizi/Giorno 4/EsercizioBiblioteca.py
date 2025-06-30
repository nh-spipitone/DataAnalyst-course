# Esercizio Python: Gestione Biblioteca (OOP & Logica)
# Crea un semplice gestionale per una biblioteca che tiene traccia dei libri e dei prestiti.


class Biblioteca:  # Definizione della classe Biblioteca
    def __init__(self, libri):  # Costruttore della classe, riceve una lista di libri
        self.libri = libri  # Attributo che contiene la lista dei libri

    def aggiungi_libro(self, libro):  # Metodo per aggiungere un libro alla biblioteca
        self.libri.append(libro)  # Aggiunge il libro alla lista dei libri

    def prestito(self, titolo):  # Metodo per prestare un libro dato il titolo

        for libro in self.libri:  # Cicla su tutti i libri della biblioteca
            if titolo == libro.titolo:  # Se il titolo corrisponde
                if libro.disponibile:  # Se il libro è disponibile
                    libro.presta()  # Presta il libro (imposta disponibile a False)
                    return True  # Restituisce True se il prestito è avvenuto
                return False  # Restituisce False se il libro non è disponibile
        print("Il libro non esiste!")  # Messaggio se il libro non è trovato
        return False  # Restituisce False se il libro non esiste

    def restituzione(self, titolo):  # Metodo per restituire un libro dato il titolo
        for libro in self.libri:  # Cicla su tutti i libri
            if titolo == libro.titolo:  # Se il titolo corrisponde
                if (
                    not libro.disponibile
                ):  # Se il libro non è disponibile (quindi in prestito)
                    libro.restituisci()  # Restituisce il libro (imposta disponibile a True)
                    return True  # Restituisce True se la restituzione è avvenuta
                return False  # Restituisce False se il libro era già disponibile
        print("Il libro non esiste!")  # Messaggio se il libro non è trovato
        return False  # Restituisce False se il libro non esiste

    def elenco_disponibili(self):  # Metodo per ottenere la lista dei libri disponibili
        libri_disponibili = []  # Lista vuota per i libri disponibili
        for libro in self.libri:  # Cicla su tutti i libri
            if libro.disponibile:  # Se il libro è disponibile
                libri_disponibili.append(
                    str(libro)
                )  # Aggiunge la rappresentazione testuale del libro
        return libri_disponibili  # Restituisce la lista dei libri disponibili

    def cerca_per_autore(self, autore):  # Metodo per cercare libri di un certo autore
        libri_autore = []  # Lista vuota per i libri dell'autore
        for libro in self.libri:  # Cicla su tutti i libri
            if autore == libro.autore:  # Se l'autore corrisponde
                libri_autore.append(
                    str(libro)
                )  # Aggiunge la rappresentazione testuale del libro
        return libri_autore  # Restituisce la lista dei libri dell'autore


class Libro:  # Definizione della classe Libro
    def __init__(self, titolo, autore, disponibile):  # Costruttore della classe
        self.titolo = titolo  # Attributo titolo del libro
        self.autore = autore  # Attributo autore del libro
        self.disponibile = disponibile  # Attributo che indica se il libro è disponibile

    def presta(self):  # Metodo per prestare il libro
        self.disponibile = False  # Imposta disponibile a False (non disponibile)

    def restituisci(self):  # Metodo per restituire il libro
        self.disponibile = True  # Imposta disponibile a True (disponibile)

    def __str__(self):  # Metodo per la rappresentazione testuale del libro
        return (
            f"Titolo:{self.titolo} Autore:{self.autore} Disponibile:{self.disponibile}"
        )


# def mostra_libri_disponibili(libri):  # Funzione per mostrare i libri disponibili
#     for libro in libri:  # Cicla su tutti i libri
#         if libro.disponibile:  # Se il libro è disponibile
#             print(f"Il libro {libro.titolo} dell'autore {libro.autore} è disponibile")  # Stampa info libro

# def conta_libri_non_disponibili(libri):  # Funzione per contare i libri non disponibili
#     contatore_libri = 0  # Inizializza il contatore a 0
#     for libro in libri:  # Cicla su tutti i libri
#         if not libro.disponibile:  # Se il libro non è disponibile
#             contatore_libri += 1  # Incrementa il contatore
#     print(f"Il numero di libri non disponibili è {contatore_libri}")  # Stampa il risultato

# # Lista di oggetti Libro con titolo, autore e disponibilità
#  libri = [
#      Libro("Il nome della rosa", "Umberto Eco", True),
#      Libro("1984", "George Orwell", True),
#      Libro("Orgoglio e pregiudizio", "Jane Austen", False),
#      Libro("Il piccolo principe", "Antoine de Saint-Exupéry", True),
#      Libro("Moby Dick", "Herman Melville", True)
#  ]

# mostra_libri_disponibili(libri)  # Mostra i libri disponibili
# libri[3].presta()  # Presta il quarto libro (indice 3)
# libri[4].presta()  # Presta il quinto libro (indice 4)

# print("___")  # Separatore

# mostra_libri_disponibili(libri)  # Mostra i libri disponibili dopo i prestiti
# libri[2].restituisci()  # Restituisce il terzo libro (indice 2)

# print("___")  # Separatore

# mostra_libri_disponibili(libri)  # Mostra i libri disponibili dopo la restituzione

# conta_libri_non_disponibili(libri)  # Conta e stampa il numero di libri non disponibili

# Crea un oggetto Biblioteca con una lista iniziale di libri
biblioteca = Biblioteca(
    libri=[
        Libro("Il nome della rosa", "Umberto Eco", True),  # Libro disponibile
        Libro("1984", "George Orwell", True),  # Libro disponibile
        Libro("Orgoglio e pregiudizio", "Jane Austen", False),  # Libro non disponibile
        Libro(
            "Il piccolo principe", "Antoine de Saint-Exupéry", True
        ),  # Libro disponibile
        Libro("Moby Dick", "Herman Melville", True),  # Libro disponibile
    ]
)

biblioteca.aggiungi_libro(
    Libro("Il nome della rosa2", "Umberto Eco", True)
)  # Aggiunge un nuovo libro
print("Elenco disponibili:")  # Stampa intestazione
print(biblioteca.elenco_disponibili())  # Stampa la lista dei libri disponibili

print("-----------------------")  # Separatore

biblioteca.prestito("Il piccolo principe")  # Presta il libro "Il piccolo principe"
print("Elenco disponibili:")  # Stampa intestazione
print(
    biblioteca.elenco_disponibili()
)  # Stampa la lista aggiornata dei libri disponibili

print("-----------------------")  # Separatore

biblioteca.restituzione(
    "Il piccolo principe"
)  # Restituisce il libro "Il piccolo principe"
print("Elenco disponibili:")  # Stampa intestazione
print(
    biblioteca.elenco_disponibili()
)  # Stampa la lista aggiornata dei libri disponibili

print("-----------------------")  # Separatore

print("Elenco per autore:")  # Stampa intestazione
print(
    biblioteca.cerca_per_autore("Umberto Eco")
)  # Stampa la lista dei libri di Umberto Eco
