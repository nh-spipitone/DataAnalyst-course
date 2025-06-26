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

voto = 