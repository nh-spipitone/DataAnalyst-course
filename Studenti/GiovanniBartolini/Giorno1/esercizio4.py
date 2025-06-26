#4: Data una lista di nomi,
# # a) Usa un ciclo per separare i nomi in due liste: una con i nomi che iniziano con una vocale e una con i nomi che iniziano con una consonante.
# # b) Stampa le due liste ottenute.

nomi = ["Anna", "Marco", "Elena", "Osvaldo", "Luca", "Irene", "Giorgio", "Umberto"]
print(f"Nomi originali: {nomi}")

lista_vocali_maiuscole = ['A', 'E', 'I', 'O', 'U']

nomi_vocali = []
nomi_consonanti = []
for nome in nomi:
    inizia_con_vocale = False
    for vocale in lista_vocali_maiuscole:
        if nome[0] == vocale:
            inizia_con_vocale = True
    if inizia_con_vocale:
        nomi_vocali.append(nome)
    else:
        nomi_consonanti.append(nome)

print(f"Nomi che iniziano con una vocale:     {nomi_vocali}")
print(f"Nomi che iniziano con una consonante: {nomi_consonanti}")