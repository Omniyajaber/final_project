import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def open_site(driver, url):
    driver.get(url)
    time.sleep(3)
    return driver.current_url


def signin(driver, username, password):
    name = driver.find_element(By.CSS_SELECTOR, '#user-name')
    name.send_keys('standard_user')
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('secret_sauce')
    time.sleep(4)
    button = driver.find_element(By.CSS_SELECTOR, '#login-button')
    button.click()
    time.sleep(3)
    return driver.current_url
driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')
open_site = (driver,'https://www.saucedemo.com/')
login = (driver,'username','password')