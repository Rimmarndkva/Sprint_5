import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def login(driver):
   
    email = "rimmarendikova39@yandex.ru" 
    password = "password123"
    

    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT))
    email_input.clear()
    email_input.send_keys(email)
    
  
    pass_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
    pass_input.clear()
    pass_input.send_keys(password)
 
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()