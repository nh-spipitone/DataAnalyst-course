# #livello1
# #punto1
# temperatura_max = [25, 30, 33, 35, 29]

# media = 0

# for temp in temperatura_max:
#     media += temp

# media = media / len(temperatura_max)

# print(f"la media della temperatura massima della settimana è {media} C°")

# temperatura_max.sort(reverse=True)

# print(f"la temperatura massima della settimana è {temperatura_max} C°")

# #punto2

# tupla_temperatura = tuple(temperatura_max)

# print(f"la tupla delle temperature massime è {tupla_temperatura}")

# # tupla_temperatura [0] = 24 immutabile

# #punto3
# numeri = [3, 5, 3, 7, 5, 9, 3]

# print("lunghezza numeri:", len(numeri))

# numeri_unici = list(set(numeri))    #elimina i duplicati e converte in lista

# numeri_unici.sort(reverse=True)      #ordina i numeri in ordine decrescente

# print(f"nuova lista numeri: {numeri_unici}")

# print("nuova lunghezza numeri:", len(numeri_unici))

# #punto4




#livello2
#punto5
voto = int(input("digita un voto tra 0 e 100:"))

if voto < 60:
    print("insufficiente")

elif voto < 70 or voto == 60:
    print("sufficiente")
elif voto < 80 or voto == 70:
    print("buono")

elif voto < 90 or voto == 80:
    print("ottimo")

else:
    print("eccellente")

print("il voto è:", voto)

#punto6

tabellina_7 = []

for n in range(1,11):
    riga = ""
    for i in range(1,11):
        tabellina = n * i
        tabellina_7.append(f"7 x {i} = {tabellina}")
        riga += f" {n} x {i} = {tabellina}"
        print(riga)

somma = 0
media = 0
contatore = 0
while True:
    n = float(input("digita un numero oppure usa 0 per terminare:"))
    if n == 0:
        break
    contatore += 1
    somma = somma + n
media = somma /contatore

    
    
    
    



