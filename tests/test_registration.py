import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators, LoginPageLocators
from generators import generate_email, generate_password

def test_successful_registration(driver):
    driver.get("https://stellarburgers.education-services.ru/register")
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
    ).send_keys("Rimma")
    
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("password123")
    
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    
    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
    assert "/login" in driver.current_url

def test_registration_with_short_password(driver):
    driver.get("https://stellarburgers.education-services.ru/register")
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
    ).send_keys("Rimma")
    
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(generate_email())
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("123") 
    
    driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
    
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegistrationPageLocators.ERROR_PASSWORD) )
    
    assert error_message.text == "Некорректный пароль"

    assert "/register" in driver.current_url