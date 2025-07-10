
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time as t
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# import pandas as pd

# driver = webdriver.Chrome()
# driver.get("https://www.amazon.it/s?k=fotocamera&__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=32DEPP0VU40EW&sprefix=fotocamera%2Caps%2C184&ref=nb_sb_noss_1")

# t.sleep(10000)

# def accept_cookies(driver): 
#     try:
#      WebDriverWait(driver, 5).until(
#         EC.visibility_of_element_located((By.XPATH, '//*[@id="sp-cc-accept"]'))
#     ).click()
#     except Exception as e:
#      print("Nessun pulsante 'Accetta' trovato:", e)
    
   
# accept_cookies(driver)

# container_fotocamere = driver.find_element(
#   By.XPATH, ('//*[@id="search"]/div[1]/div[1]/div/span[1]') 
# )

# fotocamera_divs = container_fotocamere.find_elements(
#   By.XPATH, ('//div[contains(@class,"sg-col-inner")]')
# )

# for fotocamera_div in fotocamera_divs:
#     print(fotocamera_div.text)

# t.sleep(10000)

# driver.close()