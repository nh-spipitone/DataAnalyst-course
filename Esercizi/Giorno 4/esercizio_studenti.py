# Definizione della classe base Scuola
class Scuola:
    # Costruttore che inizializza nome e indirizzo della scuola
    def __init__(self, nome_scuola, indirizzo):
        self.nome_scuola = nome_scuola  # Attributo per il nome della scuola
        self.indirizzo = indirizzo  # Attributo per l'indirizzo della scuola

    # Metodo per mostrare le informazioni della scuola
    def Mostra_Scuola(self):
        print(f"Nome della scuola: {self.nome_scuola}")  # Stampa il nome della scuola
        print(
            f"Indirizzo della scuola: {self.indirizzo}"
        )  # Stampa l'indirizzo della scuola


# Definizione della classe Studente che eredita da Scuola
class Studente(Scuola):

    # Costruttore che accetta nome, voto, scuola e indirizzo
    def __init__(self, nome, voto, scuola, indirizzo_scuola):
        super().__init__(
            scuola, indirizzo_scuola
        )  # Chiama il costruttore della classe padre
        self.nome = nome  # Attributo per il nome dello studente
        self.voto = voto  # Attributo per il voto dello studente

    # Metodo che verifica se lo studente ha superato l'esame (voto >= 18)
    def ha_superato(self) -> bool:
        return self.voto >= 18  # Restituisce True se voto >= 18, False altrimenti


# Definizione della classe Professore che eredita da Scuola
class Professore(Scuola):
    # Costruttore che accetta nome, materia, scuola e indirizzo
    def __init__(self, nome, materia, scuola, indirizzo_scuola):
        super().__init__(
            scuola, indirizzo_scuola
        )  # Chiama il costruttore della classe padre
        self.nome = nome  # Attributo per il nome del professore
        self.materia = materia  # Attributo per la materia insegnata

    # Metodo per mostrare le informazioni del professore
    def Mostra_Professore(self):
        print(f"Nome del professore: {self.nome}")  # Stampa il nome del professore
        print(f"Materia insegnata: {self.materia}")  # Stampa la materia insegnata


# Creazione di una lista con 5 oggetti Studente
listastudenti = [
    Studente(
        "Mario Rossi", 25, "Liceo Scientifico", "Via Roma 1"
    ),  # Studente con voto 25
    Studente(
        "Luca Bianchi", 15, "Liceo Classico", "Via Milano 2"
    ),  # Studente con voto 15
    Studente(
        "Anna Verdi", 30, "Liceo Artistico", "Via Napoli 3"
    ),  # Studente con voto 30
    Studente(
        "Giulia Neri", 20, "Liceo Linguistico", "Via Torino 4"
    ),  # Studente con voto 20
    Studente(
        "Marco Gialli", 10, "Liceo Tecnico", "Via Firenze 5"
    ),  # Studente con voto 10
]
count = 0  # Contatore per gli studenti che non hanno superato l'esame

# Ciclo for per iterare attraverso tutti gli studenti nella lista
for studente in listastudenti:
    # Verifica se lo studente ha superato l'esame
    if studente.ha_superato():
        print(
            f"Lo studente {studente.nome} ha superato l' esame"
        )  # Messaggio per chi ha superato
        studente.Mostra_Scuola()  # Mostra le informazioni della scuola dello studente
    else:
        count += 1  # Incrementa il contatore per chi non ha superato

# Stampa il numero totale di studenti che non hanno superato l'esame
print(f"Il numero di studenti che non hanno superato l'esame è: {count}")

# Creazione di un oggetto Professore
professore = Professore("Dr. Luigi", "Matematica", "Liceo Scientifico", "Via Roma 1")
professore.Mostra_Professore()  # Mostra le informazioni del professore
professore.Mostra_Scuola()  # Mostra le informazioni della scuola del professore
