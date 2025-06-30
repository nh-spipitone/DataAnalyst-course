# 📝 Esercizio Python Esteso: Gestione Biblioteca (OOP)

## Scenario

Ora la biblioteca deve gestire non solo i libri, ma anche alcune funzionalità per organizzare meglio i dati.

---

## Punti della consegna

### 1️⃣ Crea la classe `Libro` come già fatto prima.

### 2️⃣ Crea una classe `Biblioteca` che ha:

-   Un attributo `libri` (lista di oggetti `Libro`).
-   Metodo `aggiungi_libro(libro)` per aggiungere un libro alla biblioteca.
-   Metodo `prestito(titolo)` che cerca un libro per titolo, se disponibile lo presta e restituisce `True`, altrimenti `False`.
-   Metodo `restituzione(titolo)` che cerca un libro per titolo, se non è disponibile lo rende disponibile.
-   Metodo `elenco_disponibili()` che ritorna la lista di libri disponibili.
-   (EXTRA) Metodo `cerca_per_autore(autore)` che restituisce tutti i libri scritti da un certo autore.

---

### 3️⃣ Nel programma principale:

-   Crea una `Biblioteca`.
-   Aggiungi almeno 5 libri alla biblioteca usando il metodo apposito.
-   Stampa tutti i libri disponibili tramite il metodo della biblioteca.
-   Esegui un prestito e mostra la lista aggiornata.
-   Esegui una restituzione e mostra la lista aggiornata.
-   Usa la funzione di ricerca per autore per stampare tutti i libri di un autore specifico.

---

### 4️⃣ (Extra) Gestisci il caso in cui si provi a prendere in prestito o restituire un libro che non esiste.

---

## Esempio di output atteso (semplificato)

```
Libri disponibili:
- Il piccolo principe di Antoine de Saint-Exupéry
...

Prestito di "Harry Potter": OK

Libri disponibili dopo prestito:
...

Restituzione di "Harry Potter": OK

Libri disponibili dopo restituzione:
...

Libri scritti da J.K. Rowling:
- Harry Potter di J.K. Rowling

Prestito di "Libro Fantasma": Libro non trovato.
```

---
