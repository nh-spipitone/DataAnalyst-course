# Importa il modulo webdriver di Selenium per controllare il browser
from selenium import webdriver

# Importa By per selezionare elementi tramite vari metodi (id, xpath, ecc.)
from selenium.webdriver.common.by import By

# Importa il modulo time come t per eventuali pause
import time as t

# Importa WebDriverWait per gestire attese esplicite
from selenium.webdriver.support.ui import WebDriverWait

# Importa expected_conditions per condizioni di attesa
from selenium.webdriver.support import expected_conditions as EC

# Importa le opzioni di Chrome per configurare il browser
from selenium.webdriver.chrome.options import Options

# Importa pandas per la gestione dei dati in DataFrame
import pandas as pd


# Importa il modulo webdriver di Selenium per controllare il browser
from selenium import webdriver

# Importa By per selezionare elementi tramite vari metodi (id, xpath, ecc.)
from selenium.webdriver.common.by import By

# Importa il modulo time come t per eventuali pause
import time as t

# Importa WebDriverWait per gestire attese esplicite
from selenium.webdriver.support.ui import WebDriverWait

# Importa expected_conditions per condizioni di attesa
from selenium.webdriver.support import expected_conditions as EC

# Importa le opzioni di Chrome per configurare il browser
from selenium.webdriver.chrome.options import Options

# Importa pandas per la gestione dei dati in DataFrame
import pandas as pd

# Configura le opzioni di Chrome (opzionale)
options = Options()
options.add_argument("--start-maximized")  # Avvia la finestra massimizzata

# Avvia il browser Chrome
driver = webdriver.Chrome(options=options)

# Vai al sito di esempio
driver.get("https://quotes.toscrape.com/")

# Attendi che le citazioni siano visibili prima di procedere (attesa esplicita)
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "text"))
)

# Trova tutti gli elementi che contengono i titoli delle citazioni
quotes = driver.find_elements(By.CLASS_NAME, "text")

# Estrai e stampa i titoli delle citazioni
for quote in quotes:
    print(quote.text)

# Pausa per osservare l'output
t.sleep(3)

# Chiudi il browser
driver.quit()
