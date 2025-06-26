nomi = ["Anna", "Marco", "Elena", "Osvaldo", "Luca", "Irene", "Giorgio", "Umberto"]

vocali = []
consonanti = []

for nome in nomi:
    if nome[0] .lower() in ("a", "e", "i", "o", "u"): #oppure if nome.startswith(('A', 'E', 'I', 'O', 'U')):

        vocali.append(nome) #nome[0] per prendere il primo in questo caso, nome, della lista nomi; Se fosse stato nome[1] avrebbe preso il secondo nome della lista nomi
        
    else: 
        consonanti.append(nome)

print("Nomi che iniziano per vocale:", vocali)
print("Nomi che iniziano per consonante:", consonanti)

