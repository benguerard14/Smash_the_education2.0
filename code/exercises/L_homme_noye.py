from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import keyboard

def L_homme_noye(driver):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    forbidden_letters = ["á", "é", "í", "ó", "ú", "ü"]
    most_forbidden_letters = ["ñ"]
    try:
        main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="MasterHintContent"]')))
        text = driver.find_element(By.NAME, "ctl00$ActivityContent$sequenceAnswer").get_attribute("value")
        text = text.lower()
        keyboard = KeyController()
        value = ""
        for value in text:
            if value in letters:
                keyboard.type(value)
            elif value in forbidden_letters:
                j=forbidden_letters.index(value) + 1
                driver.find_element(By.XPATH, f'//*[@id="blck-2"]/span[{j}]/span').click()
            elif value in most_forbidden_letters:
                driver.find_element(By.XPATH,  '//*[@id="blck-1"]/span/span').click()


        time.sleep(10)
    except Exception as e:
        print(e)
        driver.quit()


