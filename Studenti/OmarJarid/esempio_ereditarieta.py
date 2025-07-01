class Animale:
    def __init__(self, nome, specie, eta, peso):
        self.nome = nome
        self.specie = specie
        self.eta = eta
        self.peso = peso

    def mostra_informazioni(self):
        print(f"Nome: {self.nome}")
        print(f"Specie: {self.specie}")
        print(f"Eta: {self.eta}")
        print(f"Peso: {self.peso}")

class Cane(Animale):
    def __init__(self, nome, specie, eta, peso, razza):
        super().__init__(nome, specie, eta, peso)
        self.razza = razza

    def abbaia(self): print(f"{self.nome} abbaia")

    def mostra_informazioni(self):
        super().mostra_informazioni()
        print(f"Razza: {self.razza}")

class Gatto(Animale):
    def __init__(self, nome, specie, eta, peso, razza):
        super().__init__(nome, specie, eta, peso)
        self.razza = razza

    def miagola(self): print(f"{self.nome} miagola")

    def mostra_informazioni(self):
        super().mostra_informazioni()
        print(f"Razza: {self.razza}")

mio_cane = Cane("Fido", "Labrador", 3, 30, "Golden Retriever")
mio_cane.abbaia()
mio_cane.mostra_informazioni()

mio_gatto = Gatto("Miau", "Persa", 2, 3, "Persa")
mio_gatto.miagola()
mio_gatto.mostra_informazioni()