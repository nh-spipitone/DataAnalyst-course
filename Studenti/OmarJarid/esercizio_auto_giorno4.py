class Motore:
    def __init__(self, tipo, potenza):
        self.tipo = tipo
        self.potenza = potenza
        self.__avviato = False # Proprità privata protetta

    def avvia_motore(self):
        print(f"Motore {self.tipo} con potenza {self.potenza} avviato")
        self.__avviato = True

    def spegni_motore(self):
        print(f"Motore {self.tipo} con potenza {self.potenza} spento")
        self.__avviato = False

    def stato_motore(self): return self.__avviato
        
class Radio:
    def __init__(self, marca, modello, max_volume):
        self.marca = marca
        self.modello = modello
        self.max_volume = max_volume
        self.volume = 0

    def accendi_radio(self): print(f"Radio {self.marca} {self.modello} accesa")
    
    def spegni_radio(self): print(f"Radio {self.marca} {self.modello} spenta")
    
    def aumenta_volume(self):
        if self.volume < self.max_volume:
            self.volume += 1
            print(f"Volume aumentato: {self.volume}")
        else:
            print("Volume già al massimo")
        
        def diminuisci_volume(self):
            if self.volume > 0:
                self.volume -= 1
                print(f"Volume diminuito a {self.volume}")
            else:
                print("Volume già al minimo")

        def cambia_modalita(self, nuova_modalita):
            self.modalita = nuova_modalita
            print(f"Modalità radio cambiata a {self.modalita}")

        def mostra_frequenza(self):
            if self.modalita == "FM":
                print("Frequenza FM")
            else:
                print("Modalità non supportata per la frequenza")

class Auto:
    def __init__(self, marca, modello, anno, motore: Motore):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.motore = motore

    def accendi_auto(self):
        self.motore.avvia_motore()
        self.motore.accendi_radio()
        print(f"Auto {self.marca} {self.modello} accesa")

    def spegni_auto(self):
        self.motore.spegni_motore()
        self.motore.spegni_radio()
        print(f"Auto {self.marca} {self.modello} spenta")

    def accelera(self):
        if self.motore.stato_motore():
            print("Auto già in movimento")
            return
        
        self.motore.avvia_motore()
        print(f"Auto {self.marca} {self.modello} in movimento")

    def attiva_bluetooth(self):
        print(f"Attivazione Bluetooth per la radio {self.radio.marca} {self.radio.modello}")
        self.radio.cambia_modalita("Bluetooth")
        self.radio.mostra_frequenza()

    def disattiva_bluetooth(self):
        print(f"Disattivazione Bluetooth per la radio {self.radio.marca} {self.radio.modello}")
        self.radio.cambia_modalita("FM")
        self.radio.mostra_frequenza()
    

moto = Motore("Benzina", 150)
moto.stato_motore()

my_car = Auto(
    "Fiat", 
    "Punto", 
    2020, 
    Motore("Benzina", 90), 
    Radio("Sony", "Xperia", 10)
)