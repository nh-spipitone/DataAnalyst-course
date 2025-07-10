# Importa il modulo webdriver di Selenium per controllare il browser
from selenium import webdriver

# Importa By per selezionare elementi tramite vari metodi (id, xpath, ecc.)
from selenium.webdriver.common.by import By

# Importa il modulo time come t per eventuali pause
import time as t

# Importa WebDriverWait per attese esplicite
from selenium.webdriver.support.ui import WebDriverWait

# Importa expected_conditions per condizioni di attesa
from selenium.webdriver.support import expected_conditions as EC

# Importa le opzioni di Chrome
from selenium.webdriver.chrome.options import Options

# Importa pandas (opzionale) e csv per salvare i dati
import pandas as pd
import csv

# Importa WebDriverManager per gestire automaticamente ChromeDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Imposta le opzioni del browser
options = Options()
options.add_argument("--start-maximized")  # Facoltativo: apre Chrome a schermo intero

# Avvia il browser con ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Vai al sito delle citazioni
driver.get("https://quotes.toscrape.com/")

# Inizializza una lista per contenere le citazioni
quotes_data = []

# Loop per scorrere tutte le pagine
while True:
    # Aspetta che le citazioni siano caricate
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
    )

    # Trova tutti gli elementi "quote" nella pagina
    quotes = driver.find_elements(By.CLASS_NAME, "quote")

    # Estrai il testo della citazione e l'autore
    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, "text").text
        author = quote.find_element(By.CLASS_NAME, "author").text
        quotes_data.append([text, author])  # Salva come lista: [citazione, autore]

    # Controlla se c'è un pulsante "Next" per andare alla pagina successiva
    try:
        next_button = driver.find_element(By.CLASS_NAME, "next")
        next_link = next_button.find_element(By.TAG_NAME, "a").get_attribute("href")
        driver.get(next_link)  # Vai alla pagina successiva
    except:
        break  # Se non c'è il pulsante "Next", esci dal ciclo

# Scrivi i dati raccolti in un file CSV
with open("citazioni.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Citazione", "Autore"])  # Intestazioni CSV
    writer.writerows(quotes_data)

print("Citazioni salvate con successo in 'citazioni.csv'.")

# Pausa opzionale per visualizzare l'output
t.sleep(2)

# Chiudi il browser
driver.quit()