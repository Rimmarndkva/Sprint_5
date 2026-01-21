import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import LoginPageLocators, ProfilePageLocators
from conftest import login 

def test_login_main_page_button(driver):
    driver.get("https://stellarburgers.education-services.ru")

    driver.find_element(*LoginPageLocators.MAIN_LOGIN_BUTTON).click()
    
    login(driver) 
    
 
    check_success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, ".//button[text()='Оформить заказ']")))
    assert check_success.is_displayed()

def test_login_personal_account(driver):
    driver.get("https://stellarburgers.education-services.ru")
    driver.find_element(*LoginPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
    login(driver)

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, ".//h1[text()='Соберите бургер']")))

def test_login_registration_form(driver):
    driver.get("https://stellarburgers.education-services.ru/register")
  
    driver.find_element(*LoginPageLocators.REGISTRATION_FORM_LOGIN_LINK).click()
    login(driver)
    assert WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

def test_login_forgot_password(driver):
    driver.get("https://stellarburgers.education-services.ru/forgot-password")

    driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LOGIN_LINK).click()
    login(driver)
    assert WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

def test_logout(driver):
    driver.get("https://stellarburgers.education-services.ru/login")
    login(driver)
    

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
    

    logout_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON))
    logout_btn.click()
    

    assert WebDriverWait(driver, 10).until(EC.url_contains("/login"))

    assert driver.find_element(*LoginPageLocators.LOGIN_BUTTON)