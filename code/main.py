from selenium import webdriver
import exercises as ex
from pynput.keyboard import Controller as KeyController
import keyboard
import mouse
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

def comic(driver):
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'MasterHintContent')))
    arr = driver.find_elements(By.CLASS_NAME, 'simple-view-card ')
    button = driver.find_element(By.XPATH, '//*[@id="ActivityContent_SimpleView"]/span[3]')
    for i in range(len(arr)):
        button.click()
        time.sleep(0.5)

def mixed_sentences(driver):
    main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "MasterHintContent")))
    w_arr = driver.find_elements(By.CLASS_NAME, 'draggmeEvent')
    num = 1
    for i in range(len(w_arr)):
        for box in w_arr:
            if int(box.get_attribute("elid")) == num:
                num += 1
                box.click()

def L_Homme_Noye(driver):
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

def multiple_choice(driver):
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

def main():
    link = input("What is the link? ")
    options = Options()
    options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })
    driver_path = './chrome/chromedriver'
    driver = webdriver.Chrome(options = options, executable_path = driver_path, service=Service(ChromeDriverManager().install()))
    driver.get(link)

    f_email = driver.find_element(By.ID, "smTxtEmail").send_keys("guerard@jm302.com")
    f_password = driver.find_element(By.ID, "smTxtPassword").send_keys("smash")
    log_in = driver.find_element(By.ID, "smBtnLogin").click()
    ex.phrase_complete(driver)
    time.sleep(1000000) 
if __name__ == '__main__':
    main()
