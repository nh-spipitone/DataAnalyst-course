# Esercizio: FizzBuzz personalizzato

## Obiettivo
Scrivi **una funzione** `fizzbuzz_personalizzato(n, parola)` che:

1. **Parametri in ingresso**
   * `n` – intero positivo (> 0) che rappresenta il limite superiore.
   * `parola` – stringa che sarà stampata in determinate condizioni.

2. **Per ogni numero da 1 a `n` (incluso)** la funzione deve **decidere cosa stampare** seguendo queste regole (in ordine di priorità):
   1. Se il numero **contiene la cifra `7`** → **stampa `parola`**  
      _(es. 7, 17, 27, 70 – 79, …)_  
   2. Altrimenti, se il numero è **multiplo di 3 _e_ 5** → stampa **`"FizzBuzz"`**
   3. Altrimenti, se è **multiplo di 3** → stampa **`"Fizz"`**
   4. Altrimenti, se è **multiplo di 5** → stampa **`"Buzz"`**
   5. In tutti gli altri casi → stampa **il numero stesso**.

3. La funzione **restituisce** la **lista** dei valori stampati, così da poter essere testata in automatico.

## Vincoli
* Usa **un ciclo `for`** per iterare da 1 a `n`.
* Gestisci le condizioni con **`if / elif / else`**.
* Non usare librerie esterne.

## Esempio
```python
risultato = fizzbuzz_personalizzato(20, "Sette!")
print(risultato)
```
Output atteso:
```
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', 'Sette!', '8', 'Fizz', 'Buzz', '11',
 'Fizz', '13', '14', 'FizzBuzz', '16', 'Sette!', 'Fizz', '19', 'Buzz']
```

## Suggerimenti
* Per verificare se un numero **contiene la cifra 7**:
  ```python
  if '7' in str(numero):
      ...
  ```
* Prova la funzione con **diversi** valori di `n` e `parola` per verificare che tutte le condizioni funzionino.

## Extra (facoltativo)
Permetti all’utente di inserire `n` e `parola` da tastiera e **richiama la funzione** per mostrare il risultato.
