# Definizione della classe Motore
class Motore:
    # Costruttore che inizializza tipo, potenza e stato del motore
    def __init__(self, tipo, potenza):
        self.tipo = (
            tipo  # Attributo pubblico per il tipo di motore (es. "Benzina", "Diesel")
        )
        self.potenza = potenza  # Attributo pubblico per la potenza del motore
        self.__avviato = (
            False  # Attributo privato per lo stato del motore (avviato/spento)
        )

    # Metodo per avviare il motore
    def avvia_motore(self):
        print(
            f"Motore {self.tipo} con potenza {self.potenza} avviato."
        )  # Stampa messaggio di avvio
        self.__avviato = True  # Imposta lo stato del motore su avviato

    # Metodo per spegnere il motore
    def spegni_motore(self):
        print(
            f"Motore {self.tipo} con potenza {self.potenza} spento."
        )  # Stampa messaggio di spegnimento
        self.__avviato = False  # Imposta lo stato del motore su spento

    # Metodo per verificare lo stato del motore
    def stato_motore(self):
        return self.__avviato  # Restituisce True se avviato, False se spento


# Definizione della classe Radio
class Radio:
    # Costruttore che inizializza gli attributi della radio
    def __init__(self, marca, modello, max_volume):
        self.marca = marca  # Attributo per la marca della radio
        self.modello = modello  # Attributo per il modello della radio
        self.modalità = "FM"  # Modalità predefinita impostata su FM
        self.frequenza = 101.1  # Frequenza predefinita in MHz
        self.max_volume = max_volume  # Volume massimo consentito
        self.volume = 0  # Volume iniziale impostato a 0

    # Metodo per accendere la radio
    def accendi_radio(self):
        print(
            f"Radio {self.marca} {self.modello} accesa."
        )  # Stampa messaggio di accensione

    # Metodo per spegnere la radio
    def spegni_radio(self):
        print(
            f"Radio {self.marca} {self.modello} spenta."
        )  # Stampa messaggio di spegnimento

    # Metodo per aumentare il volume
    def aumenta_volume(self):
        if self.volume < self.max_volume:  # Verifica se il volume non è già al massimo
            self.volume += 1  # Incrementa il volume di 1
            print(f"Volume aumentato a {self.volume}.")  # Stampa il nuovo volume
        else:
            print("Volume già al massimo.")  # Messaggio se il volume è già al massimo

    # Metodo per diminuire il volume
    def diminuisci_volume(self):
        if self.volume > 0:  # Verifica se il volume non è già a 0
            self.volume -= 1  # Decrementa il volume di 1
            print(f"Volume diminuito a {self.volume}.")  # Stampa il nuovo volume
        else:
            print("Volume già al minimo.")  # Messaggio se il volume è già al minimo

    # Metodo per cambiare modalità della radio
    def cambia_modalità(self, nuova_modalità):
        self.modalità = nuova_modalità  # Imposta la nuova modalità
        print(f"Modalità radio cambiata a {self.modalità}.")  # Stampa la nuova modalità

    # Metodo per mostrare la frequenza attuale
    def mostra_frequenza(self):
        if self.modalità == "FM":  # Verifica se la modalità è FM
            print(
                f"Frequenza attuale: {self.frequenza} MHz."
            )  # Stampa frequenza per FM
        else:
            print(
                "Modalità non supportata per la frequenza."
            )  # Messaggio per altre modalità


# Definizione della classe Auto (composizione con Motore e Radio)
class Auto:
    # Costruttore che inizializza gli attributi dell'auto
    def __init__(self, marca, modello, anno, Motore: Motore, Radio: Radio):
        self.marca = marca  # Attributo per la marca dell'auto
        self.modello = modello  # Attributo per il modello dell'auto
        self.anno = anno  # Attributo per l'anno dell'auto
        self.motore = Motore  # Composizione: l'auto contiene un oggetto Motore
        self.radio = Radio  # Composizione: l'auto contiene un oggetto Radio

    # Metodo per accendere l'auto
    def accendi_auto(self):
        print(
            f"Accensione dell'auto {self.marca} {self.modello} del {self.anno}."
        )  # Messaggio di accensione
        self.motore.avvia_motore()  # Avvia il motore dell'auto
        self.radio.accendi_radio()  # Accende la radio dell'auto

    # Metodo per spegnere l'auto
    def spegni_auto(self):
        print(
            f"Spegni l'auto {self.marca} {self.modello} del {self.anno}."
        )  # Messaggio di spegnimento
        self.motore.spegni_motore()  # Spegne il motore dell'auto
        self.radio.spegni_radio()  # Spegne la radio dell'auto

    # Metodo per accelerare l'auto
    def accelera(self):
        if self.motore.stato_motore():  # Verifica se il motore è avviato
            print(
                f"L'auto {self.marca} {self.modello} accelera."
            )  # Messaggio di accelerazione
        else:
            print(
                "Il motore non è avviato, impossibile accelerare."
            )  # Errore se motore spento

    # Metodo per attivare il Bluetooth
    def attiva_bluetooth(self):
        print(
            f"Attivazione Bluetooth per la radio {self.radio.marca} {self.radio.modello}."
        )  # Messaggio attivazione
        self.radio.cambia_modalità("Bluetooth")  # Cambia modalità radio a Bluetooth
        self.radio.mostra_frequenza()  # Mostra informazioni frequenza

    # Metodo per disattivare il Bluetooth
    def disattiva_bluetooth(self):
        print(
            f"Disattivazione Bluetooth per la radio {self.radio.marca} {self.radio.modello}."
        )  # Messaggio disattivazione
        self.radio.cambia_modalità("FM")  # Cambia modalità radio a FM
        self.radio.mostra_frequenza()  # Mostra informazioni frequenza


# Creazione di un'istanza della classe Auto con motore e radio specifici
My_Car = Auto(
    "Fiat",
    "Punto",
    2020,  # Parametri dell'auto: marca, modello, anno
    Motore("Benzina", 90),  # Creazione oggetto Motore con tipo e potenza
    Radio(
        "Sony", "XAV-AX1000", 30
    ),  # Creazione oggetto Radio con marca, modello e volume max
)

# Sequenza di operazioni sull'auto creata
My_Car.accelera()  # Tenta di accelerare (motore spento, dovrebbe dare errore)
My_Car.accendi_auto()  # Accende l'auto (avvia motore e radio)
My_Car.accelera()  # Accelera (ora il motore è acceso)
My_Car.attiva_bluetooth()  # Attiva modalità Bluetooth della radio
My_Car.disattiva_bluetooth()  # Disattiva Bluetooth e torna a FM
My_Car.spegni_auto()  # Spegne l'auto (spegne motore e radio)
