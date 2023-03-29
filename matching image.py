# ---------------------- different pictures----------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def open_site(driver, url):
    driver.get(url)
    time.sleep(5)
    return driver.current_url

def login(driver, username, password):
    name = driver.find_element(By.CSS_SELECTOR, '#user-name')
    name.send_keys('standard_user')
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('secret_sauce')
    time.sleep(4)
    button = driver.find_element(By.CSS_SELECTOR, '#login-button')
    button.click()
    time.sleep(3)

def images():
    image_first = driver.find_element(By.CSS_SELECTOR, '#item_3_img_link')
    image_first.click()
    time.sleep(3)

def image():
    image_second = driver.find_element(By.CSS_SELECTOR, '#item_1_img_link')
    image_second.click()
    return driver.current_url

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
open_site(driver,'https://www.saucedemo.com/')
login(driver,'username','password')
