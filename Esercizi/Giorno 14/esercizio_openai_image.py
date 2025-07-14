import base64  # Importa il modulo base64 per codificare dati binari in stringhe base64
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

image_path = r"Esercizi\Giorno 14\eevee.png"  # Specifica il percorso dell'immagine

base64_image = base64.b64encode(open(image_path, "rb").read()).decode(
    "utf-8"
)  # Legge l'immagine in modalità binaria, la codifica in base64 e la converte in stringa

response = client.chat.completions.create(  # Invia una richiesta di completamento chat al modello OpenAI
    model="gpt-4.1-nano",  # Specifica il modello da utilizzare
    messages=[
        {
            "role": "user",  # Definisce il ruolo del messaggio come utente
            "content": [
                {
                    "type": "text",  # Specifica che il contenuto è di tipo testo
                    "text": "Descrivi l'immagine",  # Testo della richiesta
                },
                {
                    "type": "image_url",  # Specifica che il contenuto è un'immagine
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",  # Inserisce l'immagine codificata in base64 come URL
                    },
                },
            ],
        }
    ],  # Messaggio dell'utente con la richiesta e l'immagine
)

print(
    response.choices[0].message.content
)  # Stampa il contenuto della risposta generata dal modello
