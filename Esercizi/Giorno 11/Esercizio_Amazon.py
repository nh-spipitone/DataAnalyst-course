from selenium import webdriver
import pandas as pd  # Importa pandas per la gestione dei dati in DataFrame

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

options = Options()  # Crea un oggetto Options per configurare Chrome
options.add_argument("--window-size=1920,1080")  # Imposta la dimensione della finestra

driver = webdriver.Chrome(options=options)  # Avvia Chrome con le opzioni specificate

driver.get(
    "https://www.amazon.it/s?k=fotocamera&crid=356B349BUEB27&sprefix=foto%2Caps%2C100&ref=nb_sb_ss_mvt-t11-ranker_3_4"
)


def accept_cookies(driver):
    try:
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="sp-cc-accept"]'))
        ).click()
    except Exception as e:
        print("Nessun pulsante 'Accetta' trovato:", e)


accept_cookies(driver)

container_fotocamere = driver.find_element(
    By.XPATH, ('//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[1]')
)

fotocamera_divs = container_fotocamere.find_elements(
    By.XPATH, ('//div[contains(@class,"puis-card-container")]')
)

lista_fotocamere = []

for fotocamera_div in fotocamera_divs:
    # //*[@id="35aef368-3645-4725-8248-2e9faaaa25da"]/div/div/div/div/span/div
    # //*[@id="35aef368-3645-4725-8248-2e9faaaa25da"]/div/div/div/div/span/div/div/div[2]/div[2]/div[1]/a/span
    description = fotocamera_div.find_element(By.TAG_NAME, "h2").text
    try:
        price = fotocamera_div.find_element(By.CLASS_NAME, "a-price").text
    except:
        price = "N/A"
    try:
        n_recensioni = fotocamera_div.find_element(
            By.CSS_SELECTOR, "span.a-size-base.s-underline-text"
        ).text
    except:
        n_recensioni = "N/A"

    # Trova l'immagine della fotocamera
    img = fotocamera_div.find_element(By.XPATH, ".//img").get_attribute("src")
    lista_fotocamere.append(
        {
            "description": description,
            "price": price,
            "n_recensioni": n_recensioni,
            "img": img,
        }
    )

print(len(fotocamera_divs), "fotocamere trovate.")

fotocamere_df = pd.DataFrame(lista_fotocamere)

print(fotocamere_df)
