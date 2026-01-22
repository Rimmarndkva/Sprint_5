from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from locators import ConstructorPageLocators, LoginPageLocators, ProfilePageLocators


class TestConstructor:

    def test_switch_to_sauces(self, driver): 
        driver.get("https://stellarburgers.education-services.ru")
        driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
        
        tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.SAUCES_TAB)
        )
        assert ConstructorPageLocators.ACTIVE_TAB_CLASS in tab.get_attribute("class")

    def test_switch_to_fillings(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        driver.find_element(*ConstructorPageLocators.FILLINGS_TAB).click()
        
        tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.FILLINGS_TAB)
        )
        assert ConstructorPageLocators.ACTIVE_TAB_CLASS in tab.get_attribute("class")

    def test_switch_to_buns(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        driver.find_element(*ConstructorPageLocators.SAUCES_TAB).click()
        driver.find_element(*ConstructorPageLocators.BUNS_TAB).click()
        
        tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.BUNS_TAB)
        )
        assert ConstructorPageLocators.ACTIVE_TAB_CLASS in tab.get_attribute("class")

    def test_go_to_constructor_from_logo(self, driver):
        driver.get("https://stellarburgers.education-services.ru/account/profile")
        

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ProfilePageLocators.SAVE_BUTTON))
        
        logo = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(ConstructorPageLocators.LOGO))
        logo.click()
        
        assert WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.CONSTRUCTOR_HEADER))