#Descrizione del progetto:

#“L’obiettivo del progetto è analizzare un dataset di viaggi internazionali per estrarre insight
#significativi sul comportamento dei viaggiatori, il costo dei viaggi e le preferenze in termini di destinazioni, 
#alloggi e trasporti. Utilizzerò strumenti come Python, Pandas, SQL e tecniche di regressione lineare e multipla 
#per costruire un modello predittivo e generare analisi approfondite.”



#Obiettivi principali:

  #Identificare pattern di viaggio (stagionalità, nazionalità, preferenze).
  #Stimare il costo totale del viaggio attraverso modelli di regressione.
  #Confrontare tipologie di alloggio e trasporto in base al costo e alla durata.
  #Utilizzare l’intelligenza artificiale per generare insight narrativi.



    #-----------------------------------------------------------------------------------------------------------#


#PASSO 1: PULIZIA E PREPARAZIONE DEL DATASET. 


#1.1 Importazione e lettura del dataset:

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sqlite3 



df = pd.read_csv(r"C:\Users\nnngh\Desktop\Corso Data Analyst\DataAnalyst-course\FILE DATASET\Travel details dataset PROGETTINO.csv",
                        encoding="utf-8", skip_blank_lines=True)  

                                       #encoding="utf-8": codifica del file CSV 
                                       #skip_blank_lines=True: salta le righe vuote




#1.2 Esplorazione iniziale:

print("Dimensioni del dataset:", df.shape)                  # Mostra il numero di righe e colonne
print("Prima 5 righe del dataset:", df.head())              # Visualizza le prime 5 righe 
print("Informazioni sulle colonne:", df.info())             # Mostra info sulle colonne, tipi di dato, valori nulli
print("Valori mancanti per colonna:\n", df.isnull().sum())  # Conta quanti valori mancanti ci sono per colonna

 



#1.3 Rimozione righe incomplete:

df = df.dropna(how = 'any')       # Rimuove tutte le righe con valori mancanti
print("Dimensioni del dataset dopo la rimozione delle righe incomplete:", df.shape)




#1.4 Pulizia dei costi: rimuove i simboli dei costi e rendere tutte i costi in formato numerico.


def pulizia_costi(value):       
    if pd.isnull(value):        # Se il valore è nullo, restituisci None  
                                # isnull: funzione per vedere se ci sono valori mancanti
        return None
    value = str(value).replace('$', '').replace('USD', '').replace(',', '').replace(' ', '')
    try:
        return float(value)     # Prova a convertire in float
    except:
        return None


df["Accommodation cost"] = df["Accommodation cost"].apply(pulizia_costi)
df["Transportation cost"] = df["Transportation cost"].apply(pulizia_costi)





#1.5 Conversione delle date: 

df['Start date'] = pd.to_datetime(df['Start date'], errors='coerce')   #errors='coerce' forza i valori non validi a diventare NaT (missing)
df['End date'] = pd.to_datetime(df['End date'], errors='coerce')       #pd.to_datetime trasforma stringhe in oggetti datetime.
 


#1.6. Creazione di nuove colonne:


df['Costo totale'] = df['Accommodation cost'] + df['Transportation cost']    # Creazione di una nuova colonna "Costo totale"
df['Costi per giorno'] = df['Costo totale'] / df['Duration (days)']     # Creazione di una nuova colonna "Costi per giorno"

print("Prima 5 righe del dataset con nuove colonne:", df.head())




#1.7. Pulizia delle categorie testuali:

print("Tipologie di trasporto disponibili:", df['Transportation type'].unique())         # unique: funzione per vedere i valori unici
print("Tipologie di alloggio disponibili:", df['Accommodation type'].unique())


df['Transportation type'] = df['Transportation type'].str.strip()    # Rimuove gli spazi bianchi iniziali e finali
df['Accommodation type'] = df['Accommodation type'].str.strip()        # Rimuove gli spazi bianchi iniziali e finali




