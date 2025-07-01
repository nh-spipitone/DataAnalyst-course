


class Biblioteca:
    def __init__(self, libri):
        self.libri = libri

    def aggiungi_libro(self, libro):
        self.libri.append(libro)

    def prestito(self, titolo):
        for libro in self.libri:
            if titolo == libro.titolo:
                if libro.disponibile:
                    libro.presta()
                    return True
                return False

    def restituzione(self,titolo):
        for libro in self.libri:
            if titolo == libro.titolo:
                if libro.disponibile:
                    libro.restituisci()


    def elenco_disponibili(self):
        libri_disponibili = []
        for libro in self.libri:
            if libro.disponibile:
                libri_disponibili.append(str(libro))
        return libri_disponibili

    def cerca_per_autore(self, autore):
        libri_autore = []
        for libro in self.libri:
            if autore == libro.autore:
                libri_autore.append(libro)
        return libri_autore
        


class Libro:  
    def __init__(self, titolo, autore, disponibile):  
        self.titolo = titolo  
        self.autore = autore  
        self.disponibile = disponibile  

    def presta(self):  
        self.disponibile = False  

    def restituisci(self):  
        self.disponibile = True  

    def __str__(self):
        return f"titolo: {self.titolo} autore: {self.autore} disponibile: {self.disponibile}"

def mostra_libri_disponibili(libri):  
    for libro in libri:  
        if libro.disponibile:  
            print(f"Il libro {libro.titolo} dell'autore {libro.autore} è disponibile")  

def conta_libri_non_disponibili(libri):  
    contatore_libri = 0  
    for libro in libri:  
        if not libro.disponibile:  
            contatore_libri += 1  
    print(f"Il numero di libri non disponibili è {contatore_libri}")  


# libri = [
#     Libro("Il nome della rosa", "Umberto Eco", True),
#     Libro("1984", "George Orwell", True),
#     Libro("Orgoglio e pregiudizio", "Jane Austen", False),
#     Libro("Il piccolo principe", "Antoine de Saint-Exupéry", True),
#     Libro("Moby Dick", "Herman Melville", True)
# ]

# mostra_libri_disponibili(libri)  
# libri[3].presta()  
# libri[4].presta()  

# print("___")  

# mostra_libri_disponibili(libri)  
# libri[2].restituisci()  
# print("___")  

# mostra_libri_disponibili(libri)  

# conta_libri_non_disponibili(libri) 


biblioteca = Biblioteca( libri = [    
    Libro("Il nome della rosa", "Umberto Eco", True),
    Libro("1984", "George Orwell", True),
    Libro("Orgoglio e pregiudizio", "Jane Austen", False),
    Libro("Il piccolo principe", "Antoine de Saint-Exupéry", True),
    Libro("Moby Dick", "Herman Melville", True)
    ]) 

biblioteca.aggiungi_libro(Libro("Il nome della rosa", "Umberto Eco", True))
print(biblioteca.elenco_disponibili())

print("__")

biblioteca.prestito( Libro("il piccolo principe", "Antoine de Saint-Exupéry", True))

biblioteca.restituzione("il piccolo principe")
print("elenco disponibili:")
print(biblioteca.elenco_disponibili)

print("___")

print("elenco per autore:")



