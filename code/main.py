from selenium import webdriver
import exercises as ex
from pynput.keyboard import Controller as KeyController
import keyboard
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

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
    ex.voice_test(driver)
    time.sleep(1000000) 
if __name__ == '__main__':
    main()
