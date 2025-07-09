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


# Funzione per accettare i cookies se il popup è presente
def accept_cookies(driver):
    try:
        # Attende fino a che il bottone dei cookies è visibile (max 5 secondi)
        button_cookies = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="notice"]/div[3]/button[2]')
            )
        )
        # Clicca sul bottone per accettare i cookies
        button_cookies.click()
        print("Cookies accepted")
    except Exception as e:
        # Se il bottone non viene trovato o è già stato cliccato, stampa un messaggio
        print("No cookies button found or already clicked:", e)


# Crea un oggetto Options per configurare Chrome
options = Options()
# options.add_argument("--headless=new")  # (opzionale) esegue Chrome in modalità headless
options.add_argument("--window-size=1920,1080")  # Imposta la dimensione della finestra

# Avvia una nuova istanza di Chrome con le opzioni specificate
driver = webdriver.Chrome(options=options)

# Apre la pagina del Pokédex nazionale su Pokémon Central Wiki
driver.get(
    "https://wiki.pokemoncentral.it/Elenco_dei_Pok%C3%A9mon_secondo_il_Pok%C3%A9dex_Nazionale"
)
# Trova l'iframe che contiene il messaggio dei cookies tramite XPATH
iframe = driver.find_element(By.XPATH, '//*[@id="sp_message_iframe_1322648"]')
# Passa il controllo all'interno dell'iframe
driver.switch_to.frame(iframe)

# Chiama la funzione per accettare i cookies
accept_cookies(driver)

# Torna al contesto principale della pagina (fuori dall'iframe)
driver.switch_to.default_content()

# Trova il contenitore della prima generazione tramite XPATH
contenitore_prima_gen = driver.find_element(
    By.XPATH, '//*[@id="mw-content-text"]/div[2]/div[3]'
)
# Trova tutti i div figli diretti con classe "width-xl-33" (ogni Pokémon)
pokemon_divs = contenitore_prima_gen.find_elements(
    By.XPATH, ".//div[contains(@class, 'width-xl-33')]"
)

# Crea una lista vuota per salvare i dati dei Pokémon
pokedex_rows = []

# Cicla su ogni div di Pokémon trovato
for pokemon in pokemon_divs:
    # Divide il testo del div in righe (numero, nome, tipo)
    poke_string = pokemon.text.split("\n")
    number = poke_string[0]  # Numero del Pokémon
    name = poke_string[1]  # Nome del Pokémon
    types = poke_string[2]  # Tipo del Pokémon
    # Aggiunge i dati come dizionario alla lista
    pokedex_rows.append({"number": number, "name": name, "Types": types})

# Crea un DataFrame pandas con i dati raccolti
pokedex_prima_gen_df = pd.DataFrame(pokedex_rows, columns=["number", "name", "Types"])
# Salva il DataFrame in un file CSV
pokedex_prima_gen_df.to_csv("Esercizi/Giorno 11/pokedex_prima_gen.csv", index=False)

# Mantiene il browser aperto per 10000 secondi (per debug o visualizzazione)
t.sleep(10000)
