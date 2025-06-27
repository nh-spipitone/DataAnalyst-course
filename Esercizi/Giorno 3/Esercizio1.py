# Definisce una funzione che prende un numero intero n e una stringa parola come parametri
# Restituisce una lista di stringhe
def fizzbuzz_personalizzato(n: int, parola: str) -> list[str]:

    # Controlla se n è minore di 1 e solleva un'eccezione se è vero
    if n < 1:
        raise ValueError("Il numero deve essere maggiore o uguale a 1.")

    # Inizializza una lista vuota per contenere i risultati
    risultati = []

    # Itera attraverso tutti i numeri da 1 a n (incluso)
    for numero in range(1, n + 1):
        # Controlla se il carattere "7" è presente nella rappresentazione stringa del numero
        if "7" in str(numero):
            risultati.append(parola)  # Aggiunge la parola personalizzata alla lista
        # Controlla se il numero è divisibile sia per 3 che per 5
        elif numero % 3 == 0 and numero % 5 == 0:
            risultati.append("FizzBuzz")  # Aggiunge "FizzBuzz" alla lista
        # Controlla se il numero è divisibile per 3
        elif numero % 3 == 0:
            risultati.append("Fizz")  # Aggiunge "Fizz" alla lista
        # Controlla se il numero è divisibile per 5
        elif numero % 5 == 0:
            risultati.append("Buzz")  # Aggiunge "Buzz" alla lista
        # Se nessuna delle condizioni precedenti è vera
        else:
            risultati.append(str(numero))  # Aggiunge il numero come stringa alla lista

    # Restituisce la lista completa dei risultati
    return risultati


while True:
    n=int(input("Inserisci un numero intero maggiore o uguale a 1:"))
    parola=input("Inserisci una parola:")
    risultato= fizzbuzz_personalizzato(n,parola)
    print(risultato)
    continua= input("Vuoi continuare? (s/n):")
    if continua.lower() != 's':
        break
    



