class Animale:
    def __init__(self, nome, specie, eta, peso):
        self.nome = nome
        self.specie = specie
        self.eta = eta
        self.peso = peso

    def mostra_informazioni(self):
        print(f"Nome: {self.nome}")
        print(f"Specie: {self.specie}")
        print(f"Età: {self.eta} anni")
        print(f"Peso: {self.peso} kg")

class Cane(Animale):
    def __init__(self, nome, eta, peso, razza):
        super().__init__(nome, "Cane", eta, peso)
        self.razza = razza

    def mostra_informazioni(self):
        super().mostra_informazioni()
        print(f"Razza: {self.razza}")

    def abbaia(self):
        print(f"{self.nome} abbaia: Woof! Woof!")

class Gatto(Animale):
    def __init__(self, nome, eta, peso, colore):
        super().__init__(nome, "Gatto", eta, peso)
        self.colore = colore

    def mostra_informazioni(self):
        super().mostra_informazioni()
        print(f"Colore: {self.colore}")

    def miagola(self):
        print(f"{self.nome} miagola: Meow!")

lola = Gatto("Lola", 3, 4.5, "Nero e Arancio")
baloo = Cane("Baloo", 5, 20.0, "Golden Retriever")

baloo.mostra_informazioni()
baloo.abbaia()

lola.mostra_informazioni()
lola.miagola()