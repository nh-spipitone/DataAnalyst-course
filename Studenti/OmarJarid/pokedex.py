from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as t
import pandas as pd

def accept_cookies(driver):
    try:
        button_cookies = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="notice"]/div[3]/button[2]')
            )
        )
        button_cookies.click()
        print("Pulsante 'Accetta' cliccato con successo.")
    except Exception as e:
        print("Nessun pulsante 'Accetta' trovato:", e)

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

driver.get("https://wiki.pokemoncentral.it/Elenco_dei_Pok%C3%A9mon_secondo_il_Pok%C3%A9dex_Nazionale")

#iframe = driver.find_element(By.XPATH, '//*[@id="sp_message_iframe_1322648"]')
#driver.switch_to.frame(iframe)

#accept_cookies(driver)

#driver.switch_to.default_content()

contenitore_prima_gen = driver.find_element(
    By.XPATH, '//*[@id="mw-content-text"]/div[2]/div[3]'
)

# Prendere i div figli direttamente solo del layer successivo di contenitore_prima_gen
pokemon_divs = contenitore_prima_gen.find_elements(
    By.XPATH, './/div[contains(@class, "width-xl-33")]'
)
pokedex_rows = []

for pokemon in pokemon_divs:
    poke_string = pokemon.text.split("\n")
    number = poke_string[0]
    name = poke_string[1]
    types = poke_string[2]
    pokedex_rows.append(
        {
            "number": number,
            "name": name,
            "Types": types
        }
    )

pokemon_prima_gen_df = pd.DataFrame(pokedex_rows, columns=["number", "name", "Types"])
pokemon_prima_gen_df.to_csv("pokemon_prima_gen.csv", index = False)

t.sleep(10)