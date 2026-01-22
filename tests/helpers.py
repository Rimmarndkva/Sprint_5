from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators

def login_user(driver): 
    email = "rimmarendikova39@yandex.ru"
    password = "password123"

    email_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.EMAIL_INPUT))
    email_input.clear()
    email_input.send_keys(email)

    pass_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
    pass_input.clear()
    pass_input.send_keys(password)

    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()