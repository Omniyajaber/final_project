import pytest
from main import *
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver

@pytest.fixture
def url():
    return 'https://www.saucedemo.com/'
#--------------------------negative login----------------------------------------

class TestPy:
    @pytest.mark.parametrize('username,password', [('username', 'password')])
    def test_login_negative(self,driver, url,username,password):
        open_site(driver,url)
        expected = url
        actual = login(driver, username, password)
        assert actual == expected

#_________________negative_test_______
    @pytest.mark.parametrize('username,password', [('standard_user', 'secret_sauce')])
    def test_login(self, driver, url, username, password):
        open_site(driver, url)
        expected = url
        actual = login(driver, username, password)
        assert actual != expected
#-----------------------------negative test--------------------------
#------------------------matching pictures---------------------------

    @pytest.mark.parametrize('username,password', [('standard_user', 'secret_sauce')])
    def test_image (self,driver,url,username,password):
        expected =image2(driver, url, username, password)
        actual = image1(driver, url, username, password)
        assert actual != expected

    @pytest.mark.parametrize('username,password', [('problem_user', 'secret_sauce')])
    def test_image(self, driver, url, username, password):
        expected = image2(driver, url, username, password)
        actual = image1(driver, url, username, password)
        assert actual == expected


#------------------------matching pictures---------------------------
#--------------API---------------------------------------------------
class TestApi:

    def test_status_code(self):
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/human'
        res = send_http_request(url)
        assert check_status_code(res.status_code) == True

    def test_check_word(self):
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/omniya'
        res = send_http_request(url)
        assert check_word(res.status_code) == False




