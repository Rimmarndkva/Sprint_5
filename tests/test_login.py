import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import ConstructorPageLocators, LoginPageLocators, ProfilePageLocators
from helpers import login_user

class TestLogin:

    def test_login_main_page_button(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.MAIN_LOGIN_BUTTON)).click()
        
        login_user(driver)
        
        check_success = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.ORDER_BUTTON))
        assert check_success.is_displayed()

    def test_login_personal_account(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        
        login_user(driver)

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ConstructorPageLocators.CONSTRUCTOR_HEADER))

    def test_login_registration_form(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")
        
      
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.REGISTRATION_FORM_LOGIN_LINK)).click()
        
        login_user(driver)

        assert WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

    def test_login_forgot_password(self, driver):
        driver.get("https://stellarburgers.education-services.ru/forgot-password")
        
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.FORGOT_PASSWORD_LOGIN_LINK)).click()
        
        login_user(driver)
       
        assert WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))

    def test_logout(self, driver):
        driver.get("https://stellarburgers.education-services.ru/login")
        

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LoginPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
        
        login_user(driver)
     
        logout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON))
        logout_btn.click()
        
      
        assert WebDriverWait(driver, 10).until(EC.url_contains("/login"))
        
       
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))