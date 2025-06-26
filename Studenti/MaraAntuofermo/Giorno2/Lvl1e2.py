#Livello 1
#Punto 1

temperature_max = [25, 30, 33, 35, 29]

media = 0 

for temp in temperature_max:
    media += temp

media = media / len(temperature_max)

print(f"La media delle temperature massime della settimana è {media} C°")

temperature_max.sort(reverse=True) #ordina in modo decrescente

print(f"La temperatura massima della settimana aggiornata è {temperature_max[0]} C°")


#Punto 2
Tupla_temperature = tuple(temperature_max)

print(f"La tupla delle temperature massime è {Tupla_temperature}")

#Tupla_temperature [0] = 24 Immutabile 


#Punto 3
numeri = [3, 5, 3, 7, 5, 9, 3]

print("Lunghezza numeri:", len(numeri))

numeri_unici = list(set(numeri)) #Elimina i duplicati e converte in lista

numeri_unici.sort() #Ordina la lista in modo crescente

print(f"Nuova lista numeri: {numeri_unici}")

print("Nuova lunghezza numeri", len(numeri_unici))

#Punto 4 (Funzioni)




#Livello 2
#Punto 5

voto = int(input("Inserisci il voto: "))

if voto < 60:    #if voto >= 60 and voto < 69: 
    print("Insufficiente")

elif voto <= 69:
    print("Sufficiente")

elif voto <= 79:
    print("Buono")

elif voto <= 89:
    print("Ottimo")

else:
    print("Eccellente")    

print("Il voto è:", voto)


#Punto 6

tabellina_del_7 = []

for n in range (1, 11): 
    riga = ""
    for i in range (1,11):  #for i in range(1, 11):
        tabellina = n * i   #tabellina = 7 * i
        tabellina_del_7.append(f"7 x {i} = {tabellina}")  #print(f"{n} x {i} = {tabellina}")  #print(f"7 x {n} = {tabellina}")
        riga += f"{n} x {i} = {tabellina}"  
        print(riga)


#Punto 7

somma = 0 
media = 0
contatore = 0 
numeri = []

while True:
    n = float(input("Digita un numero o usa 0 per terminare: "))
    if n == 0:
        break
    contatore += 1 
    somma = somma + n 

media = somma / contatore 


