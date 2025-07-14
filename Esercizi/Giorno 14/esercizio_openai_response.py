from openai import OpenAI  # Importa la classe OpenAI dal pacchetto openai
from dotenv import (
    load_dotenv,
)  # Importa la funzione load_dotenv per caricare variabili d'ambiente da un file .env
import os  # Importa il modulo os per interagire con il sistema operativo

# Load environment variables from .env file
load_dotenv()  # Carica le variabili d'ambiente definite nel file .env

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY"
)  # Recupera la chiave API di OpenAI dalla variabile d'ambiente

client = OpenAI(
    api_key=OPENAI_API_KEY
)  # Crea un'istanza del client OpenAI usando la chiave API

response = client.responses.create(  # Invia una richiesta di completamento chat al modello OpenAI
    model="gpt-4.1-nano",  # Specifica il modello da utilizzare
    input="Parla del ruolo di Data Analyst e Data Scientist.",  # Messaggio dell'utente con la richiesta
    temperature=0.7,  # Imposta la temperatura per controllare la creatività
)
print(response.output_text)  # Stampa il contenuto della risposta generata dal modello
