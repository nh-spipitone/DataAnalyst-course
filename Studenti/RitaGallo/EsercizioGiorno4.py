
class Libro:  
    def __init__(self, titolo, autore, disponibile):  
        self.titolo = titolo  
        self.autore = autore  
        self.disponibile = disponibile  

    def presta(self):  
        self.disponibile = False  

    def restituisci(self):  
        self.disponibile = True  

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


libri = [
    Libro("Il nome della rosa", "Umberto Eco", True),
    Libro("1984", "George Orwell", True),
    Libro("Orgoglio e pregiudizio", "Jane Austen", False),
    Libro("Il piccolo principe", "Antoine de Saint-Exupéry", True),
    Libro("Moby Dick", "Herman Melville", True)
]

mostra_libri_disponibili(libri)  
libri[3].presta()  
libri[4].presta()  

print("___")  

mostra_libri_disponibili(libri)  
libri[2].restituisci()  
print("___")  

mostra_libri_disponibili(libri)  

conta_libri_non_disponibili(libri) 



