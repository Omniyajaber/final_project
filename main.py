from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests


def open_site(driver, url):
    driver.get(url)
    time.sleep(5)
    return driver.current_url


# _______________log in-Negative_________________________

def login(driver, username, password):
    name = driver.find_element(By.CSS_SELECTOR, '#user-name')
    name.send_keys(username)
    time.sleep(3)
    passwordn = driver.find_element(By.CSS_SELECTOR, '#password')
    passwordn.send_keys(password)
    time.sleep(3)
    button = driver.find_element(By.CSS_SELECTOR, '#login-button')
    button.click()
    time.sleep(3)
    return driver.current_url


# _______________log in-Negative______________________________


# ___________________failed_test________________________________



# ___________________failed_test________________________________

# ______________________matching_pictures_test__________________


def image1(driver,url,username,password):
    open_site(driver, url)
    login(driver, username, password)
    image3 = driver.find_element(By.CSS_SELECTOR, '#item_3_img_link')
    return image3.get_attribute('src')

def image2(driver,url,username,password):
    open_site(driver,url)
    login(driver,username, password)
    image3 = driver.find_element(By.CSS_SELECTOR, '#item_1_img_link')
    return image3.get_attribute('src')
# _________________API___________

def send_http_request(url):
    res = requests.get(url)
    return res


def check_status_code(code):
    if 200 <= code < 399:
        print(f"success -->  {code}")
        return True
    else:
        print('error')
        return False


def check_word(code):
    if 400 <= code > 500:
        print(f"success --> {code}")
        return True
    else:
        print(f"yauza --> {code}")
        return False
