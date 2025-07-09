from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument("--headless=new")

# Inizializza il driver di Selenium (assicurati di avere il driver corretto per il tuo browser)
driver = webdriver.Chrome(
    options=options
)  # Puoi usare Firefox() o un altro browser supportato

driver.get("https://www.amazon.it/")


webdriver_wait = WebDriverWait(driver, 5)

print("Contenuto pagina:", driver.page_source[:500])
try:
    webdriver_wait.until(
        EC.visibility_of_element_located(
            (
                (
                    By.XPATH,
                    "/html/body/div/div[1]/div[3]/div/div/form/div/div/span/span/button[1]",
                )
            )
        )
    ).click()
except Exception as e:
    print("Nessun pulsante 'Continua' trovato o già cliccato:", e)
try:
    webdriver_wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="sp-cc-accept"]'))
    ).click()
except Exception as e:
    print("Nessun pulsante 'Accetta' trovato:", e)
# button_cookies = driver.find_element(By.XPATH, '//*[@id="sp-cc-accept"]')
# button_cookies.click()
t.sleep(2)
testo_prova = driver.find_element(
    By.XPATH, "/html/body/div[1]/div[1]/div[2]/div[1]/div[3]/div/div/h2"
).text
print("Testo trovato:", testo_prova)
driver.quit()
