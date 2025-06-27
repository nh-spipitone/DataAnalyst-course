"""------------------------------------------------------------------------------"""

# ES1
# Scrivi una funzione chiamata saluta che accetta un parametro nome.
# All'interno della funzione, stampa un saluto che includa il nome, ad esempio "Ciao, [nome]!".
# Chiedi all'utente di inserire il suo nome tramite input().
# Chiama la funzione saluta passando il nome dell'utente come argomento.
def saluta(nome):
    print(f"Ciao, {nome}!")

saluta(input("Come ti chiami? ").capitalize())

"""------------------------------------------------------------------------------"""

# ES2
# Scrivi una funzione chiamata valuta_voto che:
# Chiede all’utente di inserire il proprio voto finale (0-10).
# Se il voto è minore di 6, stampa “Non promosso”.
# Se il voto è almeno 6:
# Se è 10, stampa “Promosso con lode”.
# Altrimenti, stampa “Promosso”.
def valuta_voto(voto):
    voto = int(voto)
    if voto == 10:
        print("Promosso con lode")
    elif voto > 5:
        print("Promosso")
    else:
        print("Non promosso")

valuta_voto(input("Che voto hai preso da 1-10? "))

"""------------------------------------------------------------------------------"""

# ES3
# Scrivi una funzione chiamata analizza_numero che:
# Chiede all’utente di inserire un numero intero.
# Se il numero è maggiore di 0, controlla se è pari o dispari.
# Se è 0, stampa “Il numero è zero”.
# Se è minore di 0, stampa “Numero negativo”.
def analizza_numero(numero):
    numero = int(numero)
    if numero > 0:
        if numero % 2 == 0:
            print("Il num è pari!")
        else:
            print("Il num è dispari!")
    elif numero < 0:
        print("Il numero è negativo")
    else:
        print("Il numero è 0!")

analizza_numero(input("Ins num intero: "))

"""------------------------------------------------------------------------------"""

# ES4
# Scrivi una funzione chiamata valuta_voto che:
# Chiede all’utente di inserire il proprio voto finale (0-10).
# Se il voto è minore di 6, stampa “Non promosso”.
# Se il voto è almeno 6:
# Se è 10, stampa “Promosso con lode”.
# Altrimenti, stampa “Promosso”.
valuta_voto(input("Che voto hai preso da 1-10? "))

"""------------------------------------------------------------------------------"""

# ES5
# Scrivi una funzione chiamata calcolatrice che accetta tre parametri: num1, num2, e operazione (una stringa come "+", "-", "*", "/").
# All'interno della funzione, usa if/elif/else per determinare quale operazione eseguire.
# Restituisci il risultato del calcolo.
# Gestisci il caso della divisione per zero: se operazione è "/" e num2 è 0, la funzione dovrebbe restituire una stringa di errore (es. "Errore: divisione per zero").
# Chiedi all'utente due numeri e un simbolo di operazione.
# Chiama la funzione e stampa il risultato
def calcolatrice(num1,num2,operazione):
    if operazione == "+":
        return num1+num2
    elif operazione == "-":
        return num1-num2
    elif operazione == "*":
        return num1*num2
    elif operazione == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("Divisione impossibile!")
    else:
        return "Segno sbagliato!"

print(calcolatrice(int(input("Scegli num1: ")),int(input("Scegli num2: ")),input("Scegli operazione: "),))

"""------------------------------------------------------------------------------"""

# ES BONUS
# Scrivi una funzione chiamata is_palindroma che prende una stringa come parametro e restituisce True se la parola è palindroma, altrimenti False.
#  Una parola è palindroma se si legge uguale da sinistra a destra e da destra a sinistra.
def palindromo(stringa):
    stringa = list(stringa)
    stringa2 = stringa.copy()
    stringa2.reverse()
    print(stringa, stringa2)
    if stringa == stringa2:
        return True
    else:
        return False

print(palindromo(input("Inserisci stringa: ")))