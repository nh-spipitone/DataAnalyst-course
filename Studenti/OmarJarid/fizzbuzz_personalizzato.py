def fizzbuzz_personalizzato(n: int, parola: str) -> list[str]:
    if n < 1: raise ValueError("Il numero deve essere maggiore o uguale a 1.")
    
    risultati = []
    for numero in range(1, n + 1):
        if '7' in str(numero):
            risultati.append(parola)
        elif numero % 3 == 0 and numero % 5 == 0:
            risultati.append("FizzBuzz")
        elif numero % 3 == 0:
            risultati.append("Fizz")
        elif numero % 5 == 0:
            risultati.append("Buzz")
        else:
            risultati.append(str(numero))

    return risultati

# print(fizzbuzz_personalizzato(20, "Sette!"))

while True:
    try:
        n = int(input("Inserisci un numero: "))
        parola = input("Inserisci la parola da sostituire: ")
        risultati = fizzbuzz_personalizzato(n, parola)
        print(risultati)
        scelta = input("Vuoi continuare? (s/n): ")
        match scelta.lower():
            case "s":
                continue
            case "n":
                print
                break
            case _:
                print("Scelta non valida.")
    except ValueError as e:
        print(e)