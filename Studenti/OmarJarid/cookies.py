from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

def click_tot_volte_cookie(btn_cookie, n_clicks = 1):
    for _ in range(n_clicks): btn_cookie.click()

def accept_cookies(driver):
    try:
        button_cookies = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/div[2]/button[1]/p")
            )
        )
        button_cookies.click()
        print("Cookies accepted")
    except Exception as e:
        print("No cookies button found or already clicked:", e)

driver.get("https://cookie-clicker2.com/")

accept_cookies(driver)

iframe1 = driver.find_element(By.XPATH, '//*[@id="iframehtml5"]')
driver.switch_to.frame(iframe1)

iframe2 = driver.find_element(By.XPATH, '//*[@id="iframehtml5"]')
driver.switch_to.frame(iframe2)

btn_cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]') 
btn_cookie.click()

click_tot_volte_cookie(btn_cookie, n_clicks = 100)

t.sleep(1000)