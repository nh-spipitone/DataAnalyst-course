# Esercizio Python: Gestione Biblioteca (OOP & Logica)
# Crea un semplice gestionale per una biblioteca che tiene traccia dei libri e dei prestiti.

class Libro:  # Definizione della classe Libro
    def __init__(self, titolo, autore, disponibile):  # Costruttore della classe
        self.titolo = titolo  # Attributo titolo del libro
        self.autore = autore  # Attributo autore del libro
        self.disponibile = disponibile  # Attributo che indica se il libro è disponibile

    def presta(self):  # Metodo per prestare il libro
        self.disponibile = False  # Imposta disponibile a False (non disponibile)

    def restituisci(self):  # Metodo per restituire il libro
        self.disponibile = True  # Imposta disponibile a True (disponibile)

def mostra_libri_disponibili(libri):  # Funzione per mostrare i libri disponibili
    for libro in libri:  # Cicla su tutti i libri
        if libro.disponibile:  # Se il libro è disponibile
            print(f"Il libro {libro.titolo} dell'autore {libro.autore} è disponibile")  # Stampa info libro

def conta_libri_non_disponibili(libri):  # Funzione per contare i libri non disponibili
    contatore_libri = 0  # Inizializza il contatore a 0
    for libro in libri:  # Cicla su tutti i libri
        if not libro.disponibile:  # Se il libro non è disponibile
            contatore_libri += 1  # Incrementa il contatore
    print(f"Il numero di libri non disponibili è {contatore_libri}")  # Stampa il risultato

# Lista di oggetti Libro con titolo, autore e disponibilità
libri = [
    Libro("Il nome della rosa", "Umberto Eco", True),
    Libro("1984", "George Orwell", True),
    Libro("Orgoglio e pregiudizio", "Jane Austen", False),
    Libro("Il piccolo principe", "Antoine de Saint-Exupéry", True),
    Libro("Moby Dick", "Herman Melville", True)
]

mostra_libri_disponibili(libri)  # Mostra i libri disponibili
libri[3].presta()  # Presta il quarto libro (indice 3)
libri[4].presta()  # Presta il quinto libro (indice 4)

print("___")  # Separatore

mostra_libri_disponibili(libri)  # Mostra i libri disponibili dopo i prestiti
libri[2].restituisci()  # Restituisce il terzo libro (indice 2)

print("___")  # Separatore

mostra_libri_disponibili(libri)  # Mostra i libri disponibili dopo la restituzione

conta_libri_non_disponibili(libri)  # Conta e stampa il numero di libri non disponibili
