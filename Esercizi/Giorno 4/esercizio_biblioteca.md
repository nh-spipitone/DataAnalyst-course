# 📝 Esercizio Python: Gestione Biblioteca (OOP & Logica)

## Scenario

Devi creare un semplice gestionale per una biblioteca che tiene traccia dei libri e dei prestiti.

---

## Punti della consegna

### 1️⃣ Crea una classe `Libro` con:

-   Attributi: `titolo` (stringa), `autore` (stringa), `disponibile` (booleano, di default True)
-   Metodo: `presta()` che imposta `disponibile` a False.
-   Metodo: `restituisci()` che imposta `disponibile` a True.

---

### 2️⃣ Nel programma principale, crea una lista di **almeno 5 libri** diversi (titolo e autore a piacere).

---

### 3️⃣ **Stampa tutti i libri disponibili** (cioè quelli con `disponibile=True`), indicando titolo e autore.

---

### 4️⃣ Simula il prestito di **due libri** a scelta chiamando il metodo `.presta()` sugli oggetti corrispondenti.

---

### 5️⃣ Stampa nuovamente la lista dei libri disponibili (devono essere diminuiti di due).

---

### 6️⃣ Simula la restituzione di uno dei libri prestati, poi stampa di nuovo la lista dei disponibili.

---

### 7️⃣ **(Extra)** Conta e stampa quanti libri **NON** sono disponibili.

---

## Suggerimenti

-   Usa `for` e `if` per scorrere e filtrare i libri disponibili.
-   Puoi aggiungere metodi `__str__` per stampare meglio gli oggetti, ma non è obbligatorio.

---

## Esempio di output atteso (semplificato)

```
Libri disponibili:
- Il piccolo principe di Antoine de Saint-Exupéry
- Harry Potter di J.K. Rowling
...

Libri disponibili dopo prestiti:
- Il piccolo principe di Antoine de Saint-Exupéry
...

Libri disponibili dopo restituzione:
- Il piccolo principe di Antoine de Saint-Exupéry
- Harry Potter di J.K. Rowling
...

Libri NON disponibili: 1
```

---
