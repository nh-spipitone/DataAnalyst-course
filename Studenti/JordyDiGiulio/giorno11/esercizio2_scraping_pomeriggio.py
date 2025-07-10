# Importa il modulo webdriver di Selenium per controllare il browser
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd


options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://quotes.toscrape.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "text"))
)

quotes = driver.find_elements(By.CLASS_NAME, "quote")
print(f"Numero totale di citazioni: {len(quotes)}")

# Estrai e stampa i tag unici
tags = driver.find_elements(By.CLASS_NAME, "tag")
tag_list = set()  # Usare un set per evitare duplicati
for tag in tags:
    tag_list.add(tag.text)

print("Tag unici:")
for tag in sorted(tag_list):  # Ordinati per leggibilità
    print(tag)

# Pausa opzionale
t.sleep(3)

# Chiudi il browser
driver.quit()