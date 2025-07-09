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

import random  # Importa il modulo random (anche se non viene usato nel codice)

#opzionale in alcuni esercizi
options = Options()  # Crea un oggetto Options per configurare Chrome
options.add_argument(
    "--window-size=1920,1080"
)  # Imposta la dimensione della finestra del browser

driver = webdriver.Chrome(options=options)  # Avvia Chrome con le opzioni specificate

#opzionale in alcuni esercizi
def click_tot_volte_cookie(btn_cookie, n_clicks=1):
    for _ in range(n_clicks):  # Ripete per il numero di click richiesti
        btn_cookie.click()  # Clicca sul grande bottone del cookie

#opzionale in alcuni esercizi
def accept_cookies(driver):
    try:
        # Attende fino a che il bottone dei cookies è visibile (max 5 secondi)
        button_cookies = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/button[1]/p")
            )
        )
        # Clicca sul bottone per accettare i cookies
        button_cookies.click()
        print("Cookies accepted")
    except Exception as e:
        # Se il bottone non viene trovato o è già stato cliccato, stampa un messaggio
        print("No cookies button found or already clicked:", e)


driver.get("https://cookie-clicker2.com/")  # Apre il sito Cookie Clicker 2

accept_cookies(driver)  # Prova ad accettare i cookies

iframe1 = driver.find_element(
    By.XPATH, '//*[@id="iframehtml5"]'
)  # Trova il primo iframe
driver.switch_to.frame(iframe1)  # Passa il controllo all'interno dell'iframe

iframe2 = driver.find_element(
    By.XPATH, '//*[@id="iframehtml5"]'
)  # Trova (di nuovo) l'iframe (probabilmente ridondante)
driver.switch_to.frame(
    iframe2
)  # Passa il controllo all'interno del secondo iframe (potrebbe essere un errore)

btn_cookie = driver.find_element(
    By.XPATH, '//*[@id="bigCookie"]'
)  # Trova il bottone del grande cookie

btn_cookie.click()  # Clicca una volta sul grande bottone del cookie

click_tot_volte_cookie(
    btn_cookie, n_clicks=100
)  # Clicca 100 volte sul bottone del cookie

# Trova il bottone del cookie tramite X (commento non necessario)

t.sleep(1000)  # Attende 1000 secondi prima di chiudere lo script
