class Scuola:
    def __init__(self, nome_scuola, indirizzo):
        self.nome_scuola = nome_scuola
        self.indirizzo = indirizzo

        def mostra_scuola(self):
            print(f"Nome della scuola: {self.nome_scuola}")
            print(f"Indirizzo della scuola: {self.indirizzo}")

class Studente:
    def __init__(self, nome, voto):
        self.nome = nome
        self.voto = voto

    def ha_superato(self) -> bool: return self.voto >= 18

class Professore(Scuola):
    def __init__(self, nome, indirizzo, materia):
        super().__init__(nome, indirizzo)
        self.materia = materia
        self.nome = nome

        def mostra_professore(self):
            print(f"Nome del professore: {self.nome}")
            print(f"Materia: {self.materia}")

studenti = [
    Studente("Omar", 20),
    Studente("Aldo", 16),
    Studente("Giovanni", 19),
    Studente("Giacomo", 17),
    Studente("Giuseppe", 18),
    Studente("Andrea", 19),
    Studente("Giorgio", 17),
    Studente("Domenico", 16),
]

bocciati = 0

print("Studenti che hanno superato l'esame: ")
for studente in studenti:
    if studente.ha_superato():
        print(f"- {studente.nome}")
    else:
        bocciati += 1

print(f"Numero di studenti che non hanno superato l'esame: {bocciati}")