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

driver = webdriver.Chrome()  # Avvia Chrome con le opzioni specificate

driver.get("https://www.amazon.it/s?k=fotocamera&crid=356B349BUEB27&sprefix=foto%2Caps%2C100&ref=nb_sb_ss_mvt-t11-ranker_3_4")


def accept_cookies(driver): 
    try:
     WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="sp-cc-accept"]'))
    ).click()
    except Exception as e:
     print("Nessun pulsante 'Accetta' trovato:", e)
    
   
accept_cookies(driver)

container_fotocamere = driver.find_element(
  By.XPATH, ('//*[@id="search"]/div[1]/div[1]/div/span[1]') 
)

fotocamera_divs = container_fotocamere.find_elements(
  By.XPATH, ('//div[contains(@class,"sg-col-inner")]')
)

for fotocamera_div in fotocamera_divs:
    print(fotocamera_div.text)

t.sleep(10000)




        