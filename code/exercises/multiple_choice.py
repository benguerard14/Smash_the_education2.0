from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def multiple_choice(driver):
    time.sleep(10)
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ActivityTypeTimeImage"]/div/span')))
    button = driver.find_element(By.XPATH, '//*[@id="ActivityTypeTimeImage"]/div/span').click()
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ConteinerToHide2"]/div/button[1]')))
    button = driver.find_element(By.XPATH, '//*[@id="ConteinerToHide2"]/div/button[1]').click()
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'MasterHintContent')))
    q_arr = driver.find_elements(By.CLASS_NAME, "DrownedLettersEvent")
    for question in q_arr:
        if question.get_attribute("data-answer") == "True":
            question.click()
    button = driver.find_element(By.XPATH, '//*[@id="ConteinerToHide2"]/div/button[2]').click()