#1.8  Funzione che prende una stringa e restituisce solo la parte prima della virgola:

def pulizia_stati_destinazioni(destination):
    if pd.isnull(destination):  # Se il valore è nullo, restituisci None
        return None
    return destination.split(',')[0].strip()  # Prende solo la prima parte prima della virgola e rimuove spazi extra

# Applichiamo la funzione alla colonna 'Destination'
df['Destination'] = df['Destination'].apply(pulizia_stati_destinazioni)






#PASSO 2: ANALISI ESPLORATIVA DEI DATI (EDA): 


#2.1 ANALISI DISTRIBUZIONE DELLE DESTINAZIONI PIU FREQUENTI:

top_destinazioni = df['Destination'].value_counts().head(10)    # Conta le occorrenze di ogni destinazione e ordina in ordine decrescente
print("Destinazioni maggiori:", top_destinazioni)               # Mostra le destinazioni maggiori con il loro numero di occorrenze


#Visualizziamo con un barplot:

plt.figure(figsize=(10,6))                                                            # Imposta la dimensione del grafico
sns.barplot(x=top_destinazioni.values, y=top_destinazioni.index, palette='viridis')   # Crea il barplot
plt.title("Top 10 destinazioni più visitate")                                         # Imposta il titolo del grafico
plt.xlabel("Numero di viaggi")                                                        # Imposta l'etichetta dell'asse x
plt.ylabel("Destinazione")                                                            # Imposta l'etichetta dell'asse y                                                           #
plt.tight_layout()                                                                    # Ridimensiona automaticamente i grafici
plt.show()                                                                            # Mostra il grafico





#2.2 ANALISI DISTRIBUZIONE DEL COSTO MEDIO PER TIPO DI ALLOGGIO:   


costo_medio_alloggio = df.groupby('Accommodation type')['Accommodation cost'].mean().sort_values()    # Calcola il costo medio per ogni tipo di alloggio
print("Costo medio per tipo di alloggio:", costo_medio_alloggio)                                      # Mostra il costo medio per ogni tipo di alloggio


plt.figure(figsize=(10,6))
sns.barplot(x=costo_medio_alloggio.values, y=costo_medio_alloggio.index, palette='magma')
plt.title("Costo medio per tipo di alloggio")
plt.xlabel("Costo medio (€)")
plt.ylabel("Tipo di alloggio")
plt.tight_layout()
plt.show()





#2.3 ANALISI ESPLORATIVA DELLE PREFERENZE DI TRASPORTO PER FASCIA DI ETA':

#bins: definisce i limiti dei gruppi
#labels: definisce i nomi dei gruppi
#unstack: riporta i dati in formato tabella
#size: conta le occorrenze
#fillna(0): imposta il valore mancante come 0
#pd.cut: crea le fasce


# Creiamo una colonna 'fascia di età':
df['Età fascia'] = pd.cut(df['Traveler age'], bins=[18, 30, 40, 50, 60], labels=['18-30', '31-40', '41-50', '51-60'])


# Raggruppiamo e contiamo il mezzo di trasporto per fascia : 
trasporto_per_età = df.groupby(['Età fascia', 'Transportation type']).size().unstack().fillna(0)
print("Preferenze di trasporto per fascia d'età:", trasporto_per_età)


# Usiamo heatmap per visualizzare i valori ottenuti:
plt.figure(figsize=(10,6))
sns.heatmap(trasporto_per_età, annot=True, cmap='Blues', fmt=".0f")
plt.title("Preferenze di trasporto per fascia d'età")
plt.xlabel("Mezzo di trasporto")
plt.ylabel("Fascia d'età")
plt.tight_layout()
plt.show()







#2.4 ANALISI ESPLORATIVA LINEPLOT DEL COSTO MEDIO PER DURATA DEL VIAGGIO

