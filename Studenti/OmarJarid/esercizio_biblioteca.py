class Libro:
    def __init__(self, titolo, autore, disponibile = True):
        self.titolo = titolo
        self.autore = autore
        self.disponibile = disponibile
    
    def presta(self): self.disponibile = False

    def restituisci(self): self.disponibile = True

class Biblioteca:
    def __init__(self):
        self.libri = []

    def aggiungi_libro(self, libro): self.libri.append(libro)

    def prestito(self, titolo):
        for libro in self.libri:
            if libro.titolo == titolo and libro.disponibile:
                libro.presta()
                return True
            
        print("Libro non trovato.\n")
        return False
    
    def restituzione(self, titolo):
        for libro in self.libri:
            if libro.titolo == titolo and not libro.disponibile:
                libro.restituisci()
                return

        print("Il libro non esiste nel nostro archivio.\n")
        return
    
    def elenco_disponibili(self):
        libri_disponibili = []
        for libro in self.libri:
            if libro.disponibile: libri_disponibili.append(libro)
        
        return libri_disponibili
    
    def cerca_per_autore(self, autore):
        libri_autore = []
        for libro in self.libri:
            if libro.autore == autore: libri_autore.append(libro)
        
        return libri_autore

    def conta_libri_prestati(self):
        contatore = 0
        for libro in self.libri:
            if not libro.disponibile: contatore += 1
        return contatore

biblioteca = Biblioteca()
libri = [
    Libro("Il Signore degli Anelli", "J.R.R. Tolkien"),
    Libro("Harry Potter e la Pietra Filosofale", "J.K. Rowling"),
    Libro("Il Trono di Spade", "George R.R. Martin"),
    Libro("La straniera", "Diana Gabaldon"),
    Libro("Design Patterns", "Gang of Four")
]

for libro in libri: biblioteca.aggiungi_libro(libro)

print("Libri disponibili:")
biblioteca.elenco_disponibili()

biblioteca.prestito("Design Patterns")
biblioteca.prestito("La straniera")

print("Libri disponibili dopo prestiti:")
biblioteca.elenco_disponibili()

biblioteca.restituzione("La straniera")

print("Libri disponibili dopo restituzione:")
biblioteca.elenco_disponibili()

autore = input("Inserisci un autore: ")
print(f"Libri di {autore}: ")
for libro in biblioteca.cerca_per_autore(autore): print(f"- '{libro.titolo}'")
print()

print(f"Libri NON disponibili: {biblioteca.conta_libri_prestati()}")