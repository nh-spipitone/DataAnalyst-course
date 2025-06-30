class Motore:
    def __init__(self, tipo, potenza):
        self.tipo = tipo
        self.potenza = potenza
        self.__avviato = False

    def avvia_motore(self):
        print(f"Avvio motore {self.tipo} con potenza {self.potenza} CV.")
        self.__avviato = True

    def spegni_motore(self):
        print(f"Spegni motore {self.tipo}.")
        self.__avviato = False
        
    def stato_motore(self):
        return "Avviato" if self.__avviato else "Spento"

class Radio:
    def __init__(self, marca, modello, max_volume=100):
        self.marca = marca
        self.modello = modello
        self.max_volume = max_volume
        self.__volume = 0

    def accendi_radio(self):
        print(f"Accensione radio {self.marca} {self.modello}.")
        self.__volume = 10
    
    def spegni_radio(self):
        print(f"Spegni radio {self.marca} {self.modello}.")
        self.__volume = 0

    def aumenta_volume(self):
        if self.__volume < self.max_volume:
            self.__volume += 1
            print(f"Volume aumentato a {self.__volume}.")
        else:
            print("Volume gia al massimo.")

    def diminuisci_volume(self):
        if self.__volume > 0:
            self.__volume -= 1
            print(f"Volume diminuito a {self.__volume}.")
        else:
            print("Volume gia al minimo.")
            
    def stato_volume(self):
        return f"Volume attuale: {self.__volume}."


class Macchina:
    def __init__(self, marca, modello, anno, motore: Motore, radio: Radio):
        self.motore = motore
        self.radio = radio
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def accendi_auto(self):
        print(f"Accensione auto {self.marca} {self.modello} del {self.anno}.")
        self.motore.avvia_motore()
        self.radio.accendi_radio()

    def spegni_auto(self):
        print(f"Spegni auto {self.marca} {self.modello}.")
        self.motore.spegni_motore()
        self.radio.spegni_radio()

    def accelera(self):
        if self.motore.stato_motore() == "Avviato":
            print(f"Accelerazione della {self.marca} {self.modello}.")
        else:
            print("Il motore non è avviato, impossibile accelerare.")
            
    def frena(self):
        print(f"Frenata della {self.marca} {self.modello}.")



motore = Motore("Benzina", 150)
print(motore.stato_motore())
motore.avvia_motore()
print(f"Stato del motore: {motore.stato_motore()}")

MyCar = Macchina("Fiat", "Panda", 2020, motore, Radio("Sony", "XAV-AX1000"))
MyCar.accendi_auto()
print(MyCar.motore.stato_motore())
print(MyCar.radio.stato_volume())

MyCar.accelera()
MyCar.radio.aumenta_volume()
print(MyCar.radio.stato_volume())

MyCar.frena()
MyCar.spegni_auto()
print(f"Stato del motore dopo lo spegnimento: {motore.stato_motore()}")
print(f"Stato del volume radio dopo lo spegnimento: {MyCar.radio.stato_volume()}")