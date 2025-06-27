def presentami(nome, cognome, età):
    
    return print(f'Ciao, sei {nome} {cognome} e hai {età} anni')

presentami('jordy', 'di giulio', '28')

###### ESERCIZI DISCORD ###############

# 1 #

def saluta(nome):
    print(f"Ciao, {nome}!")

nome_utente = input("Inserisci il tuo nome: ")
saluta(nome_utente)



# 2 #

def valuta_voto():
    voto = int(input("Inserisci il tuo voto (0-10): "))
    if voto < 6:
        print("Non promosso")
    elif voto == 10:
        print("Promosso con lode")
    else:
        print("Promosso")

valuta_voto()



# 3 #

def analizza_numero():
    numero = int(input("Inserisci un numero intero: "))
    if numero > 0:
        if numero % 2 == 0:
            print("Numero positivo pari")
        else:
            print("Numero positivo dispari")
    elif numero == 0:
        print("Il numero è zero")
    else:
        print("Numero negativo")

analizza_numero()

# 4 #

def calcolatrice(numero1, numero2, operazione):
    if operazione == "+":
        return numero1 + numero2
    elif operazione == "-":
        return numero1 - numero2
    elif operazione == "*":
        return numero1 * numero2
    elif operazione == "/":
        if numero2 == 0:
            return "Errore: divisione per zero"
        return numero1 / numero2
    else:
        return "Operazione non valida"


primo_numero = float(input("Inserisci il primo numero: "))
secondo_numero = float(input("Inserisci il secondo numero: "))
operazione_desiderata = input("Inserisci l'operazione (+, -, *, /): ")

risultato = calcolatrice(primo_numero, secondo_numero, operazione_desiderata)
print("Risultato:", risultato)

# BONUS

def is_palindroma(parola):

    parola = str(parola.lower())

    lista_di_lettere = parola.split()

    if lista_di_lettere == sorted(lista_di_lettere, reverse=True):
        print('è palindroma')
    else:
        print('Non è palindroma')

is_palindroma('anna')