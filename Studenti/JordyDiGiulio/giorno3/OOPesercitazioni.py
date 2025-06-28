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

##### DISCORD #####

# ESERCIZIO 1 
'''Creare una classe chiamata Persona con nome ed età come attributi.
Aggiungere un metodo che stampi se la persona è maggiorenne (età >= 18) o minorenne.
Usare una struttura if per fare il controllo.'''

class Persona:
    def __init__(self, nome, età):
        self.nome = nome
        self.età = età
    
    def is_maggiorenne(self):
        if int(self.età) >= 18:
            print('Si è maggiorenne')
        else:
            print('Non è maggiorenne')

bober = Persona('bober', '25')

bober.is_maggiorenne()

# ESERCIZIO 2
class Studente:
    def __init__(self, nome, lista_voti):
        self.nome = nome
        self.lista_voti = lista_voti
    
    
    def calcola_media(self):
        somma = 0
        for voto in self.lista_voti:
            somma += voto
            
            media = somma / len(self.lista_voti)

        return media
    
    
    def is_promosso(self):
        media = self.calcola_media()

        if media >= 8:
            print('Promosso con ottimi voti')

        if media >= 6:
            
            if media >= 8:
                return f'Promosso con ottimi voti (media: {media})'
            else:
                return f'Promosso (media: {media})'
        
        else:
            return f'Bocciato (media: {media})'
    

lista_voti = [4, 6, 8, 9, 10, 3, 5]
studente1 = Studente('marco',lista_voti)

print(studente1.is_promosso())


# ESERCIZIO 3

class Negozio:
    def __init__(self):
        self.inventario = {
            'pane': 10,
            'latte': 5,
            'biscotti': 14,
            'caramelle': 7
        }
    
    def mostra_inventario(self):

        for prodotto, quantità in self.inventario.items():
            print(f'- {prodotto}: {quantità}')
    
    def shop(self, switch=False):

        while switch:
            self.mostra_inventario()
            print('Digitare un comando:' \
            '- acquista' \
            '- esci')
            comando = input()

            if comando == 'acquista':
                self.mostra_inventario()
                prodotto_acquistato = input('Scegliere il prodotto da acquistare')

                #or prodotto in self.inventario.keys():
                if str(prodotto_acquistato) in self.inventario.keys():
                    if self.inventario[prodotto_acquistato] > 0:
                        print(f"L'acquisto di {prodotto_acquistato} è andato a buon fine")
                        self.inventario[prodotto_acquistato] -= 1
                    else:
                        print('Ci dispiace, il prodotto richiesto non è disponibile')
            
            elif comando == 'esci':
                print('Grazie per averci scelto!')
                break

            else:
                print('Comando non valido')
                break


negozio = Negozio()

negozio.shop(True)
            
