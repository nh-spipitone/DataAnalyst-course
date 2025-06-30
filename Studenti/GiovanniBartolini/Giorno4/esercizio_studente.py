# Scrivi una classe Studente che rappresenta uno studente con i seguenti attributi:

# nome (stringa)
# voto (intero)
# La classe deve avere un metodo:

# ha_superato() che restituisce True se il voto è maggiore o uguale a 18, altrimenti False.

class Scuola:
    def __init__(self, nome_scuola, indirizzo):
        self.nome_scuola = nome_scuola
        self.indirizzo = indirizzo

    def Mostra_Scuola(self):
        print(f"Scuola: {self.nome_scuola}, Indirizzo: {self.indirizzo}")


class Studente(Scuola):

    def __init__(self, nome, voto, scuola, indirizzo):
        super().__init__(scuola, indirizzo)
        self.nome = nome
        self.voto = voto

    def ha_superato(self) -> bool:
        return self.voto >= 18


class Professore(Scuola):
    def __init__(self, nome, materia, scuola, indirizzo):
        super().__init__(scuola, indirizzo)
        self.nome = nome
        self.materia = materia

    def Mostra(self):
        print(f"Nome Professore: {self.nome}, Materia: {self.materia}")


# Consegna:
# Crea una lista di almeno 5 studenti con nomi e voti a tua scelta.
# Stampa il nome di tutti gli studenti che hanno superato l’esame (voto >= 18).
# Conta quanti studenti non hanno superato l’esame e stampa il risultato.

if __name__ == "__main__":
    studenti = [
        Studente("Alice", 30, "Liceo Scientifico", "Via Roma 1"),
        Studente("Marco", 15, "Liceo Classico", "Via Milano 2"),
        Studente("Giulia", 20, "Istituto Tecnico", "Via Napoli 3"),
        Studente("Luca", 10, "Liceo Artistico", "Via Torino 4"),
        Studente("Sara", 25, "Istituto Professionale", "Via Firenze 5")
    ]

    print("Studenti che hanno superato l'esame:")
    studenti_bocciati = 0
    for studente in studenti:
        if studente.ha_superato():
            print(f"- {studente.nome} dalla scuola", end= " ")
            studente.Mostra_Scuola()
        else:
            studenti_bocciati += 1

    print(f"Numero di studenti che non hanno superato l'esame: {studenti_bocciati}")

