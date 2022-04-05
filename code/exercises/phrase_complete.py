from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def phrase_complete(driver):
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'op1')))
    buttons = driver.find_elements(By.CLASS_NAME, "draggmeEvent")
    for i in range(len(buttons) + 1):
        button = driver.find_element(By.ID, f"op{i + 1}").click()


