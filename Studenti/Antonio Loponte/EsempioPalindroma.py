def is_palindroma(s):
    # Converte la stringa in minuscolo e rimuove gli spazi
    s = s.lower().replace(" ", "")
    # Confronta la stringa con la sua versione invertita
    return s == s[::-1]


# Chiede all'utente di inserire una parola
parola = input("Inserisci una parola: ")
# Verifica se la parola è palindroma e stampa il risultato
if is_palindroma(parola):
    print("La parola è palindroma.")
else:
    print("La parola non è palindroma.")
