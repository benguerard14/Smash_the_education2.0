from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def word_guess(driver):
    try:
        main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "C_Ans")))
        answer = driver.find_element(By.ID, "C_Ans").get_attribute("textContent").split("\n")[1]
        text_box = driver.find_element(By.ID, "Textarea")
        text_box.clear()
        text_box.send_keys(answer)
        verify = driver.find_element(By.ID, "verified").click()
        time.sleep(5)
    except Exception as e:
        print("OOPSIES")
        print(e)
        

