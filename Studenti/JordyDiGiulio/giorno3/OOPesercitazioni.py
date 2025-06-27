# DEFINIRE UNA CLASSE

class Animale:
    def __init__(self, razza, habitat):
        self.razza = razza
        self.habitat = habitat


    def ruggito(self):
        print('rooaarrr')

animale1 = Animale('meticcio', 'giungla')

animale1.ruggito()


class Jordy:
    def __init__(self, nome, cognome, età):
        self.nome = nome
        self.cognome = cognome
        self.età = età

    def presenta(self):
        print(self.nome)
        print(self.cognome)
        print(self.età)

scheda_jordy = Jordy('jordy', 'di giulio', 28)

scheda_jordy.presenta()



class Gatto(Animale):
    def __init__(self, nome, colore, razza, habitat):
        super().__init__(razza, habitat)
        self.nome = nome
        self.colore = colore
    
    def ruggito(self):
        print('miao')

gatto1 = Gatto('carletto', 'nero', 'meticcio', 'città')
gatto1.ruggito()


