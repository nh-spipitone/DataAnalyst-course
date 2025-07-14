import json  # Importa il modulo json per lavorare con dati in formato JSON
import requests  # Importa il modulo requests per effettuare richieste HTTP
from openai import OpenAI  # Importa la classe OpenAI dal pacchetto openai
from dotenv import (
    load_dotenv,
)  # Importa la funzione load_dotenv per caricare variabili d'ambiente da un file .env
import os  # Importa il modulo os per interagire con il sistema operativo

# Carica le variabili d'ambiente definite nel file .env
load_dotenv()

# Recupera la chiave API di OpenAI dalla variabile d'ambiente
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Crea un'istanza del client OpenAI usando la chiave API
client = OpenAI(api_key=OPENAI_API_KEY)


# Funzione per gestire le chiamate agli strumenti (tool_calls)
def function_calling(tool_calls):
    for tool_call in tool_calls:  # Itera su tutte le chiamate agli strumenti
        if (
            tool_call.function.name == "get_weather"
        ):  # Se il nome della funzione è 'get_weather'
            args = json.loads(
                tool_call.function.arguments
            )  # Decodifica gli argomenti JSON
            temperature = get_weather(
                args["latitude"], args["longitude"]
            )  # Ottiene la temperatura
            return f"The current temperature is {temperature}°C"  # Restituisce la temperatura formattata


# Funzione per ottenere la temperatura attuale da Open-Meteo API
def get_weather(latitude, longitude):
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    )  # Effettua una richiesta GET all'API di Open-Meteo
    data = response.json()  # Converte la risposta in formato JSON
    return data["current"]["temperature_2m"]  # Restituisce la temperatura attuale


# Definizione degli strumenti (tools) disponibili per il modello OpenAI
tools = [
    {
        "type": "function",  # Tipo di strumento: funzione
        "function": {
            "name": "get_weather",  # Nome della funzione
            "description": "Get current temperature for provided coordinates in celsius.",  # Descrizione della funzione
            "parameters": {
                "type": "object",  # Tipo di parametri: oggetto
                "properties": {
                    "latitude": {"type": "number"},  # Proprietà: latitudine (numero)
                    "longitude": {"type": "number"},  # Proprietà: longitudine (numero)
                },
                "required": ["latitude", "longitude"],  # Parametri obbligatori
                "additionalProperties": False,  # Non sono ammessi parametri aggiuntivi
            },
            "strict": True,  # Parametri devono essere rispettati rigorosamente
        },
    }
]

# Richiesta al modello OpenAI con strumenti abilitati
response = client.chat.completions.create(
    model="gpt-4.1-2025-04-14",  # Specifica il modello da utilizzare
    messages=[
        {
            "role": "user",  # Ruolo del messaggio: utente
            "content": "What's the weather like in Napoli today?",  # Contenuto del messaggio
        }
    ],  # Lista dei messaggi
    tools=tools,  # Strumenti disponibili per il modello
    tool_choice="auto",  # Scelta automatica dello strumento da utilizzare
)

# Stampa il risultato della funzione chiamata dal modello
print(function_calling(response.choices[0].message.tool_calls))
