from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def comic(driver):
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'MasterHintContent')))
    arr = driver.find_elements(By.CLASS_NAME, 'simple-view-card ')
    button = driver.find_element(By.XPATH, '//*[@id="ActivityContent_SimpleView"]/span[3]')
    for i in range(len(arr)):
        button.click()
        time.sleep(0.5)

