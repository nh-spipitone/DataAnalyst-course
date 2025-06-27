def fizzbuzz_personalizzato(n: int, parola: str) -> list[str]:

    
    if n < 1:
        raise ValueError("Il numero deve essere maggiore o uguale a 1.")

    
    risultati = []

    
    for numero in range(1, n + 1):
        
        if "7" in str(numero):
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



while True:
    n = int(input("Inserisci un numero intero maggiore o uguale a 1: "))
    parola = input("Inserisci una parola: ")
    risultato = fizzbuzz_personalizzato(n, parola)
    print(risultato)
    continua = input("Vuoi continuare? (s/n): ")
    if continua.lower() != "s":
        break