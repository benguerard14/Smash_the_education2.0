from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def image_choose(driver):
    try:
        main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="draggables"]/div[1]')))
        arr = []
        for i in range(6):
            t = driver.find_element(By.XPATH, f'//*[@id="draggables"]/div[{i + 1}]').get_attribute("elid")
            arr.append(t)
        for i in range(6):
             image = driver.find_element(By.ID, f"resultBox_{arr[i]}").click()
        time.sleep(100)
    except Exception as e:
        print(e)
        driver.quit()
