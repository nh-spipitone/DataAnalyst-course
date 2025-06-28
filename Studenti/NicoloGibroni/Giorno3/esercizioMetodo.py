class Animale:
    def __init__(self, tipo, verso):
        self.tipo = tipo
        self.verso = verso

    def suono(self):
        print(f"Sono un {self.tipo} e faccio: {self.verso}")

animale = Animale("Gorillone", "wowowowowow")
animale.suono()