spesa = {"uova": 1.5, "pane": 2.0, "latte": 1.2, "pasta": 0.8, "carne": 5.0}



articolo = str(input("Inserisci un prodotto"))
prezzo = float(input("Inserisci il prezzo del prodotto"))

spesa[articolo] = prezzo

print(f"Il prezzo di {spesa}")

totale_spesa = 0
for articolo, prezzo in spesa.items():
    print(f"Il prezzo di {articolo} è {prezzo}")
    totale_spesa += prezzo
print(f"Il totale della spesa è: {totale_spesa}")
