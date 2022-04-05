from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def voice_test(driver):
    try:
        main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Sequence_1")))
        exercises = driver.find_elements(By.CLASS_NAME, 'activity-o-card-answerbase')
        button_1 = driver.find_element(By.ID, "Sequence_1").click()
        for i in range(len(exercises)):
            for i in range(3):
                time.sleep(1)
                voice_button = driver.find_element(By.XPATH, '//*[@id="r01"]/div[2]').click()
                time.sleep(1)
                voice_button = driver.find_element(By.XPATH, '//*[@id="r01"]').click()
                time.sleep(1)
    except Exception as e:
        print(e)

