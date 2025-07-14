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

driver = webdriver.Chrome()

driver.get("https://www.amazon.it/s?k=rtx+5070&i=computers&crid=14M9WILRIOQGM&sprefix=RTX+5070%2Ccomputers%2C120&ref=nb_sb_ss_mvt-t11-ranker_2_8")



def accept_cookies(driver):
    try:
        button_cookies = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="sp-cc-accept"]')))
        button_cookies.click()
        print("Cookies accepted")
    except Exception as e:
        print("Cookies not accepted:", e)

accept_cookies(driver)

t.sleep(10000)

