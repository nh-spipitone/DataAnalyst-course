from openai import OpenAI  # Importa la classe OpenAI per interagire con l'API OpenAI
from dotenv import (
    load_dotenv,
)  # Importa load_dotenv per caricare variabili d'ambiente da un file .env
import os  # Importa os per interagire con il sistema operativo
import json

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Recupera la chiave API di OpenAI dalla variabile d'ambiente
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Crea un'istanza del client OpenAI usando la chiave API
client = OpenAI(api_key=OPENAI_API_KEY)

# Realizziamo un ai modello che genera un file JSONL per il fine-tuning


def generate_jsonl_for_finetuning(data, filename="finetuning_data.jsonl"):
    """
    Genera un file JSONL per il fine-tuning e lo salva su disco.

    Args:
        data (list): Lista di dizionari contenenti le coppie domanda-risposta.
        filename (str): Nome del file da creare (default: "finetuning_data.jsonl").

    Returns:
        str: Path del file salvato.
    """
    jsonl_lines = []
    for item in data:
        jsonl_lines.append(
            json.dumps(item)
        )  # Converte ogni dizionario in una stringa JSON

    jsonl_content = "\n".join(jsonl_lines)  # Unisce le stringhe JSON con newline
    jsonl_content += "\n"  # Aggiunge una newline finale per conformità al formato JSONL

    # Salva il contenuto JSONL in un file
    with open(filename, "a", encoding="utf-8") as f:
        f.write(jsonl_content)

    print(f"File JSONL salvato come: {filename}")
    return filename  # Restituisce il path del file salvato


def get_5_jsonl_query(questions, answers):
    """
    Genera un file JSONL per il fine-tuning con 5 domande e risposte.

    Args:
        questions (list): Lista di domande.
        answers (list): Lista di risposte corrispondenti.

    Returns:
        str: Stringa in formato JSONL.
    """
    data = []
    for question, answer in zip(questions, answers):
        data.append(
            {
                "messages": [
                    {"role": "user", "content": question},
                    {"role": "assistant", "content": answer},
                ]
            }
        )  # Crea un dizionario per ogni coppia domanda-risposta
    return generate_jsonl_for_finetuning(data)  # Genera il JSONL dal dizionario creato


def function_calling(tool_calls):
    """
    Gestisce le chiamate agli strumenti (tool_calls) per generare JSONL.

    Args:
        tool_calls (list): Lista di chiamate agli strumenti.

    Returns:
        str: Risultato della chiamata allo strumento.
    """
    for tool_call in tool_calls:  # Itera su tutte le chiamate agli strumenti
        if (
            tool_call.function.name == "get_5_jsonl_query"
        ):  # Se il nome della funzione è 'get_5_jsonl_query'
            args = json.loads(
                tool_call.function.arguments
            )  # Decodifica gli argomenti JSON
            return get_5_jsonl_query(
                args["questions"], args["answers"]
            )  # Restituisce il JSONL generato


tools = [
    {
        "type": "function",  # Tipo di strumento: funzione
        "function": {
            "name": "get_5_jsonl_query",  # Nome della funzione
            "description": "Generate Q&A in conversation format for finetuning in jsonl",  # Descrizione della funzione
            "parameters": {
                "type": "object",  # Tipo di parametri: oggetto
                "properties": {
                    "questions": {
                        "type": "array",  # Tipo di proprietà: array
                        "items": {
                            "type": "string",  # Ogni elemento dell'array è una stringa
                        },
                        "description": "List of questions to generate JSONL for finetuning.",
                    },
                    "answers": {
                        "type": "array",  # Tipo di proprietà: array
                        "items": {
                            "type": "string",  # Ogni elemento dell'array è una stringa
                        },
                        "description": "List of answers corresponding to the queries.",
                    },
                },
                "required": ["questions", "answers"],  # Parametri obbligatori
                "additionalProperties": False,  # Non sono ammessi parametri aggiuntivi
            },
            "strict": True,  # Parametri devono essere rispettati rigorosamente
        },
    }
]


def generate_openai_jsonl(data, n_examples=5, model="gpt-4o-mini"):
    responses = []
    for i in range(n_examples):
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that generates JSONL files for fine-tuning.",
                },
                {
                    "role": "user",
                    "content": f"Genera 5 nuove Q&A prendendo spunto da queste: {data}",
                },
            ],
            tools=tools,
            temperature=0.8,
            tool_choice="required",
        )
        function_calling(response.choices[0].message.tool_calls)
        responses.append(response)

    return responses


def load_jsonl_file_data(filename):
    """
    Carica i dati da un file JSONL.

    Args:
        filename (str): Nome del file JSONL da caricare.

    Returns:
        list: Lista di dizionari contenenti i dati del file.
    """
    data = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line.strip()))  # Carica ogni riga come un dizionario
    return data


data = load_jsonl_file_data(r"Esercizi\Giorno 15\corso_data_analyst.jsonl")

generate_openai_jsonl(
    data, 2, model="gpt-4.1-nano"
)  # Genera 10 esempi di Q&A usando il modello specificato
