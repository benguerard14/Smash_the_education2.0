from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def mixed_sentences(driver):
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "MasterHintContent")))
    w_arr = driver.find_elements(By.CLASS_NAME, 'draggmeEvent')
    num = 1
    for i in range(len(w_arr)):
        for box in w_arr:
            if int(box.get_attribute("elid")) == num:
                num += 1
                box.click()

