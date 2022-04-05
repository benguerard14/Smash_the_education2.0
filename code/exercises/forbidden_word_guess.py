from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def forbidden_word_guess(driver):
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "MasterHintContent")))
    arr = driver.find_elements(By.CLASS_NAME, "textarea")
    for i in range(len(arr)):
        answer = driver.find_element(By.XPATH, f'//*[@id="Answer_{i + 1}"]/span').get_attribute("textContent")
        arr[i].send_keys(answer)
    button = driver.find_element(By.ID, 'ActivityContent_sendAnswers').click()


