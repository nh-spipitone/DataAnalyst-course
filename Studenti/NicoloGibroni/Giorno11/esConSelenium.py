from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://quotes.toscrape.com/")

divPrincipale = driver.find_element(By.XPATH, '/html/body/div/div[2]')
quotes = divPrincipale.find_elements(By.CLASS_NAME, "quote")
listaQuotes = []
tagUnici = set()
for quote in quotes:
    tagList = []
    text = quote.find_element(By.CLASS_NAME, "text").text
    author = quote.find_element(By.CLASS_NAME, "author").text
    tags = quote.find_elements(By.CLASS_NAME, "tag")
    for tag in tags:
        tagList.append(tag.text)
        tagUnici.add(tag.text)
    listaQuotes.append({"text":text, "author":author, "tags":tagList})
driver.quit()
print(listaQuotes)
print("________________")
print(tagUnici)
