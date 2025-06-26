# #punto 5

# voto = int(input("digita un voto tra 0 e 100: "))

# if voto <60:
#     print("insufficente")
# elif voto <= 69:
#     print("sufficiente")
# elif voto <= 79:
#     print("buono")
# elif voto <= 89:
#     print("ottimo")
# else:
#     print("eccellente")

# print("il voto è:", voto)

#punto 6

tabellina_del_7= []

for n in range (1,11):
    riga=""
    for i in range (1,11):
        tabellina=n*i 
        tabellina_del_7.append(f"7x{i}={tabellina}")
        riga+=f"{n}x{i}={tabellina} "
    print(riga)

somma=0
media=0
contatore=0
numeri=[]
while True:
    n=float(input("digita un numero o usa 0 per terminare:"))
    if n == 0:
        break
    contatore+=1
    somma=somma+n
media= somma / contatore


    



           
