# Scrivi una funzione fizzbuzz_personalizzato(n, parola) che:

# Parametri in ingresso

# n – intero positivo (> 0) che rappresenta il limite superiore.
# parola – stringa che sarà stampata in determinate condizioni.
# Per ogni numero da 1 a n (incluso) la funzione deve decidere cosa stampare seguendo queste regole (in ordine di priorità):

# Se il numero contiene la cifra 7 → stampa "parola"
# (es. 7, 17, 27, 70 – 79, …)
# Altrimenti, se il numero è multiplo di 3 e 5 → stampa "FizzBuzz"
# Altrimenti, se è multiplo di 3 → stampa "Fizz"
# Altrimenti, se è multiplo di 5 → stampa "Buzz"
# In tutti gli altri casi → stampa il numero stesso.
# La funzione restituisce la lista dei valori stampati, così da poter essere testata in automatico.

def fizzbuzz_personalizzato(n:int, parola:str) -> list[str]:
    risultati = []
    for i in range(1, n + 1):
        if '7' in str(i):
            risultati.append(parola)
            #print(parola)
        elif i % 15 == 0:
            risultati.append("FizzBuzz")
            #print("FizzBuzz")
        elif i % 3 == 0:
            risultati.append("Fizz")
            #print("Fizz")
        elif i % 5 == 0:
            risultati.append("Buzz")
            #print("Buzz")
        else:
            risultati.append(str(i))
            #print(i)
    return risultati

# Esempio di utilizzo
# test con n = 20 e parola = "Sette!"
risultato = fizzbuzz_personalizzato(20, "Sette!")
print("Risultati con n = 20 e parola 'Sette!':", risultato)
# Output atteso:
# 1 , 2 , Fizz , 4 , Buzz , Fizz , Sette! , 8 , Fizz , Buzz , 11 , Fizz , 13 , 14 , FizzBuzz , Sette! , 17 , 18 , Fizz , 20

# test con n negativo
risultato_negativo = fizzbuzz_personalizzato(-5, "Sette!")
print("Risultati con n negativo:", risultato_negativo)
# Output atteso: []

# test con input utente
try:
    n_input = int(input("Inserisci un numero intero positivo: "))
    parola_input = input("Inserisci una parola: ")
    if n_input > 0:
        risultato_input = fizzbuzz_personalizzato(n_input, parola_input)
        print("Risultati con input utente:", risultato_input)
    else:
        print("Il numero deve essere positivo.")
except ValueError:
    print("Input non valido. Assicurati di inserire prima un numero intero positivo e poi una parola.")

