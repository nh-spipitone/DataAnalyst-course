from datetime import date

# Definizione della classe base Animale
class Animale:
    # Costruttore che inizializza gli attributi comuni a tutti gli animali
    def __init__(self, nome, specie, eta, peso):
        self.nome = nome  # Attributo per il nome dell'animale
        self.specie = specie  # Attributo per la specie dell'animale
        self.eta = eta  # Attributo per l'età dell'animale
        self.peso = peso  # Attributo per il peso dell'animale

    # Metodo per mostrare le informazioni base dell'animale
    def mostra_informazioni(self):
        print(f"Nome: {self.nome}")  # Stampa il nome dell'animale
        print(f"Specie: {self.specie}")  # Stampa la specie dell'animale
        print(f"Età: {self.eta} anni")  # Stampa l'età dell'animale
        print(f"Peso: {self.peso} kg")  # Stampa il peso dell'animale


# Definizione della classe Cane che eredita da Animale
class Cane(Animale):
    # Costruttore che accetta nome, razza, età e peso
    def __init__(self, nome, razza, eta, peso):
        # Chiama il costruttore della classe padre, impostando automaticamente specie="Cane"
        super().__init__(nome, "Cane", eta, peso)
        self.razza = razza  # Attributo specifico per la razza del cane

    # Metodo specifico per il comportamento del cane
    def abbaia(self):
        print(f"{self.nome} abbaia!")  # Stampa che il cane abbaia

    # Override del metodo mostra_informazioni per includere la razza
    def mostra_informazioni(self):
        super().mostra_informazioni()  # Chiama il metodo della classe padre
        print(f"Razza: {self.razza}")  # Aggiunge l'informazione sulla razza


# Definizione della classe Gatto che eredita da Animale
class Gatto(Animale):
    # Costruttore che accetta nome, razza, età e peso
    def __init__(self, nome, razza, eta, peso):
        # Chiama il costruttore della classe padre, impostando automaticamente specie="Gatto"
        super().__init__(nome, "Gatto", eta, peso)
        self.razza = razza  # Attributo specifico per la razza del gatto

    # Metodo specifico per il comportamento del gatto
    def miagola(self):
        print(f"{self.nome} miagola!")  # Stampa che il gatto miagola

    # Override del metodo mostra_informazioni per includere la razza
    def mostra_informazioni(self):
        super().mostra_informazioni()  # Chiama il metodo della classe padre
        print(f"Razza: {self.razza}")  # Aggiunge l'informazione sulla razza


# Creazione di un'istanza della classe Cane
mio_cane = Cane("Fido", "Labrador", 3, 30)
# Creazione di un'istanza della classe Gatto
mio_gatto = Gatto("Micio", "Siamese", 2, 5)


# Chiamata al metodo per mostrare le informazioni del cane
mio_cane.mostra_informazioni()
# Chiamata al metodo specifico per far abbaiare il cane
mio_cane.abbaia()
# Chiamata al metodo per mostrare le informazioni del gatto
mio_gatto.mostra_informazioni()
# Chiamata al metodo specifico per far miagolare il gatto
mio_gatto.miagola()


class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def info(self):
        return f"{self.anno} {self.marca} {self.modello}"


class Auto(Veicolo):
    def __init__(self, marca, modello, anno, porte):
        super().__init__(marca, modello, anno) 
        self.porte = porte

    def info(self):
        return f"{super().info()}, Porte: {self.porte}"


class Moto(Veicolo):
    def __init__(self, marca, modello, anno, cilindrata):
        super().__init__(marca, modello, anno)
        self.cilindrata = cilindrata

    def info(self):
        return f"{super().info()}, Cilindrata: {self.cilindrata}cc"





class Prodotto:
    def __init__(self, nome, prezzo):
        self.nome = nome
        self.prezzo = prezzo

    def descrizione(self):
        return f"Prodotto: {self.nome}, Prezzo: €{self.prezzo:.2f}"


class Alimentari(Prodotto):
    def __init__(self, nome, prezzo, scadenza):
        super().__init__(nome, prezzo)
        self.scadenza = scadenza  

    def descrizione(self):
        return (f"Alimentare: {self.nome}, Prezzo: €{self.prezzo:.2f}, "
                f"Scadenza: {self.scadenza.strftime('%d/%m/%Y')}")


class Elettronico(Prodotto):
    def __init__(self, nome, prezzo, garanzia):
        super().__init__(nome, prezzo)
        self.garanzia = garanzia  

    def descrizione(self):
        return (f"Elettronico: {self.nome}, Prezzo: €{self.prezzo:.2f}, "
                f"Garanzia: {self.garanzia}")