# Calcolo del costo medio per ciascuna durata
durata_costo = df.groupby('Duration (days)')['Costo totale'].mean()



plt.figure(figsize=(10,6))
sns.lineplot(x=durata_costo.index, y=durata_costo.values, marker='o', color='teal')
plt.title('Costo medio totale in base alla durata del viaggio')
plt.xlabel('Durata del viaggio (giorni)')
plt.ylabel('Costo medio (€)')
plt.grid(True)                                                         # Mostra la griglia
plt.tight_layout()
plt.show()









#PASSO 3: SQL – ANALISI DEL DATASET CON QUERY 


#3.1 Connessione al database SQLite e salvataggio del DataFrame

import sqlite3                                          # Importa la libreria per gestire database SQLite
from sqlalchemy import create_engine, text              # Importa funzioni per collegarsi a un database SQL


from dotenv import load_dotenv      #per caricare le variabili d'ambiente
import os                           #per accedere alle variabili d'ambiente
load_dotenv()                       #per caricare le variabili d'ambiente
db_path= os.getenv("DBPATH")        #per caricare le variabili d'ambiente

engine = create_engine(db_path)     #crea un engine per la connessione al database




# Crea o apre un database chiamato 'esercizio_viaggi.db':
conn = sqlite3.connect('esercizio_viaggi.db')     



# Salva il DataFrame 'df' come tabella SQL chiamata 'esercizio_viaggi'
df.to_sql('esercizio_viaggi', conn, if_exists='replace', index=False)





#3.2 VIAGGIATORI AMERICANI CON SPESA SOPRA I €2000 


americani_spesa_sopra_2000 = pd.read_sql_query("""
       SELECT "Traveler name", "Destination", "Costo totale"
       FROM esercizio_viaggi
       WHERE "Traveler nationality" = 'American' AND "Costo totale" > 2000
       ORDER BY "Costo totale" DESC
       """, conn)


print("I viaggiatori Americani con spesa sopra i 2000 sono: ")
print(americani_spesa_sopra_2000)






#3.3 VIAGGI PIU COSTOSI (TOP 5) 

viaggi_più_costosi_top5 = pd.read_sql_query("""
          SELECT "Traveler name", "Destination", "Costo totale"
          FROM esercizio_viaggi
          ORDER BY "Costo totale" DESC
          LIMIT 5
          """, conn)


print("I viaggi piu costosi sono: ")
print(viaggi_più_costosi_top5)





#3.4 COSTO MEDIO TOTALE PER NAZIONALITA'

costo_medio_totale_per_nazionalità = pd.read_sql_query("""
          SELECT "Traveler nationality", AVG("Costo totale") AS "Costo medio totale"
          FROM esercizio_viaggi
          GROUP BY "Traveler nationality"
          ORDER BY "Costo medio totale" DESC
          """, conn)

print("Costo medio totale per nazionalità: ")
print(costo_medio_totale_per_nazionalità)






#3.5 MEZZI DI TRASPORTO USATI DA VIAGGIATORI TRA I 25 E I 35 ANNI:

mezzi_di_trasporto_usati_da_viaggiatori_tra_i_25_e_i_35_anni = pd.read_sql_query("""
          SELECT "Transportation type", COUNT(*) AS "Numero di viaggiatori"
          FROM esercizio_viaggi
          WHERE "Traveler age" BETWEEN 25 AND 35
          GROUP BY "Transportation type"
          ORDER BY "Numero di viaggiatori" DESC
          """, conn)

print("Mezzi di trasporto usati da viaggiatori tra i 25 e i 35 anni: ")
print(mezzi_di_trasporto_usati_da_viaggiatori_tra_i_25_e_i_35_anni)





#3.6 COSTO PER UN GIORNO MEDIO PER DESTINAZIONE:

