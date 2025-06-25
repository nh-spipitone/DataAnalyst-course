# Questa esercitazione contiene quattro esercizi di difficoltà media pensati per consolidare le nozioni su liste, insiemi, dizionari e controllo del flusso in Python.

# 1: Data una lista di numeri: 
# a) Crea una nuova lista contenente solo i numeri pari, 
# b) Utilizzando una list comprehension, genera una lista con i quadrati di tutti i numeri.
# c) Stampa la lunghezza di entrambe le liste risultanti.

numbers = [12, 7, 9, 20, 33, 4, 18]
print(f"Starting number list: {numbers}")

even_numbers = []
square_numbers = []
for num in numbers:
    #a)
    if num % 2 == 0:
        even_numbers.append(num)
    #b)
    square_numbers.append(num*num)

print(f"Even number list: {even_numbers}")
print(f"Square number list: {square_numbers}")

#c)
print(f"The lenght of the even number list is {len(even_numbers)}, and of the square number list is {len(square_numbers)}")