costo_per_un_giorno_medio_per_destinazione = pd.read_sql_query("""
          SELECT "Destination", AVG("Costi per giorno") AS "Costo medio per giorno"
          FROM esercizio_viaggi
          GROUP BY "Destination"
          ORDER BY "Costo medio per giorno" DESC
          """, conn)

print("Costo per un giorno medio per destinazione: ")
print(costo_per_un_giorno_medio_per_destinazione)






#3.7 DURATA MEDIA DEI VIAGGI PER MEZZO DI TRASPORTO:


durata_media_dei_viaggi_per_mezzo_di_trasporto = pd.read_sql_query("""
          SELECT "Transportation type", AVG("Duration (days)") AS "Durata media dei viaggi"
          FROM esercizio_viaggi
          GROUP BY "Transportation type"
          ORDER BY "Durata media dei viaggi" DESC
          """, conn)


print("Durata media dei viaggi per mezzo di trasporto: ")
print(durata_media_dei_viaggi_per_mezzo_di_trasporto)









#PASSO 4: MACHINE LEARNING - REGRESSIONE LINEARE MULTIPLA CON SCIKIT-LEARN: 

#Obbiettivo: Prevedere il costo totale del viaggio usando: 
        #-Regressione Lineare Multipla (più variabili)


#Prevedere il costo totale del viaggio in base a:
    #-durata del viaggio
    #-età del viaggiatore
    #-stagione del viaggio
    #-destinazione
    #-nazionalità
    #-genere del viaggiatore
    #-Accommodation cost



#4.1 Importazione e lettura del dataset:

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error 
from sklearn.preprocessing import LabelEncoder, StandardScaler


#4.2 Creazione della colonna "Season":

# Funzione per convertire mese in stagione
def get_season(date):
    if pd.isnull(date):
        return None
    month = date.month
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Autumn'

# Applica la funzione
df['Season'] = df['Start date'].apply(get_season)



X = df[
    [
        "Duration (days)",
        "Season",
        "Destination",
        "Transportation type",   
    ]
]

# Identifichiamo le colonne numeriche e categoriche PRIMA della codifica
categorical_features = X.select_dtypes(include=["object"]).columns.tolist()


print(f"Features categoriche: {categorical_features}")


X_processed = X.copy()


label_encoders = {}

for feature in categorical_features:
    le = LabelEncoder()
    X_processed[feature] = le.fit_transform(X_processed[feature])
    label_encoders[feature] = le


y = df["Transportation cost"]  # Variabile dipendente da predire


# Suddividiamo il dataset in training (80%) e test (20%):

X_train, X_test, y_train, y_test = train_test_split(
          X, y, test_size=0.2, random_state=42
)

# 4.4.1 Normalizzazione delle features con StandardScaler:



# 4.5 Creazione e addestramento del modello:

model = LinearRegression()  # Creiamo il modello di regressione lineare

model.fit(
    X_train, y_train
)  # Alleniamo il modello sui dati di training normalizzati

print("Modello addestrato con successo sui dati normalizzati!")









# 4.6


# Previsioni sui dati di test normalizzati
y_pred = model.predict(X_test)


print("Valutazione del modello:")

print("RMSE", np.sqrt(mean_squared_error(y_test, y_pred)))  # Calcola la radice quadrata dell'errore quadratico medio
print("MAE", mean_absolute_error(y_test, y_pred))  # Calcola l'errore assoluto medio
print("R2", r2_score(y_test, y_pred))  # Calcola il coefficiente di determinazione


features = X_processed.columns
coefficients = model.coef_
intercept = model.intercept_

print(f"Intercetta: {intercept:.2f} $")  # Stampa l'intercetta


for feature, coef in zip(
    features, coefficients
):  # Cicla sulle colonne e sui coefficienti
    print(
        f"Coefficiente per {feature}: {coef:.2f} $ per unità"
    )  # Stampa il coefficiente per ogni colonna

# Nota: I coefficienti per le features numeriche normalizzate rappresentano
# l'impatto di una deviazione standard sulla variabile target









